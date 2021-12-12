#!/usr/bin/env python

import datetime
from socket import *
import sys

from server.UDPServer import clients


def buffer_to_file(file, buffer, address, socket):
    data, address = socket.recvfrom(buffer)
    while data != 'EOF'.encode():
        file.write(data)
        data, address = socket.recvfrom(buffer)
    print("finished receiving file")


def file_to_buffer(file, buffer, address, socket):
    data = file.read(buffer)
    while data:
        if socket.sendto(data, address):
            print("sending ...")
            data = file.read(buffer)
    socket.sendto('EOF'.encode(), address)  # this indicates the end of the file to the server
    print("finished sending file")


def receive_message(address):
    while True:
        try:
            msg, address = socket.recvfrom(2048).decode('utf-8')
            print(msg + "\n")
        except:
            print("connection closed")
            socket.close()
            break


def send_message(address, username):
    while True:
        msg = input("\n")
        socket.sendto(f'<{username}> {msg}'.encode('utf-8'), address)

def usernameIsValid(username):
    for client in clients:
        if username == client["username"]:
            return False
    return True