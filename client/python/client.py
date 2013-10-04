#/bin/python
# This is a simple TCP client script
# used to test an echo server running on port 8880

import socket

# Create the socket object
client_socket = socket.socket()

# Assume the server is running on the same host as this client
host = socket.gethostname()

# Assume the server is running on port 8880
port = 8880

# Connect to the server
client_socket.connect((host, port))

# This is the list of messages this client will send to the echo server
messages = ["Hello", "World", "this", "is", "an", "echo server", "test", "bye"]
for message in messages:
  print ">> Sent: ", message
  client_socket.send(message)

  print "<< Received: ", client_socket.recv(1024)

# Always remember to close the socket
client_socket.close()

