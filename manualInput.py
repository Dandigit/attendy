#!/usr/bin/env python

import RPi.GPIO as GPIO
import datetime
import os
import logging
from sheetsync import Sheet, ia_credentials_helper

# Normally logging would be turned on, but we don't want to confuse the user

# Enter your OAUTH2 credentials here:
CLIENT_ID = '946386881583-q0jl6r8280p56o0ma4qph2157tmp1hs2.apps.googleusercontent.com'
CLIENT_SECRET = 'rhniAHN0Rz_cs_AGB81TrkWX'
creds = ia_credentials_helper(CLIENT_ID, CLIENT_SECRET,
                              credentials_cache_file='cred_cache.json')


text = raw_input('Enter full name of student: ')
currentTime = '{:%H:%M:%S}'.format(datetime.datetime.now())
currentDate = '{:%dT:%m:%Y}'.format(datetime.datetime.now())
name = text
        
data = { name: {"Time" : currentTime, "Date" : currentDate}}

# Find or create a spreadsheet, then inject data.
target = Sheet(credentials=creds, document_name="Attendy")
target.inject(data)
print "Written to spreadsheet: %s" % target.document_href
os.system('success.mp3')
