from socket import *
import sys
termMessage = 'server has terminated.'
okMessage = 'HTTP/1.1 200 OK'
notfoundMessage = 'HTTP/1.1 404 NOT FOUND'
badrequestMessge = 'HTTP/1.1 400 BAD REQUEST'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('the server is ready to receive.')
while True:
    connectionSocket, clientAddr = serverSocket.accept()
    message = connectionSocket.recv(2048).decode()
    if message == ' ' or message == '':
        connectionSocket.send(termMessage.encode())
        connectionSocket.close()
        serverSocket.close()
        break
    print('received message: ', message)
    print(len(message))
    messageFields = message.split()
    connectionSocket.send(messageFields[0].encode())
    print(messageFields)
    print(clientAddr)
    connectionSocket.close()