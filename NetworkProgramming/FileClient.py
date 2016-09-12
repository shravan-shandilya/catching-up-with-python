#!/usr/bin/python
import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1" , 8888))
s.send("Hello,this is shravan")
data = s.recv(1024)
s.send("resources")
available_resources = s.recv(1024)
print "Available resurces",available_resources
print "type 'nothing' to quit"
resource = raw_input("What do you want?\n")
while resource != "nothing":
	s.send("get "+resource)
	recv_file = file("recieved/"+resource,"w+")
	data = ""
	while data != "EOF":
		recv_file.write(data)
		data = s.recv(1024)
		print data
	recv_file.close()
	print "available resources",available_resources
	resource = raw_input("what do you want?\n")
s.close()
