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



















