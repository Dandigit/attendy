#!/bin/bash

# This is the Attendy Bash installer.
# It will install Attendy and its dependencies.

cd ~

echo "Installing Attendy..."

tput sc
echo "[       ]"

sudo apt-get install python2.7-dev > /dev/null 2>&1

tput rc
tput ed
echo "[\u0965      ]"

git clone https://github.com/lthiery/SPI-Py.git > /dev/null 2>&1

tput rc
tput ed
echo "[\u0965\u0965     ]"

cd ~/SPI-Py
sudo python setup.py install > /dev/null 2>&1

tput rc
tput ed
echo "[\u0965\u0965\u0965    ]"

cd ~
sudo rm -rf SPI-Py

pip install sheetsync > /dev/null 2>&1

tput rc
tput ed
echo "[\u0965\u0965\u0965\u0965   ]"

sudo pip install sheetsync > /dev/null 2>&1

tput rc
tput ed
echo "[\u0965\u0965\u0965\u0965\u0965  ]"

sudo pip uninstall gspread > /dev/null 2>&1

tput rc
tput ed
echo "[\u0965\u0965\u0965\u0965\u0965\u0965 ]"

sudo pip install --upgrade gspread==0.6.2 > /dev/null 2>&1

tput rc
tput ed
echo "[\u0965\u0965\u0965\u0965\u0965\u0965\u0965]"

echo ""
echo "------------------------- URGENT -------------------------"
echo "Attendy and its dependencies have been configured, however"
echo "you will need to proceed with Google Sheets API setup at"
echo "http://attendy.dandigit.com/setup/api. Thanks for installing!"
