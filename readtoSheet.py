#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import sheetupdate
import datetime
from random import randint
from time import sleep

reader = SimpleMFRC522.SimpleMFRC522()

def testsheet():
        spreadsheetId = '1HxIF-7LGQI-OtNyNIYU9ao0CKPfzFW6eGyurC6qvmBI'
        rangeName = 'A1:D'
        values = {'values':[['Time','Date','Name','ID'],]}
  
        sheetupdate.update_authenticate(spreadsheetId, rangeName, values)
  
try:
        id, text = reader.read()
        currentTime = '{:%H:%M:%S}'.format(datetime.datetime.now())
        currentDate = '{:%dT:%m:%Y}'.format(datetime.datetime.now())
        c = id
        d = text
        values = {'values':[[currentTime, currentDate, c, d],]}
        rangeName = 'A'+ str(i) + ':D'
        sheetupdate.update_authenticate(spreadsheetId, rangeName, values)
finally:
        GPIO.cleanup()
  
if __name__ == '__main__':
        testsheet()
  
