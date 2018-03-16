#!/usr/bin/env python

import RPi.GPIO as GPIO
import os
import sys
sys.path.append('libraries/SimpleMFRC522.py')
import SimpleMFRC522
import datetime
import logging
from sheetsync import Sheet, ia_credentials_helper

# Defining the RC522 reader
reader = SimpleMFRC522.SimpleMFRC522() 

# Right now we're logging - so much could go wrong.
logging.getLogger('sheetsync').setLevel(logging.DEBUG)
logging.basicConfig()

# Enter your OAUTH2 credentials here:
CLIENT_ID = 'Enter client ID here'
CLIENT_SECRET = 'Enter client secret here'
creds = ia_credentials_helper(CLIENT_ID, CLIENT_SECRET,
                              credentials_cache_file='cred_cache.json')
readerOn = true

try:
    while readerOn == true:
        id, text = reader.read()
        os.system('mpg123 -q success.mp3 &')
        currentTime = '{:%H:%M:%S}'.format(datetime.datetime.now())
        currentDate = '{:%d:%m:%Y}'.format(datetime.datetime.now())
        cardId = id
        name = text
        
        data = { name: {"Time" : currentTime, "Date" : currentDate}}

        # Find or create a spreadsheet, then inject data.
        target = Sheet(credentials=creds, document_name="Attendy")
        target.inject(data)
        print "Written to spreadsheet: %s" % target.document_href
        print "Ready"
finally:
    GPIO.cleanup()
  
