#!/bin/python 
# This is a simple echo server
# An echo server will send back to client
# the same message it received.
# This server will accept only one connection

import socket

class Server:
  def __init__(self, host='', port=8888):
    """
    By default this server will run at localhost  
    on port 8888, but a different host and port can 
    be informed during object creation
    """
    self.host = host
    self.port = port

  def run(self):
    # create a new socket that uses TCP and IPV4
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the socket just created to the host and port
    server_socket.bind((self.host, self.port))

    # start listening in the socket for connections
    # this socket will have at most 1 connection queued
    server_socket.listen(1)

    print "Server ready to receive connection"

    # accept a new connection
    client, address = server_socket.accept()
    
    print "Got a new connection from ", address

    while True:
      # wait to receive some data from client
      # read 1024 bytes from the socket
      # if client send 'bye', then finishes
      data = client.recv(1024)
      
      if data:
        # send back what it received
        print "received ", data
        client.send(data)

        if data == 'bye':
          break

    # close client socket
    client.close()

    # close server socket
    server_socket.close()

# end of Server class


# Main 
server = Server("0.0.0.0", 8880)
server.run()
