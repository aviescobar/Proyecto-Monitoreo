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
