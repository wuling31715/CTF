import socket

with open('port', 'r') as file:
    port = int(file.read())
s2 = socket.socket()
s2.connect(('127.0.0.1', port))
message = s2.recv(1024)
s2.close()
print('receive: %s' % str(message))