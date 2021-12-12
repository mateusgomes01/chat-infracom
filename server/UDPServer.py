#!/usr/bin/env python

from socket import *
import threading
from my_socket import *
import sys

clients = []  # list of clients connected

host = "0.0.0.0"
port = 9999
buf = 1024
s = socket(AF_INET, SOCK_DGRAM)
addr = (host, port)
s.bind(addr)

while True:
    username, addr = s.recvfrom(buf)
    username = username.decode('utf-8')

    client = {
        'username': username,
        'addr': addr
    }

    if not usernameIsValid(username):
        print('Fechando conexão')
        username.send('Nome de usuário em uso'.encode('utf-8'))
        username.close()
    else:
        clients.append(client)
        print('Cliente conectado: ', client['username'])
        username.send('Connectado'.encode('utf-8'))

        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()
# receives filename before receiving file
data, addr = s.recvfrom(buf)
filename = data.decode()

# creates a new file to write upcomming contents
f = open(filename, 'w+b')

# receives file contents
buffer_to_file(f, buf, addr, s)

# creates new file name to send back to client
filename_client = 'copy_of_' + filename
s.sendto(filename_client.encode(), addr)
print("sending file name...")

f.seek(0)  # moves pointer to beginning of file

# sends file back to client with new name
file_to_buffer(f, buf, addr, s)

print("finished")

f.close()
s.close()
