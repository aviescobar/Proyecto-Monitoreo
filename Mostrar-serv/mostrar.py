import socket
import mss
import pickle
import struct
import numpy as np  # Importa numpy para la conversion de la imagen

def start_server(host='0.0.0.0', port=9999):
  # Crear socket del servidor
  server_socket = socket.socket(socket.AF_INET , so)
