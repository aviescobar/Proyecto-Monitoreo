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
