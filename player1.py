'''-----------------------------------------------------------

	Author: 	Jordan  Fluth
	Date:		May 5, 2014

	Description: This is a spin on the classic hangman game.
	
	Rules:
		1)
		2)

-----------------------------------------------------------'''

import socket
import sys
from array import *


HOST, PORT = "localhost", 9999

total_Wrong = 0
total_Right = 0
current_Puzzle = array('c', [])

# Create a socket (SOCK_STREAM means a TCP socket)
print("connecting...")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

	sock.connect((HOST, PORT))
	print("connection established...\n")


	Word = sock.recv(4096)
	total_Length = len(Word) - 1
	current_Puzzle.fromstring('_' * total_Length)
	wordMask = ' '.join(current_Puzzle)
	print wordMask
	
	while (total_Right < total_Length):
		data = raw_input("Enter a guess: ")
		sock.sendall(data + "\n")
	

		# Receive data from the server and shut down
		received = sock.recv(1024)
		received = int(received)
	
	
		if (received < 0):
			print("you guessed incorrectly...\n")
			total_Wrong += 1
		
		else:
			print "you guessed correct...\n"
			index = 0
			while index < len(Word):
				index = Word.find(data, index)
				if index == -1:
					break
				current_Puzzle[index] = data
				index += 1
			total_Right += received 
			
			
		wordMask = ' '.join(current_Puzzle)
		print wordMask
		
		
except (OverflowError, IOError):
	print("Error Message")	
			
finally:
    sock.close()

print "Sent:     {}".format(data)
print "Received: {}".format(received)
