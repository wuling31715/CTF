import socket
import random

port = random.randint(1000, 9999)   
with open('port', 'w') as file:
    file.write(str(port))
s1 = socket.socket()
s1.bind(('127.0.0.1', port))
s1.listen(5)
while True:
    connect, address = s1.accept()
    print('connected from: %s' % (address,))
    message = 'connect success!'
    connect.sendall(message.encode())
    connect.close()