import socket
import sys, urllib, webbrowser, urllib2
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

#helper method to parse x and y coordinates from the http response 
def getCoords(message):
	a, b, c, d, e, f, g = message
	if a == 'y':
		Y_COORD = int(c)
		X_COORD = int(g)
	elif e == 'y':
		Y_COORD = int(g)
		X_COORD = int(c)
	return X_COORD, Y_COORD

def openBoard(path):
	host = 'http://localhost:'
	if PORT == 5000 and path == '/own_board.html':
		webbrowser.open(host + port + '/p1own_board.html')
		return 
	elif PORT != 5000 and path == '/own_board.html':
		webbrowser.open(host + port + '/p2own_board.html')
		return 
	elif PORT == 5000 and path == '/opponent_board.html':
		webbrowser.open(host + port + 'p1opponent_board.html')
		return 
	elif PORT != 5000 and path == '/opponent_board.html':
		webbrowser.open(host + port + '/p2opponent_board.html')
		return
	else:
		return
	return 
#class to handle http requests and use them to interact with battleship game
class myHandler(SimpleHTTPRequestHandler):
	
	def do_GET(self):
		self.send_response(200)
		# message = self.rfile.read(int(self.headers.getheader('Content-Length')))
		# board = message[4:7]
		# print board
		self.send_header('Content-type','text/html')
		self.end_headers()
		
		# Send the html message
		openBoard(self.path)
		result = self.path
		if result:
			self.wfile.write(result)
		else:
			self.wfile.write('There was an error')
		return

	#Handler for the POST requests
	def do_POST(self):
		self.send_response(200)
		message = self.rfile.read(int(self.headers.getheader('Content-Length')))
		X_COORD, Y_COORD = getCoords(message)
		#here is where we need to call battleship
		res = {key1 : X_COORD, key2 : Y_COORD}
		print res
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
