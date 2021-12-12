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
    print("finished receiving file");


def file_to_buffer(file, buffer, address, socket):
    data = file.read(buffer)
    while data:
        if socket.sendto(data, address):
            print("sending ...")
            data = file.read(buffer)
    socket.sendto('EOF'.encode(), address)  # this indicates the end of the file to the server
    print("finished sending file");


def usernameIsValid(username):
    for client in clients:
        if username == client["username"]:
            return False
    return True


def messagesTreatment(client, buffer):
    username = client["username"]
    client = client["sock"]
    while True:
        try:
            data, address = socket.recvfrom(buffer)
            data = data.decode('utf-8')
            broadcast(data, username)
        except:
            deleteClient(client)


def broadcast(message, username):
    for client in clients:
        if client["username"] != username:
            try:
                socket.sendto(f'<{datetime.datetime.now().time()}><{username}><{message}'.encode('utf-8'), client["address"])
            except:
                deleteClient(client)
                break


def deleteClient(client):
    clients.remove(client)
    msg = f'{client["username"]} disconnected!\n'
    broadcast(msg, "Server")

