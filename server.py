#https://www.acmesystems.it/python_http

import socket
import sys
from pprint import pprint
import httplib
import requests
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

# BUFFER_SIZE = 1024

#retrieve port and board inputs from command line
port = sys.argv[1]
own_board = sys.argv[2]
key1 = 'hit='
key2 = 'sink='

#initialize sockets for servers
# s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'   
PORT = int(port)
res = {key1 : 'B', key2 : 'F'}

#class to handle http requests - it starts to work, but does not finish sending response
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the POST requests
	def do_POST(self):
		print 'post request entered'
		print self.wfile
		self.send_response(200)
		self.end_headers()
		self.wfile.write(res)
		return			
try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer((HOST, PORT), myHandler)
	print 'Started httpserver on port', PORT
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()

#bind first server to socket
# s1.bind((HOST, PORT))
# print 'Successfully connected to: ' + str(PORT)

# s1.listen(10)



#create listening connection to receive data from client
# conn, addr = s1.accept()
# print 'Connected with ' + addr[0] + ':' + str(addr[1])


# data = conn.recv(BUFFER_SIZE)
# if data:
# 	print data
# else:
# 	print 'no data'

# response = 'B'
# conn.send(response)
# conn.close()

#need logic to take data from client side to interact with battleship game
#need to update own_board based on game logic

