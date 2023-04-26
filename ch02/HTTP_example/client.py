from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = ' ' 
clientSocket.send(message.encode())
recvMessage = clientSocket.recv(2048)
print("from server: ", recvMessage.decode())
clientSocket.close()
