#!/usr/bin/env python

import pyrebase
import datetime
from time import sleep

# Enter your Firebase credentials in here
config = {
  "apiKey": "AIzaSyAXRs79-GGaalWFFT27uvBeX73rPGw2Dv8",
  "authDomain": "attendy-backend.firebaseapp.com",
  "databaseURL": "https://attendy-backend.firebaseio.com",
  "storageBucket": "attendy-backend.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
db.child("users").child("Morty")
data = {"name": "Mortimer 'Morty' Smith"}
db.child("users").push(data)
