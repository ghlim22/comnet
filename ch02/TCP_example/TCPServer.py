from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM) # creating the welcoming socket for receiving a TCP connection establishment request from a client.
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(2048).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
