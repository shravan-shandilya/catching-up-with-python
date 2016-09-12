#!/usr/bin/python
import socket
import sys,os
 
HOST = '127.0.0.1'   
PORT = 8888 
 
print 'Socket created'
 
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
	s.bind((HOST, PORT))
except socket.error , msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
print 'Socket bind complete'	
s.listen(10)
print 'Socket now listening'
conn, addr = s.accept()
handshake = conn.recv(1024)
if handshake.startswith("Hello"):
	username = handshake.split(" ")[2]
	conn.send("Message recieved")
data = conn.recv(1024)
while data != "nothing":
	if data.startswith("get"):
		temp_file = file("./resources/"+data.split(" ")[1],"r")
		temp_data = temp_file.read(1024)
		while temp_data:
			conn.send(temp_data)
			temp_data = temp_file.read(1024)
		conn.send("EOF")
		temp_file.close()
	elif data == "resources":
		conn.send(str(os.listdir("./resources")))
	else:
		break
	data = conn.recv(1024)
conn.close()
