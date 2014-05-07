import SocketServer
import socket
import math
import linecache
import random

class MyServer():
	
	def __init__(self):
	
		generate = random.randint(1, 1000)
		chooseWord = (generate % 126)
		if (chooseWord == 0):
			chooseWord = (chooseWord + 1)
		self.Word = linecache.getline('WordList.txt', chooseWord)
		print self.Word
		
	def match(self, data):
		index = self.Word.find(data)
		print data
		print index
		return index

if __name__ == "__main__":

	HOST, PORT = "localhost", 9999
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((HOST, PORT))
	sock.listen(1)
	conn, addr = sock.accept()
	print 'connected by', addr
	server = MyServer()
	conn.sendall(server.Word)
	
	while 1:
		data = conn.recv(1024).strip()
		if not data: break
		Index = server.match(data)
		if (Index < 0):
			conn.sendall('nomatch')
		else :
			conn.sendall(str(Index) + "\n")
	
	conn.close()

