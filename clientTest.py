import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.189', 4000 ))
client.send('I am CLIENT\n'.encode())
from_server = client.recv(4096)
client.close()
print(from_server.decode('ascii'))
