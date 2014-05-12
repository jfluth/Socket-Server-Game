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
import subprocess
from array import *


# This class contains all the functions required for the
# hangman game
class hangman():
	
	

	def connect(self):
		# Create a socket and establish a connection
		print("connecting...")
		self.HOST, self.PORT = "localhost", 9999
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.HOST, self.PORT))
		print("connection established...\n")


	def game_setup(self):
		self.Word = self.sock.recv(4096)
		self.total_Wrong = 0
		self.total_Right = 0
		self.guessed = array('c', [])
		self.current_Puzzle = array('c', [])
		self.total_Length = len(self.Word) - 1
		self.current_Puzzle.fromstring('_' * self.total_Length)
		self.wordMask = ' '.join(self.current_Puzzle)
		print self.wordMask	


	def send_guess(self):
		self.data = raw_input("Enter a guess: ")
		if self.guessed.count(self.data) == 0:
			self.guessed.append(self.data)
			self.sock.sendall(self.data + "\n")
		else:
			print "you have already guessed this: try again\n"
			send_guess()


	def get_result(self):
		self.received = self.sock.recv(1024)
		self.received = int(self.received)
		
		
	def update_game_state(self):
		if (self.received < 0):
			self.total_Wrong += 1
			print("you guessed incorrectly:\t{} times\n".format(self.total_Wrong))
			if self.total_Wrong == 3:
				print "You guessed wrong too many times...\n\nYou Lose!\n\n"
				game.sock.close()
		
		else:
			print ("you guessed correct!\nyour score is:\t{}".format(self.total_Right))
			index = 0
			while index < len(self.Word):
				index = self.Word.find(self.data, index)
				if index == -1:
					break
				self.current_Puzzle[index] = self.data
				index += 1
			self.total_Right += self.received 
			
			
		self.wordMask = ' '.join(self.current_Puzzle)
		print self.wordMask
	

if __name__ == "__main__":
	
	game = hangman()
	
	try:
		game.connect()
		game.game_setup()
	
		while (game.total_Right < game.total_Length):
			game.send_guess()
			game.get_result()
			game.update_game_state()	
		
		
	except (OverflowError, IOError):
		print("Error Message")	
			
	finally:
		 game.sock.close()

#print "Sent:     {}".format(data)
#print "Received: {}".format(received)


