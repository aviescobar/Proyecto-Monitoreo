import paramiko
import tkinter as tk
from tkinter import messagebox
import re  # Para validar la IP

class ApagarPCApp:
   def __init__(self, root):
      self.root = root
      self.root.title("Apagar PC")
      self.root.geometry("400x300")
      self.root.configure(bg='white')

      # Título
      titulo = tk.Label(self.root, text="Apagar PC Remoto", font=("Arial", 16, "bold"), bg='white', fg='black')
      titulo.pack(pady=10)

      # Entradas
      self.crear_entrada("IP del Servidor:", "ip")
      self.crear_entrada("Usuario:", "usuario")
      self.crear_entrada("Contraseña:", "contraseña", es_contrasena=True)

      # Botón para apagar
      boton_shutdown = tk.Button(self.root, text="Apagar", command=self.apagar_pc, font=("Arial", 14), bg="#3498db", fg="white")
  
   def crear_entrada(self, texto, atributo, es_contrasena=False):
      """Crea una etiqueta y entrada de texto."""
      frame = tk.Frame(self.root, bg='white')
      frame.pack(pady=5, padx=10)

      label = tk.Label(frame, text=texto, font=("Arial", 12), bg='white', fg='black')
      label.pack(side=tk.LEFT)

      entrada = Entry(frame, font=("Arial", 12), bg='white', fg='black', show="*" if es_contrasena else "")
      entrada.pack(side=tk.LEFT, padx=5)

      setattr(self, f"entrada_{atributo}", entrada)
  
   def validar_ip(self, ip):
      """Valida si la IP tiene un formato correcto."""
      patron = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
      if not re.match(patron, ip):
         messagebox.showerror("Error", "La dirección IP no es válida.")
         return False
      return True

   def apagar_pc(self):
      """Apaga un equipo remoto usando SSH."""
      ip = self.entrada_ip.get()
      user = self.entrada_usuario.get()
      password = self.entrada_contraseña.get()

      if not ip or not self.validar_ip(ip):
         return

      if not user or not password:
         messagebox.showerror("Error", "Todos los campos son obligatorios.")
         return

      try:
         # Conexión SSH
         ssh_client = paramiko.SSHClient()
         ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
         ssh_client.connect(ip, username=user, password=password)

         # Ejecutar el comando de apagado
         command = f'echo {password} | sudo -S shutdown now'
         stdin, stdout, stderr = ssh_client.exec_command(command)

         stdout_output = stdout.read().decode()
         stderr_output = stderr.read().decode()
         print(stdout_output)
         print(stderr_output)

         ssh_client.close()
         messagebox.showinfo("Éxito", "El PC se ha apagado correctamente.")
      except paramiko.AuthenticationException:
         messagebox.showerror("Error", "Autenticación fallida. Verifica el usuario o contraseña.")
      except paramiko.SSHException as e:
         messagebox.showerror("Error", f"Error en la conexión SSH: {str(e)}")
      except Exception as e:
          messagebox.showerror("Error", f"Error inesperado: {str(e)}")

if __name__ == "__main__":
   ventana = tk.Tk()
   app = ApagarPCApp(ventana)
   ventana.mainloop()

















