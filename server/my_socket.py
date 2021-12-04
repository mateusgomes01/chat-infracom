#!/usr/bin/env python

from socket import *
import sys


def buffer_to_file(file, buffer, address, socket):
    data,address = socket.recvfrom(buffer)
    while(data != 'EOF'.encode()):
        file.write(data)
        data,address = socket.recvfrom(buffer)
    print("finished receiving file");

def file_to_buffer(file, buffer, address, socket):
    data = file.read(buffer)
    while (data):
        if(socket.sendto(data,address)):
            print("sending ...")
            data = file.read(buffer)
    socket.sendto('EOF'.encode(),address) # this indicates the end of the file to the server
    print("finished sending file");
