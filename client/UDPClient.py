#!/usr/bin/env python

from socket import *
from ..my_socket import *
import sys

host = "localhost"
port = 9999
buf = 1024
s = socket(AF_INET,SOCK_DGRAM)
addr = (host,port)

# opens file sent by command line
f = open (sys.argv[1], "rb")

# sends filename before sending file's content
filename = sys.argv[1] 
s.sendto(filename.encode(),addr)
print("sending file name...")

# starts sending the file to the server
# <<<<<<<<<<<<<<<<<<<<<<<< func b
data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        print("sending ...")
        data = f.read(buf)
s.sendto('EOF'.encode(),addr) # this indicates the end of the file to the server
# >>>>>>>>>>>>>>>>>>>>>>>> func b

f.close()

# receives new file name from server
filename,addr = s.recvfrom(buf)
f = open(filename.decode(),'wb') # creates new file with file name received from server

# starts receiving new file contents sent by the server
# <<<<<<<<<<<<<<<<<<<<<<<< func a
# data,addr = s.recvfrom(buf)
# while(data != 'EOF'.encode()):
#     f.write(data)
#     data,addr = s.recvfrom(buf)
# >>>>>>>>>>>>>>>>>>>>>>>> func a
ms.buffer_to_file(f, buf, addr, s) 

print("finished")

s.close()
f.close()
