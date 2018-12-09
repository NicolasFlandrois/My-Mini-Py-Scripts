#! ~/bin/python3

#Automaticaly run bash from Python script
#Author Nicolas Flandrois - Sun 09 Dec 2018 04:26:44 PM CET 

#Add or remove bash command lines you actally need, and sleep lap time

#Run this program preceeding by "bg" command line, in bash/Linux terminal. To show what job is in Background run "bg job". to stop background jobs "bg stop".

import os
import time

print ("hello world")

NAME = input("GitHub user name : ")
PWD = input("Passphrase : ")

os.system("clear")

while True:
	for i in range(4):
		os.system ("git commit -a -m 'Auto Commit'")
		time.sleep(3)
		#time express in seconds (20min = 1200sec)
		#For testing this time.sleep is set to 3sec

	print("Now your commits will be push to GitHub")
	os.system("git push origin master")
	time.sleep(10)
	print("Your files, and commits has been uploaded and saved to your GitHub")
