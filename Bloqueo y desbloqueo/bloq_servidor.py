import socket

# Configurar el servidor
HOST = "0.0.0.0"  # Escuchar en todas las interfaces
PORT = 5000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
  server.bind((HOST, PORT))
  server.listen(1)
  print(f"Servidor en ejecución en {HOST}:{PORT}")
  conn, addr = server.accept()
  print(f"Conexión establecida desde {addr}")
  with conn:
