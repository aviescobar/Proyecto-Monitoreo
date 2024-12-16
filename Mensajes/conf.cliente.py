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
      msg_from_server = client_socket.recv(1024).decode()
      if msg_from_server.lower() == 'exit':
        print("Servidor desconectado")
        client_socket.close()
        break
    print(f"Servidor: {msg_from_server}")

# Función para enviar mensajes al servidor
def enviar_mensajes():
  while True:
      msg_to_server = input("Tú: ")
      client_socket.send(msg_to_server.encode())
