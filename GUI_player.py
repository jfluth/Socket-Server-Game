

import socket
import sys
import subprocess
from array import *
from Tkinter import *





if __name__ == "__main__":

	game = hangman()
	
	try:
		game.connect()
		game.game_setup()
		data = ''
		game.game_setup()
		'''while (game.total_Right < game.total_Length):
			game.send_guess()
			game.get_result()
			game.update_game_state()'''
		'''---------------------- GUI Setup ---------------------------------'''
		master = Tk() 
		Label(master, text="Welcome to Hangman!\n\n").grid(row=1, sticky=W)
		Puzzle = Message(master, textvariable=game.wordMask)
		Puzzle.grid(row=3, column=2)
		Label(master, text="Enter Guess:", textvariable=data).grid(row=5, sticky=W)
		guess = Entry(master)
		guess.grid(row=5, column=1) 
		guess_button = Button(master, text="Guess")
		game.sock.sendall(data + "\n")
		guess_button.grid(row=5, column=2)  
		mainloop()	
		
		
	except (OverflowError, IOError):
		print("Error Message")	
			
	finally:
		 game.sock.close()
