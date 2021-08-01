import socket
import time

SERVER = "10.64.37.35"
PORT = 2356
SERVER_ADDR = (SERVER, PORT)
BUFFER = 1024
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
