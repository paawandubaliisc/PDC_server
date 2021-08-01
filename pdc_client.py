import socket
import time
import struct

SERVER = "10.64.37.35"
PORT = 2345
SERVER_ADDR = (SERVER, PORT)
BUFFER = 1024
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


###################### Config Frame
SYNC_CONFIG = 0xAA21
FRAME_SIZE = 48
ID_CODE = 1
TIME_BASE = 10**6
NUM_PMU = 0x1
ST_NAME = 0xABCD

FORMAT = 0x0007
PHNMR = 0x0006
vol_phas = 3
curr_phas = 3
ANNMR = 0x0002
DGNMR = 0x0000
CHNAM = 0xABCDABCD

PHUNIT = 0x10001000
ANUNIT = 0x02000032
DIGUNIT = 0x0
FNOM = 0x0001


########################### Data Frame
SYNC_DATA = 0xAA00
STAT = 0xABCD
VA = 0xDCBADCBADCBADCBA
VB = 0xDCBADCBADCBADCBA
VC = 0xDCBADCBADCBADCBA
IA = 0xDCBADCBADCBADCBA
IB = 0xDCBADCBADCBADCBA
IC = 0xDCBADCBADCBADCBA
FREQ = 0xABCD
DFREQ = 0xDCBA
ANALOG1 = 0xDCBADCBA
ANALOG2 = 0xDCBADCBA
ANALOG3 = 0xDCBADCBA
ANALOG4 = 0xDCBADCBA
DIGITAL = 0xABCD


def current_time():
        CT = time.time()
        SOC_SERVER = int(CT)
        FRACSEC_SERVER = int((CT - SOC_SERVER)*10**6)
        #print("Time is " + str(CT))
        #print("SOC Server in seconds is " + str(SOC_SERVER) + 
               #"\nFRACSEC in useconds is " + str(FRACSEC_SERVER))
        return SOC_SERVER, FRACSEC_SERVER

i = 20
while i > 0:
    SOC_CLIENT = current_time()[0]
    FRACSEC_CLIENT = current_time()[1]
    msg = struct.pack('!HHHIIIHIHHHHIIIHH', 
                        SYNC_CONFIG, 
                        FRAME_SIZE, 
                        ID_CODE ,
                        SOC_CLIENT,
                        FRACSEC_CLIENT , 
                        TIME_BASE,
                        NUM_PMU, 
                        ST_NAME, 
                        FORMAT, 
                        PHNMR, 
                        ANNMR, 
                        DGNMR, 
                        CHNAM, 
                        PHUNIT, 
                        ANUNIT, 
                        DIGUNIT, 
                        FNOM)
    client.sendto(msg, SERVER_ADDR)
    print("SYNC is " + str(SYNC))
    print("FRAME size is " + str(FRAME_SIZE))
    print("PMU ID is " + str(ID_CODE))
    print("SOC_CLIENT is " + str(SOC_CLIENT))
    print("FRACSEC_CLIENT is " + str(FRACSEC_CLIENT))
    i = i - 1

