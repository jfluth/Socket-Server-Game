from socket import *
import thread
import math
import linecache
import random

BUFF = 1024
HOST = "localhost"
PORT = 9999 

global Puzzle

class threaded_Serv():
	
	def __init__(self):
		self.total_Length = len(Puzzle) - 1
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
		print self.player_score
		return matches
		
		
	def isWinner(self):
		if (self.numRight == self.score):
			return 1
		else:
			return 0


def response(key):
	return 'Server response: ' + key


def handler(clientsock,addr):
	server = threaded_Serv()
	clientsock.sendall(Puzzle)
    
	while 1:
		data = clientsock.recv(1024).strip()
		if not data: break
		Index = server.match(data)
		if (Index < 0):
			clientsock.sendall(str(Index) + "\n")
		else :
			clientsock.sendall(str(Index) + "\n")
			
	clientsock.close()
	print addr, "- closed connection" 


if __name__=='__main__':
	generate = random.randint(1, 126)
	Puzzle = linecache.getline('WordList.txt', generate)
	print Puzzle
	
	ADDR = (HOST, PORT)
	serversock = socket(AF_INET, SOCK_STREAM)
	serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	serversock.bind(ADDR)
	serversock.listen(5)
	
	
	while 1:
		print 'waiting for connection... listening on port', PORT
		clientsock, addr = serversock.accept()
		print '...connected from:', addr
		thread.start_new_thread(handler, (clientsock, addr))
		
		
