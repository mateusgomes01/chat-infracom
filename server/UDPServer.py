#!/usr/bin/env python

from socket import *
from my_socket import *
import sys

host = "0.0.0.0"
port = 9999
buf = 1024
s = socket(AF_INET,SOCK_DGRAM)
s.bind((host,port))
addr = (host,port)

# receives filename before receiving file
data,addr = s.recvfrom(buf)
filename = data.decode()

# creates a new file to write upcomming contents
f = open(filename,'w+b')

# receives file contents
buffer_to_file(f, buf, addr, s)


# creates new file name to send back to client
filename_client = 'copy_of_'+filename
s.sendto(filename_client.encode(),addr)
print("sending file name...")

f.seek(0) # moves pointer to beginning of file

# sends file back to client with new name
file_to_buffer(f, buf, addr, s)

print("finished")

f.close()
s.close()
