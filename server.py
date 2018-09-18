import socket
import sys, urllib, webbrowser
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

#class to handle http requests and use them to interact with battleship game
class myHandler(SimpleHTTPRequestHandler):
	
	def do_GET(self):
		self.send_response(200)
		message = self.rfile.read(3)
		self.send_header('Content-type','text/html')
		self.end_headers()
		res = 'The board has been opened.'
		# Send the html message
		self.wfile.write(res)
		if message == 'own' and PORT == 5000:
			webbrowser.open('http://localhost:5000/P1/own_board.html')
			return
		elif message == 'own' and PORT != 5000:
			webbrowser.open('http://localhost:' + port + '/P2/own_board.html')
			return
		elif message == 'opp' and PORT == 5000:
			webbrowser.open('http://localhost:5000/P1/opponent_board.html')
			return
		elif message == 'own' and PORT != 5000:
			webbrowser.open('http://localhost:' + port + '/P2/opponent_board.html')
			return
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
