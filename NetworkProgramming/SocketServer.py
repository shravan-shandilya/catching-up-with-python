import socket
import sys
 
HOST = '127.0.0.1'   
PORT = 8888 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
print 'Socket bind complete'    
s.listen(10)
print 'Socket now listening'
conn, addr = s.accept()
 
#whom did we connect with
print 'Connected with ' + addr[0] + ':' + str(addr[1])
