import paramiko
import tkinter as tk
from tkinter import messagebox

def ejecutar_comando_ssh(host, usuario, contraseña, comando):
  try:
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, username=usuario, password=contraseña)
