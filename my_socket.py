#!/usr/bin/env python

from socket import *
import sys


def buffer_to_file(file, buffer, address, socket):
    data,address = socket.recvfrom(buffer)
    while(data != 'EOF'.encode()):
        file.write(data)
        data,address = socket.recvfrom(buf)
    print("finished receiving file");
