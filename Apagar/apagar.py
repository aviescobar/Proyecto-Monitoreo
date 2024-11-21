import paramiko
import tkinter as tk
from tkinter import messagebox

def ejecutar_comando_ssh(host, usuario, contraseña, comando):
  try:
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, username=usuario, password=contraseña)
    stdin, stdout, stderr = ssh_client.exec_command(comando)
    stdin.write(contraseña + '\n')
    stdin.flush()
    salida = stdout.read().decode("utf-8")
    error = stderr.read().decode("utf-8")
    ssh_client.close()
    return salida, error
  except Exception as e:
    return None, str(e)
    
def ejecutar_apagado():
  host = host_entry.get()
  usuario = usuario_entry.get()
  contraseña = contraseña_entry.get()
  comando_apagado = "sudo -S shutdown -h now"
  comando_contraseña = f"echo '{contraseña}' | {comando_apagado}"


  salida, error = ejecutar_comando_ssh(host, usuario, contraseña, comando_contraseña)

  if error and "contraseña para" in error:

    messagebox.showinfo("Éxito", "El equipo Ubuntu se ha apagado correctamente.")
  else:
    messagebox.showinfo("Éxito", "El equipo Ubuntu se ha apagado correctamente.")

def habilitar_boton(event=None):
  if host_entry.get() and usuario_entry.get() and contraseña_entry.get():
    btn_apagar.config(state=tk.NORMAL)
  else:
    btn_apagar.config(state=tk.DISABLED)
    
root = tk.Tk()
root.title("Apagar PC remoto")
root.geometry("380x380")
root.resizable(False, False)

# Obtener dimensiones de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular la posición para centrar la ventana
x = (screen_width // 2) - (380 // 2)
y = (screen_height // 2) - (380 // 2)

root.geometry(f"380x380+{x}+{y}")

tk.Label(root, text="Apagar la computadora de un usuario/cliente").pack(pady=10)

tk.Label(root, text="Ip de la computadora:").pack(anchor="w", padx=20)
host_entry = tk.Entry(root)
host_entry.pack(fill="x", padx=20)



















