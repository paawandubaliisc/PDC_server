import logging
#from pdc_client import current_time
import socket
import struct
import time
from influxdb import InfluxDBClient
from collections import deque


################## Queue class
class queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data_recv):
        self.queue.appendleft(data_recv)
    
    def dequeue(self):
        return self.queue.pop()
    
    def size(self):
        return len(self.queue)
    
    def show(self):
        print(self.queue)

    def empty_check(self):
        return True if len(self.queue) == 0 else False


################## Logger Class
class log:
    def __init__(self,
                 logger_name,
                 logger_level):
        self.logger_name = logger_name
        self.logger_level = logger_level
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(logging.INFO)
        self.file_handler = logging.FileHandler('{}.log'.format(self.logger_name))
        self.file_handler.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        self.logger.addHandler(self.file_handler)
        self.file_handler.setFormatter(self.formatter)
        self.logger.info('{} log STARTED'.format(self.logger_name))

            
    def log_data_gen(self, sender, MILSEC_SERVER, data_recv):
        self.logger.info("Sender is {}".format(sender))
        self.logger.info("Time is {}".format(MILSEC_SERVER))
        '''
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
        '''
        self.logger.info("Message Complete")
    
    def log_data(self, msg):
        self.logger.info(msg)


#################### Influx db inclusion

class db:
    def __init__(self, 
                 host = 'localhost',
                 port = 8086,
                 dbname = 'PMU'):
                 
        self.json_counter = 0
        self.write_counter = 0
        ############ logger for InfluxDB
        self.db_log = log(logger_name = "db_log", logger_level = "INFO")
        ############# db client starting
        self.host = host
        self.port = port
        self.dbname = dbname
        self.client = InfluxDBClient(host, port, dbname)
        self.db_log.log_data('client created with {},{},{}'.format(host, port, dbname))
        self.create_dbs()
        self.get_db_list()

    def create_dbs(self):
        self.client.create_database('{}1'.format(self.dbname))
        self.db_log.log_data('new db with name {}1 created'.format(self.dbname))
        ###
        self.client.create_database('{}2'.format(self.dbname))
        self.db_log.log_data('new db with name {}2 created'.format(self.dbname))
        ###
        self.client.create_database('{}3'.format(self.dbname))
        self.db_log.log_data('new db with name {}3 created'.format(self.dbname))
        ###
        self.client.create_database('{}4'.format(self.dbname))
        self.db_log.log_data('new db with name {}4 created'.format(self.dbname))
        ###
        self.client.create_database('{}5'.format(self.dbname))
        self.db_log.log_data('new db with name {}5 created'.format(self.dbname))
        ###
        self.client.create_database('{}6'.format(self.dbname))
        self.db_log.log_data('new db with name {}6 created'.format(self.dbname))
        ###
        self.client.create_database('{}7'.format(self.dbname))
        self.db_log.log_data('new db with name {}7 created'.format(self.dbname))
        ###
        self.client.create_database('pdc')
        self.db_log.log_data('new db with name pdc created')
        ###

    def get_db_list(self):
        self.db_log.log_data('db list is {}'.format(self.client.get_list_database()))
        #return self.client.get_list_database()
    
    def switch_to_db(self,dbname):
        self.client.switch_database(dbname)
        self.db_log.log_data('db switching to {}'.format(dbname))
    
    def get_json(self,
                 sender, 
                 data_array,
                 MILSEC_SERVER):
        MILSEC_CLIENT = int((data_array[3] + data_array[4]*10**-6)*10**3)
        time1 = time.perf_counter_ns()
        json = [
                    {
                        "measurement" : "voltage",
                        "tags" : {
                        },
                        "fields": { 
                                    "time_server" : MILSEC_SERVER,
                                    "time_client" : MILSEC_CLIENT,
                                    "V11_mag" : data_array[6],
                                    "V11_ph"  : data_array[7],
                                    "V12_mag" : data_array[8],
                                }
                    } 
                ]
        time2 = time.perf_counter_ns()
        print('json time is {}'.format(time2 - time1))
        self.json_counter = self.json_counter + 1
        print("json counter is {}".format(self.json_counter))
        return json
    
    def write_to_db(self,json):
        time1 = time.perf_counter_ns()
        result = self.client.write_points(json, time_precision = 'ms')
        time2 = time.perf_counter_ns()
        self.db_log.log_data('Write successful: {}'.format(result))
        self.write_counter += 1
        print("write counter is {}".format(self.write_counter))
        print('write time is {}'.format(time2 - time1))


##################### Server Class 
class server:
    def __init__(self,
                 SERVER,
                 PORT):
        self.SERVER = SERVER
        self.PORT = PORT
        self.dict = {'10.64.37.31' : 'ss8',
                     '10.64.37.32' : 'ss26',
                     '10.64.37.33' : 'ss17',
                     '10.64.37.34' : 'ss30',
                     '10.64.37.35' : 'pdc',
                     '10.64.37.36' : 'ss38',
                     '10.64.37.37' : 'ss37',
                     '10.64.37.38' : 'ss65'}

        self.func_dict = {'pmu1' : "pmu1_func",
                          'pmu2' : "pmu2_func",
                          'pmu3' : "pmu3_func",
                          'pmu4' : "pmu4_func",
                          'pmu5' : "pmu5_func",
                          'pmu6' : "pmu6_func",
                          'pmu7' : "pmu7_func",
                          'pdc'  : "pdc_func"}
        self.SERVER_ADDR = (self.SERVER, self.PORT)
        self.BUFFER = 1024
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.gen_log = log(logger_name = "gen_log", logger_level = "INFO")
        #self.client = db("localhost", 8086, "pmu")
        self.db_queue = queue()
        self.log_queue = queue()
        self.pmu_queue = queue()

    #SERVER = "10.64.37.35"
    #PORT = 2345
    
    def start_server(self):
        self.server.bind(self.SERVER_ADDR)
        print("[SERVER STARTING] at " + str(self.SERVER))
        while True:
            msg, cl_addr = self.server.recvfrom(self.BUFFER)
            MILSEC_SERVER = self.current_time()[2]
            data_recv = self.msg_unpack(msg) 
            sender = self.dict[cl_addr[0]]
            queue_set = [sender, MILSEC_SERVER,data_recv]
            print("Data recv from {} at {}".format(sender, MILSEC_SERVER))
          
            ################################################
    
    def start_gen_logging(self):
        while True:
            if self.log_queue.empty_check() == False:
                queue_set = self.log_queue.dequeue()
                self.gen_log.log_data_gen(queue_set[0], queue_set[1], queue_set[2])
        
    
    def start_db_logging(self):
        while True:
            if self.db_queue.empty_check() == False:
                queue_set = self.db_queue.dequeue()
                sender = queue_set[0]
                MILSEC_SERVER = queue_set[1]
                data_recv = queue_set[2]
                self.client.switch_to_db(sender)
                json = self.client.get_json(sender, data_recv, MILSEC_SERVER)
                self.client.write_to_db(json)


            

            


            
            
    def pmu1_func(self, data_recv, MILSEC_SERVER):
        pass

    def pmu2_func(self, data_recv, MILSEC_SERVER):
        pass

    def pmu3_func(self, data_recv, MILSEC_SERVER):
        pass

    def pmu4_func(self, data_recv, MILSEC_SERVER):
        pass

    def pmu5_func(self, data_recv, MILSEC_SERVER):
        pass

    def pmu6_func(self, data_recv, MILSEC_SERVER):
        pass

    def pmu7_func(self, data_recv, MILSEC_SERVER):
        pass

    def pdc_func(self, data_recv, MILSEC_SERVER):
        pass

    def current_time(self):
        CT = time.time()
        SOC_SERVER = int(CT)
        FRACSEC_SERVER = (CT - SOC_SERVER)*10**6
        MILSEC_SERVER = int((time.time())*10**3)
        return SOC_SERVER, FRACSEC_SERVER, MILSEC_SERVER
        
    def msg_unpack(self,msg):
        data_recv = struct.unpack('!3H2IH12d6IH',msg)
        return data_recv
        



        








'''
print("Time is " + str(CT))
print("SOC Server in seconds is " + str(SOC_SERVER) + 
        "\nFRACSEC in useconds is " + str(FRACSEC_SERVER))
'''





'''
    print("SYNC is " + str(data_recv[0]))
    print("FRAME size is " + str(data_recv[1]))
    print("PMU ID is " + str(data_recv[2]))
    print("SOC_CLIENT is " + str(data_recv[3]))
    print("FRACSEC_CLIENT is " + str(data_recv[4]))
    '''
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

def log_data(self, data_recv, sender):
    self.logger.info("sender is {}".format(sender))
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
    '''    