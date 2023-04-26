from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to recieve')
while True:
    connetionSocket, addr = serverSocket.accept()
    sentence = connetionSocket.recv(2048).decode()
    if sentence == ' ':
        connetionSocket.close()
        print('The server received termination signal.')
        break
    captializedSentence = sentence.upper()
    connetionSocket.send(captializedSentence.encode())
    connetionSocket.close()
    