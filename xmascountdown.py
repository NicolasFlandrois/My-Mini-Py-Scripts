#! usr/bin/python3

# Thu 20 Dec 2018 03:04:22 PM CET 
# Author: Nicolas Flandrois
# Description: Christmas countdown, according to a choosen year.
# NB: This script is not UTC/Timezone aware. Time is set as naive, using your local (computer) timezone as default.

import time
import datetime
import os
import platform
import sys

def clean():
	if platform.system() == "Windows":
		os.system("cls")
	elif platform.system() == "Linux":
		os.system("clear")

try:
    Year = int(input("Xmas of which year? "))
except:
    print("Oops! ",sys.exc_info()[0],""" occured. That was no valid number.  Try again...
choose a year, in number, format YYYY.""")

xd = datetime.datetime(Year, 12, 25, 0, 0, 1)

clean()

while True:
    td = datetime.datetime.now()
    delta = xd - td
    print(delta.strftime('%Y years, %m months, %d days, %H:%M:%S'))
    time.sleep(1)
    clean()
print()

#Failed tests:
#I want the countdown to appear as: YYYY years MM months DD days HH:MM:SS; and remove at least the microseconds.
# print(delta.strftime('%Y years, %m months, %d days, %H:%M:%S'))  Doesn't work out
