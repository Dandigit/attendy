#!/usr/bin/env python

import pyrebase
import datetime
from time import sleep

# Enter your Firebase credentials in here
config = {
  "apiKey": "Enter Firebase apiKey here",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
db.child("users").child("Morty")
data = {"name": "Mortimer 'Morty' Smith"}
db.child("users").push(data)
