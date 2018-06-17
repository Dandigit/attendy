#!/usr/bin/env python

import RPi.GPIO as GPIO
import os
import sys
sys.path.append('libraries/')
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
    id, text = reader.read()
    print("Card ID: ", id)
    print("Data: ", text)
    os.system('mpg123 -q success.mp3 &')
finally:
    GPIO.cleanup()
