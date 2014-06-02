from socket import *
from array import *
import thread
import math
import time
import linecache
import random
import os

BUFF = 4096
HOST = "localhost"
PORT = 9999 

global Puzzle
global server
global end_game_msg
global gameover
global thread_count
thread_count = 0
development = 1
threads = []


class threaded_Serv():

	def __init__(self):
		self.total_length = len(Puzzle) - 1
		self.player_score = 0
		if development:
			print Puzzle
		
		
				
	def is_match(self, data):
		index = 0
		matches = 0
		
		while index < len(Puzzle):
			index = Puzzle.find(data, index)
			if index == -1:
  				break
			index += 1
			matches += 1
			self.player_score += 1
		
		if matches == 0:
			return -1
		
		os.system('cls' if os.name == 'nt' else 'clear')
		
		if development:
			print "Player Score is: {}".format(self.player_score)

		return matches
		
		

def response(key):
	return 'Server response: ' + key



def handler(clientsock,addr):

	global end_game_msg
	server = threaded_Serv()
	clientsock.sendall(Puzzle)
	

	while 1:
		data = clientsock.recv(4096).strip()
		if not data: break
		Index = server.is_match(data)
		clientsock.sendall(str(Index) + "\n")

		gameover = clientsock.recv(4096)
		if end_game_msg:
			gameover = 'n'
		
		if gameover == 'y':
			end_game_msg = True
		
		if end_game_msg:
			
			if gameover == 'y':
				clientsock.sendall("W")
				#time.sleep(3)
			
			elif gameover == 'n':
				clientsock.sendall("L")
				#time.sleep(3)
		
		else:
			clientsock.sendall("C")
				
	clientsock.close()
	print addr, "- closed connection" + "\n"
		
			

if __name__=='__main__':
	# Generate Puzzle 
	generate = random.randint(1, 126)
	Puzzle = linecache.getline('WordList.txt', generate)
	
	end_game_msg = False
	
	os.system('cls' if os.name == 'nt' else 'clear')
	print "\n" + Puzzle
	
	# Socket Setup 	
	ADDR = (HOST, PORT)
	serversock = socket(AF_INET, SOCK_STREAM)
	serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	serversock.bind(ADDR)
	serversock.listen(5)
	
	# Establish Connections 
	while 1:
		print 'waiting for connection... listening on port', PORT
		clientsock, addr = serversock.accept()

		print '...connected from:', addr
		t = thread.start_new_thread(handler, (clientsock, addr));

		#t = threading.Thread(target=handler, args=(thread_count,))
		threads.append(t)

		#(thread.start_new_thread(handler, (clientsock, addr)))
		
		
