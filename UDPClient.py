from socket import *
serverName = 'localhost'
serverPort = 12000
while True:
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = input('Type a message: ')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print('Message received from server:' + modifiedMessage.decode())
    clientSocket.close()
    if message == 'exit':
        break


