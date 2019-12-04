# cite: https://classes.engineering.wustl.edu/ese205/core/index.php?title=Serial_Communication_between_Raspberry_Pi_%26_Arduino

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)
while 1: 
    if(ser.in_waiting >100):
        line = ser.readline()
        print(line)

