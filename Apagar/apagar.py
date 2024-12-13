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




















