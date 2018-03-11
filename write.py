#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
sys.path.append('libraries/SimpleMFRC522.py')
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
        text = raw_input('Enter data to write: ')
        print("Please place your tag on the reader")
        reader.write(text)
        print("Write successful!")
finally:
        GPIO.cleanup()
