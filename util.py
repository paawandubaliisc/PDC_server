import socket
import time


class pdc:
    SERVER = socket.gethostbyname(socket.gethostname())
    PORT = 2345
    SERVER_ADDR = (SERVER, PORT)
    BUFFER = 1024
    server = socket.socket(socket.AF_INET, socket.SOCK.DGRAM)
