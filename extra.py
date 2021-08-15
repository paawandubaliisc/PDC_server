#from datetime import datetime
from influxdb import InfluxDBClient
#t1 = datetime.now()
#print(t1)

import time
'''
print(time.time())
print(int((time.time())*10**3))
'''

CT = time.time()
SOC_CLIENT = int(CT)
FRACSEC_CLIENT = int((CT - SOC_CLIENT)*10**6)
print(CT)
print(SOC_CLIENT)
print(FRACSEC_CLIENT)
print(int(CT*10**3))
print((SOC_CLIENT + FRACSEC_CLIENT*10**-6)*10**3)
print(int((SOC_CLIENT + FRACSEC_CLIENT*10**-6)*10**3))



'''
timeprecision = 's'
t2 = str(datetime.now())
print(t2.split( ))
t3 = t2.split( )
print(t3[1])


func_dict = {'pmu1' : "a",
                  'pmu2' : "b",
                  'pmu3' : "c",
                  'pmu4' : "d",
                  'pmu5' : "e",
                  'pmu6' : "f",
                  'pmu7' : "g",
                  'pmu8' : "h"}

print(func_dict.get('pmu8'))
'''