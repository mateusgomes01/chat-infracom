from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
while True:

    print("The server is ready to receive")
    message, clientAddress = serverSocket.recvfrom(2048)
    messageReceived = message.decode()
    print("Message received from client: " + messageReceived)
    modifiedMessage = messageReceived.upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print("The message has been modified and sent back to the client")
    if messageReceived == "exit":
        serverSocket.close()
        print("The server is closed")
        break

