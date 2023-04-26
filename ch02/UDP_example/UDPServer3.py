from socket import *
from select import *
import sys
from time import ctime

TERM_MSG = "The server has terminated."

HOST = ''
PORT = 12000
BUFSIZE = 1024
ADDR = (HOST, PORT)

# generate socket for UDP transport.
serverSocket = socket(AF_INET, SOCK_DGRAM)
# bind port to socket.
serverSocket.bind(ADDR)
print('The server is ready to receive.')

while True:
    clientMsg, clientAddr = serverSocket.recvfrom(BUFSIZE)
    clientSentence = clientMsg.decode()
    if clientSentence == '' or clientSentence == ' ':
        serverSocket.sendto(TERM_MSG.encode(), clientAddr)
        serverSocket.close()
        break
    modifiedMsg = clientSentence.upper()
    serverSocket.sendto(modifiedMsg.encode(), clientAddr)
exit()
