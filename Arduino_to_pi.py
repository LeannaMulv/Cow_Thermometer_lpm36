#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)
while 1: 
    if(ser.in_waiting >10):
        line = ser.readline()
        print(line)

