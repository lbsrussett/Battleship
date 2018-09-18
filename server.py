import socket
import sys, urllib
from pprint import pprint
import httplib
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SimpleHTTPServer import SimpleHTTPRequestHandler

#retrieve port and board inputs from command line
port = sys.argv[1]
own_board = sys.argv[2]
key1 = 'hit='
key2 = 'sink='
X_COORD = -1
Y_COORD = -1

HOST = '127.0.0.1'   
PORT = int(port)

#class to handle http requests - it starts to work, but does not finish sending response
class myHandler(SimpleHTTPRequestHandler):
	
	#Handler for the POST requests
	def do_POST(self):
		content_length = self.headers.getheaders('content-length')
		l = int(content_length[0]) if content_length else 0
		self.send_response(200)
		message = self.rfile.read(int(self.headers.getheader('Content-Length')))
		print message
		res = {key1 : 'B', key2 : 'T'}
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write(res)
		return			
try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer((HOST, PORT), myHandler)
	print 'Started httpserver on port', PORT
	
	#Wait forever for incoming http requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
