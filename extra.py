#from datetime import datetime
#from influxdb import InfluxDBClient
#t1 = datetime.now()
#print(t1)

import time

print(time.time())
print(time.time() + 420)
print(int((time.time() + 300)*10**3))

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
from collections import deque

class queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data_recv):
        self.queue.appendleft(data_recv)
    
    def dequeue(self):
        return self.queue.pop()
    
    def size(self):
        return len(self.queue)
    
    def show_queue(self):
        print(self.queue)

set1 = ["sender2",1,2,3,4]
set2 = ["sender1",3,4,5,6]
#sender = "pdc"
import time
data_queue = queue()
t1 = time.perf_counter_ns()
data_queue.enqueue(set1)
t2 = time.perf_counter_ns()
print("enqueue time is {}", format(t2-t1))
data_queue.enqueue(set2)
#print(data_queue.size())
data_queue.show_queue()
set3 = data_queue.dequeue()
print(set3)
set3 = data_queue.dequeue()
print(set3)




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