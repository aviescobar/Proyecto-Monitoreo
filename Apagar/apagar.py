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
