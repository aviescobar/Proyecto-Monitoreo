import socket
import threading

# Configuración del cliente
HOST = '172.168.2.152'  # IP del servidor
PORT = 12345      # Puerto del servidor

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Función para recibir mensajes del servidor
def recibir_mensajes():
  while True:
