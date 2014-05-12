from socket import *
from Tkinter import *
import thread
import math
import linecache
import random

BUFF = 1024
HOST = "localhost"
PORT = 9999 

global Puzzle
global server
global end_game_msg


class threaded_Serv():
	
	def __init__(self):
		self.total_length = len(Puzzle) - 1
		self.player_score = 0
		print Puzzle
		
				
	def match(self, data):
		index = 0
		matches = 0
		while index < len(Puzzle):
			index = Puzzle.find(data, index)
			if index == -1:
				break
			index += 1
			if (index >= 0):
				matches += 1
				self.player_score += 1
		if matches == 0:
			return -1
		if self.player_score == self.total_length:
			end_game_msg = True
		print "Player Score is: {}".format(self.player_score)
		return matches
		

def response(key):
	return 'Server response: ' + key


def handler(clientsock,addr):
	server = threaded_Serv()
	clientsock.sendall(Puzzle)
    
	while 1:
		data = clientsock.recv(1024).strip()
		if not data: break
		print data
		Index = server.match(data)
		clientsock.sendall(str(Index) + "\n")

			
	clientsock.close()
	print addr, "- closed connection" 


def is_winner():
	if end_game_msg:
		print "Winner"
		

if __name__=='__main__':
	'''---------------------- Generate Puzzle --------------------------'''
	generate = random.randint(1, 126)
	Puzzle = linecache.getline('WordList.txt', generate)
	end_game_msg = False
	print Puzzle
	

	'''---------------------- Socket Setup ------------------------------'''	
	ADDR = (HOST, PORT)
	serversock = socket(AF_INET, SOCK_STREAM)
	serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	serversock.bind(ADDR)
	serversock.listen(5)
	
	'''---------------------- Establish Connections ---------------------'''
	while 1:
		print 'waiting for connection... listening on port', PORT
		clientsock, addr = serversock.accept()
		print '...connected from:', addr
		thread.start_new_thread(handler, (clientsock, addr))
		
		
