#!/usr/bin/env python

from socket import *
import threading
from my_socket import *
import sys

host = "localhost"
port = 9999
buf = 1024
s = socket(AF_INET, SOCK_DGRAM)
addr = (host, port)


username = input("Enter your name: ")
socket.sendTo(username.encode('utf-8'), addr)
response = socket.recvfrom(1048)
response = response.decode('utf-8')

if response == 'Nome de usuário em uso':
    print(f'\n{response}\n')
    socket.close()
    print('\n'+response)

threadR = threading.Thread(target=receive_message(), args=[s])
trreadS = threading.Thread(target=send_message(), args=[s, username])

trreadS.start()
threadR.start()
# opens file sent by command line
f = open(sys.argv[1], "rb")

# sends filename before sending file's content
filename = sys.argv[1] 
s.sendto(filename.encode(), addr)
print("sending file name...")

# starts sending the file to the server
file_to_buffer(f, buf, addr, s)

f.close()

# receives new file name from server
filename, addr = s.recvfrom(buf)
f = open(filename.decode(), 'wb') # creates new file with file name received from server

# starts receiving new file contents sent by the server
buffer_to_file(f, buf, addr, s) 

print("finished")

s.close()
f.close()
