'''

	This is the top level python script that starts the game
	
'''

import os
import time

response = raw_input("Start a new server? 'y' or 'n' ")

while response == 'y':
	os.system('cls' if os.name == 'nt' else 'clear')
	print "Starting Game Server...\n"
	time.sleep(1)
	os.system("gnome-terminal -e 'python threadedServ.py'")

	print "About to start a new game:\n"
	players = raw_input("how many players? ")
	time.sleep(1)

	for x in range (0, int(players)):
		os.system("gnome-terminal -e 'python player.py'")
		x += 1
	print "\n\n"
	response = raw_input("Start a new server? 'y' or 'n' ")
