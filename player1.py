
import socket
import sys

HOST, PORT = "localhost", 9999
var = 1

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("connecting...")
try:
	sock.connect((HOST, PORT))
	print("connection established...\n")



#while var > 0:
	data = raw_input("Enter a guess: ")
	#print "You entered: ", data
	sock.sendall(data + "\n")

	# Receive data from the server and shut down
	received = sock.recv(1024)
	if (received == "match"):
		print("your guess of \"", data, "\" was correct...")
			
finally:
    sock.close()

print "Sent:     {}".format(data)
print "Received: {}".format(received)
