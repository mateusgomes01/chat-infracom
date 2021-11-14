from socket import *

#definindo o endereco do servidor
serverName = 'localhost'
serverPort = 12000
#definindo o endereco do cliente
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Create a UDP socket
sock = socket(AF_INET, SOCK_DGRAM)
server_address = (serverName, serverPort)
# Send data
filename = input("Digite o nome do arquivo: ")
file = open(filename, "r+b")
file_data = file.read(1024)
file.close()
sock.sendto(file_data, server_address)
print("Enviado!")
#receber o arquivo de volta do servidor
file_data, server = sock.recvfrom(1024)
print("Recebido!")
file = open(file_data, "wb")
file.write(file_data)
file.close()
print("Arquivo recebido!")
# Close the socket
sock.close()



