import socket
import struct
import numpy as np
import cv2

def run_receiver():
  receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
