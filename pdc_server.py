###################### PDC Server Building ###########################
# features to be added here
# Step 1: Receive sequence voltage data from various PMUs in cartesian
#         coordinate system
# Step 2: Store the data in arrays named after each bus depending upon
#         PMU id, this array will be used for calculation
# Step 3: Create a log file that will create a CSV notepad file for each
#         bus. This can be used for making trends for various voltages
# Step 4: Obtain phase voltages from sequence voltages for each bus from
#         Step 2 data
# Step 5: Estimate incoming current to the faulted line using long TL
#         model and bus voltages
# Step 6: Using incoming current and bus voltages, calculate the fault 
#         distance for all the fault types
# Step 7: Send the decision back to PMU

import time
import socket
import struct
import multiprocessing
from util import pdc

PDC_server = pdc()
#PDC_server.current_time()
PDC_server.start_server()