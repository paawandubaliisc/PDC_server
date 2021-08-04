import logging
#from pdc_client import current_time
import socket
import struct
import time


##################### PDC Class 
class pdc:
    SERVER = "10.64.37.35"
    PORT = 2345
    SERVER_ADDR = (SERVER, PORT)
    BUFFER = 1024
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("[SERVER STARTING] at " + str(SERVER))

    def start_server(self):
        #print(self.SERVER_ADDR)
        self.create_log()
        self.server.bind(self.SERVER_ADDR)
        while True:
            msg, cl_addr = self.server.recvfrom(self.BUFFER)
            SOC_SERVER, FRACSEC_SERVER = self.current_time()
            data_recv = self.msg_unpack(msg)
            self.log_data(data_recv)           
            '''       
            print("\nSYNC is " + str(data_recv[0]))
            print("\nFRAME size is " + str(data_recv[1]))
            print("\nPMU ID is " + str(data_recv[2]))
            print("\nSOC_CLIENT is " + str(data_recv[3]))
            print("\nFRACSEC_CLIENT is " + str(data_recv[4]))
            '''
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
        data_recv = struct.unpack('!3H2IH12d6IH',msg)
        return data_recv
        '''
        print("SYNC is " + str(data_recv[0]))
        print("FRAME size is " + str(data_recv[1]))
        print("PMU ID is " + str(data_recv[2]))
        print("SOC_CLIENT is " + str(data_recv[3]))
        print("FRACSEC_CLIENT is " + str(data_recv[4]))
        '''
    
    def create_log(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.file_handler = logging.FileHandler('server.log')
        self.file_handler.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        self.logger.addHandler(self.file_handler)
        self.file_handler.setFormatter(self.formatter)
        self.logger.info('SERVER STARTED at {}'.format(self.SERVER)) 
        
    def log_data(self, data_recv):
        self.logger.info("E13_pos_mag: {},E13_pos_ph: {}"
                       .format(data_recv[6], data_recv[7]))
        self.logger.info("E13_neg_mag: {},E13_neg_ph: {}"
                       .format(data_recv[8], data_recv[9]))
        self.logger.info("E13_zero_mag: {},E13_zero_ph: {}"
                       .format(data_recv[10], data_recv[11]))
        self.logger.info("I13_pos_mag: {},I13_pos_ph: {}"
                       .format(data_recv[12], data_recv[13]))
        self.logger.info("I13_neg_mag: {},I13_neg_ph: {}"
                       .format(data_recv[14], data_recv[15]))
        self.logger.info("I13_zero_mag: {},I13_zero_ph: {}"
                       .format(data_recv[16], data_recv[17]))






