import socket

ip = '192.168.1.1'
port = '80'
s = socket.socket()
response = s.connect((ip, int(port)))
message = '1111'
s.send(message.encode())
service = s.recv(1024)
s.close()
print(service)