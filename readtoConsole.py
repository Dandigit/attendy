#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
sys.path.append('libraries/SimpleMFRC522.py')
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
        id, text = reader.read()
        print("Card ID: ", id)
        print("Data: ", text)
finally:
        GPIO.cleanup()
