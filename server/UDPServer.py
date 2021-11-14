#!/usr/bin/env python

from socket import *
import sys
import select

host="0.0.0.0"
port = 9999
s = socket(AF_INET,SOCK_DGRAM)
s.bind((host,port))

addr = (host,port)
buf=1024

# receives filename before receiving file
data,addr = s.recvfrom(buf)
filename = data.decode()

# creates a new file to write upcomming contents
f = open(filename,'w+b')
data,addr = s.recvfrom(buf)

# receives file contents
while(data != 'EOF'.encode()):
    f.write(data)
    data,addr = s.recvfrom(buf)

# creates new file name to send back to client
filename_client = 'copy_of_'+filename
s.sendto(filename_client.encode(),addr)
print("sending file name...")

f.seek(0) # moves pointer to beginning of file

# sends file back to client with new name
data = f.read(buf)
while(data):
    if(s.sendto(data,addr)):
        print("sending ...")
        data = f.read(buf)
s.sendto('EOF'.encode(),addr) # this indicates the end of the file to the client

print("finished")

f.close()
s.close()
