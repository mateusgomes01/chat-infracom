from socket import *

# Cria o socket UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

# Recebe o arquivo
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    filename = message.decode()
    print('Arquivo recebido: ' + filename)
    # MUDA O NOME DO ARQUIVO
    filename = filename.split('.')
    filename[0] = filename[0] + '_copia'
    filename = '.'.join(filename)
    print('Arquivo copiado: ' + filename)
    f = open(filename, 'wb')
    outputdata = f.read()
    f.close()
    serverSocket.sendto(outputdata, clientAddress)
    print('Arquivo enviado: ' + filename)
    serverSocket.close()
    print('Fim do programa')
    break
