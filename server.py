import SocketServer
import socket
import math
import linecache
import random

class MyServer():
	
	def __init__(self):
		generate = random.randint(1, 126)
		self.puzzle = linecache.getline('WordList.txt', generate)
		
		self.total_Length = len(self.puzzle) - 1
		self.player_score = 0
		print self.puzzle
		
				
	def match(self, data):
		index = 0
		matches = 0
		while index < len(self.puzzle):
			index = self.puzzle.find(data, index)
			if index == -1:
				break
			index += 1
			if (index >= 0):
				matches += 1
				self.player_score += 1
		#print index
		#print self.player_score
		return matches
		
	def isWinner():
		if (self.numRight == self.score):
			return 1
		else:
			return 0

if __name__ == "__main__":

	HOST, PORT = "localhost", 9999
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((HOST, PORT))
	sock.listen(5)
	conn, addr = sock.accept()
	print 'connected by', addr
	server = MyServer()
	conn.sendall(server.puzzle)
	
	while 1:
		data = conn.recv(1024).strip()
		if not data: break
		Index = server.match(data)
		if (Index < 0):
			conn.sendall(str(Index) + "\n")
		else :
			conn.sendall(str(Index) + "\n")
	
	conn.close()

