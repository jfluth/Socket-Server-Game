
import socket
import sys

HOST, PORT = "localhost", 9999

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("connecting...")
try:
	sock.connect((HOST, PORT))
	print("connection established...\n")

	Word = sock.recv(4096)
	blank = ' _ '
	wordMask = blank*(len(Word) - 1)
	print wordMask
	
	data = raw_input("Enter a guess: ")
	#print "You entered: ", data
	sock.sendall(data + "\n")
	

	# Receive data from the server and shut down
	received = sock.recv(1024)

	if (received == "nomatch"):
		print("you guessed incorrectly...\n")
		
	else:
		print "you guessed correct...\n"
		#wordMask[received] = data
		#print wordMask
	
		
except (OverflowError, IOError):
	print("Error Message")	
			
finally:
    sock.close()

print "Sent:     {}".format(data)
print "Received: {}".format(received)
