

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
import os
import time
from array import *

# constants
game_state = (
"""
	 ------
	 |    |
	 |
	 |
	 |
	 |
	 |
	 |
	 |
	----------
""",
"""
	 ------
	 |    |
	 |    O
	 |
	 |
	 |
	 |
	 |
	 |
	----------
""",
"""
	 ------
	 |    |
	 |    O
	 |   -+-
	 | 
	 |   
	 |   
	 |   
	 |   
	----------
""",
"""
	 ------
	 |    |
	 |    O
	 |  /-+-
	 |   
	 |   
	 |   
	 |   
	 |   
	----------
""",
"""
	 ------
	 |    |
	 |    O
	 |  /-+-/
	 |   
	 |   
	 |   
	 |   
	 |   
	----------
""",
"""
	 ------
	 |    |
	 |    O
	 |  /-+-/
	 |    |
	 |   
	 |   
	 |   
	 |   
	----------
""",
"""
	 ------
	 |    |
	 |    O
	 |  /-+-/
	 |    |
	 |    |
	 |   | 
	 |   | 
	 |   
	----------
""",
"""
	 ------
	 |    |
	 |    O
	 |  /-+-/
	 |    |
	 |    |
	 |   | |
	 |   | |
	 |  
	----------
""")

# This class contains all the functions required for the hangman game
class hangman():
	def connect(self):
		# Create a socket and establish a connection
		self.HOST, self.PORT = "localhost", 9999
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("connecting...")
		
		self.sock.connect((self.HOST, self.PORT))
		print("connection established...\n")

	def game_setup(self):
		self.total_Wrong = 0
		self.total_Right = 0
		self.guessed = array('c', [])
		self.current_Puzzle = array('c', [])
		
		self.Word = self.sock.recv(4096)
		self.total_Length = len(self.Word) - 1
		self.current_Puzzle.fromstring('_' * self.total_Length)
		self.wordMask = ' '.join(self.current_Puzzle)
		
		self.game_display()

	def game_display(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		print "\n" + game_state[self.total_Wrong]
		print "\n" + "\t" + self.wordMask
		print ("\nYou guessed correct:\t\t{} times".format(self.total_Right))
		print("You guessed incorrectly:\t{} times\n".format(self.total_Wrong))
		#print("\nGame status:\t\t{}\n".format(self.gstatus))	

	def send_guess(self):
		self.data = raw_input("Enter a guess: ")
		
		while self.guessed.count(self.data) != 0:
			print "\nYou have already guessed this: try again"
			self.data = raw_input("Enter a guess: ")
		
		self.guessed.append(self.data)
		self.sock.sendall(self.data + "\n")

	def get_result(self):
		self.received = self.sock.recv(4096)
		self.received = int(self.received)
		
	def update_game_state(self):
		if (self.received < 0):
			self.total_Wrong += 1
			
			if self.total_Wrong >= 7:
				print "\nYou've been hung!\n"
				self.sock.close()
		
		else:
			index = 0
			
			while index < len(self.Word):
				index = self.Word.find(self.data, index)
				if index == -1:
					break
				self.current_Puzzle[index] = self.data
				index += 1
			
			self.total_Right += self.received			
		
		self.wordMask = ' '.join(self.current_Puzzle)
		self.game_display()
		
		
	
	def is_done(self):
		if self.total_Right == (len(self.Word) - 1):
			self.sock.sendall("y")
			
		elif self.total_Wrong >= 7:
			self.sock.sendall("h")
			
		else:
			self.sock.sendall("n")
		
		self.check = self.sock.recv(4096)	
		
		if self.check == 'W':
			os.system('cls' if os.name == 'nt' else 'clear')
			print "You are the Winner!"
			time.sleep(3)
			self.sock.close()
		
		elif self.check == 'H':
			os.system('cls' if os.name == 'nt' else 'clear')
			print "You've been hanged! - You Lose -"
			time.sleep(3)
			self.sock.close()
		
		elif self.check == 'L':
			os.system('cls' if os.name == 'nt' else 'clear')
			print "You are the Loser!"
			time.sleep(3)
			self.sock.close()
		
		elif self.check == 'C':
			self.check = self.check
			
		

if __name__ == "__main__":
	game = hangman()

	try:
		game.connect()
		game.game_setup()
	
		while (game.total_Right < game.total_Length):
			game.send_guess()
			game.get_result()
			game.update_game_state()
			game.is_done()	
		
		
	except (OverflowError, IOError):
		print("Error Message")	
			
	finally:
		 game.sock.close()



