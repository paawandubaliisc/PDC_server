import socket
import time


class pdc:
    SERVER = "10.64.37.35"
    PORT = 2345
    SERVER_ADDR = (SERVER, PORT)
    BUFFER = 1024
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def start_server(self):
        print(self.SERVER_ADDR)
        self.server.bind(self.SERVER_ADDR)
        print("[SERVER STARTING]")
        msg, cl_addr = self.server.recvfrom(self.BUFFER)
        print(msg)
        return(msg,cl_addr)
    
    def current_time(self):
        CT = time.time()
        SOC_SERVER = int(CT)
        FRACSEC_SERVER = (CT - SOC_SERVER)*10**6
        print("Time is " + str(CT))
        print("SOC Server in seconds is " + str(SOC_SERVER) + 
              "\nFRACSEC in useconds is " + str(FRACSEC_SERVER))
        return SOC_SERVER, FRACSEC_SERVER
