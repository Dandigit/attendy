#!/usr/bin/env python

import sheetupdate
import datetime
from random import randint
from time import sleep

def testsheet():
    spreadsheetId = '1HxIF-7LGQI-OtNyNIYU9ao0CKPfzFW6eGyurC6qvmBI'
    rangeName = 'A1:D'
    values = {'values':[['Time','Date','Name','ID'],]}
  
    sheetupdate.update_authenticate(spreadsheetId, rangeName, values)
  
try:
    while True:
        for i in range(2):
            currentTime = '{:%H:%M:%S}'.format(datetime.datetime.now())
            currentDate = '{:%dT:%m:%Y}'.format(datetime.datetime.now())
            c = "This would be the card ID, but this is just a test."
            d = "This would be the student's name, but this is just a test."
            values = {'values':[[currentTime, currentDate, c, d],]}
            rangeName = 'A'+ str(i) +':D'
            sheetupdate.update_authenticate(spreadsheetId, rangeName, values)
            print("Success!")

if __name__ == '__main__':
    testsheet()
