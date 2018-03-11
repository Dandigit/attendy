import os
import logging
from sheetsync import Sheet, ia_credentials_helper
# Turn on logging so you can see what sheetsync is doing.
logging.getLogger('sheetsync').setLevel(logging.DEBUG)
logging.basicConfig()

# Create OAuth2 credentials, or reload them from a local cache file.
CLIENT_ID = 'Enter client ID here'
CLIENT_SECRET = 'Enter client secret here'
creds = ia_credentials_helper(CLIENT_ID, CLIENT_SECRET,
                              credentials_cache_file='cred_cache.json')

data = { "Row 1": {"Test" : "Succeeded", "Test" : "Succeeded"},
         "Row 2" : {"Test" : "Succeeded", "Test" : "Succeeded"} }

# Find or create a spreadsheet, then inject data.
target = Sheet(credentials=creds, document_name="Attendy Sync Test")
target.inject(data)
print "Spreadsheet created/appended here: %s" % target.document_href
os.system('mpg123 -q success.mp3 &')
