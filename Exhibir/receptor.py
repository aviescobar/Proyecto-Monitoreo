import socket
import struct
import numpy as np
import cv2

def run_receiver():
  receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  receiver_socket.connect(('172.168.2.242', 5001))  # Reemplaza 'IP_DEL_SERVIDOR' con la IP del servidor
  print("Conectado al servidor para recibir la pantalla.")

  data = b""
  payload_size = struct.calcsize(">L")
  
  try:
      while True:
        # Recibir el tamaño de la imagen
        while len(data) < payload_size:
           data += receiver_socket.recv(4096)

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        print("Tamaño de imagen recibida en el receptor (esperado):", msg_size)

        # Recibir la imagen
        while len(data) < msg_size:
        
        
