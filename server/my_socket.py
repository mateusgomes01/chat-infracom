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
    print("finished sending file");


def usernameIsValid(username):
    for client in clients:
        if username == client["username"]:
            return False
    return True


def messagesTreatment(client, buffer):
    username = client["username"]
    client = client["addr"]
    while True:
        try:
            data, address = socket.recvfrom(buffer)
            data = data.decode('utf-8')
            if data == f'hi, meu nome eh {username}':
                data = f'O {username} esta conectado!\n'
                broadcast(data, username)
            elif data == 'bye':
                data = f'O {username} esta desconectado!\n'
                broadcast(data, username)
                deleteClient(client)
                break
            elif data == 'list':
                for client in clients:
                    socket.sendto(client["username"].encode('utf-8'), address)
            else:
                data = f'<{datetime.datetime.now().time()}><{username}>: <{data}'
                broadcast(data, username)
        except:
            deleteClient(client)


def broadcast(message, username):
    for client in clients:
        if client["username"] != username:
            try:
                socket.sendto(f'<{message}'.encode('utf-8'), client["addr"])
            except:
                deleteClient(client)
                break


def deleteClient(client):
    clients.remove(client)
    msg = f'{client["username"]} disconnected!\n'
    broadcast(msg, "Server")
