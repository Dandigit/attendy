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
  id, text = reader.read()
  currentTime = '{:%H:%M:%S}'.format(datetime.datetime.now())
  currentDate = '{:%dT:%m:%Y}'.format(datetime.datetime.now())
  c = "This would be the card ID, but this is just a test."
  d = "This would be the student's name, but this is just a test."
  values = {'values':[[currentTime, currentDate, c, d],]}
  rangeName = 'A'+ str(i) + ':D'
  sheetupdate.update_authenticate(spreadsheetId, rangeName, values)
finally:
  print("Right now the GPIO would be cleaned, but that's not an issue at the moment as this is just a test.")
  
if __name__ == '__main__':
testsheet()
