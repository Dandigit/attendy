#!/usr/bin/env python

import RPi.GPIO as GPIO
import os
import sys
sys.path.append('libraries/')
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
    text = raw_input('Enter data to write: ')
    print("Please place your tag on the reader")
    reader.write(text)
    print("Write successful!")
    os.system('mpg123 -q success.mp3 &')
finally:
    GPIO.cleanup()
