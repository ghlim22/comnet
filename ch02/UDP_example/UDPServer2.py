from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while True:
    sentence, clientAddr = serverSocket.recvfrom(2048)
    modifiedSentence = sentence.decode().upper()
    serverSocket.sendto(modifiedSentence.encode(), clientAddr)