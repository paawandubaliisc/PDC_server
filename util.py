import socket
import time
import struct


class pdc:
    SERVER = "10.64.37.35"
    PORT = 2345
    SERVER_ADDR = (SERVER, PORT)
    BUFFER = 1024
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def start_server(self):
        #print(self.SERVER_ADDR)
        self.server.bind(self.SERVER_ADDR)
        print("[SERVER STARTING] at " + str(self.SERVER))
        while True:
            msg, cl_addr = self.server.recvfrom(self.BUFFER)
            data_recv = self.msg_unpack(msg)
            
        return(msg,cl_addr)
    
    def current_time(self):
        CT = time.time()
        SOC_SERVER = int(CT)
        FRACSEC_SERVER = (CT - SOC_SERVER)*10**6
        '''
        print("Time is " + str(CT))
        print("SOC Server in seconds is " + str(SOC_SERVER) + 
              "\nFRACSEC in useconds is " + str(FRACSEC_SERVER))
        '''
        return SOC_SERVER, FRACSEC_SERVER

    def msg_unpack(self,msg):
        data_recv = struct.unpack('!HHHIIIHIHHHHIIIHH',msg)
        return data_recv
        #12345678
        '''
        print("SYNC is " + str(data_recv[0]))
        print("FRAME size is " + str(data_recv[1]))
        print("PMU ID is " + str(data_recv[2]))
        print("SOC_CLIENT is " + str(data_recv[3]))
        print("FRACSEC_CLIENT is " + str(data_recv[4]))
        '''


