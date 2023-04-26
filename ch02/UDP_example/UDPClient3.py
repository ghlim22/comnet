from socket import *
from select import *
import sys
from time import ctime

SERVER = "127.0.0.1"
SERVER_PORT = 12000
BUFSIZE = 1024
SERVER_ADDR = (SERVER, SERVER_PORT)

# generate socket - client side.
clientSocket = socket(AF_INET, SOCK_DGRAM)
# get user input sentence.
sentence = input('Input lowercase sentence: ')
# send the sentence to the server using UDP protocol.
clientSocket.sendto(sentence.encode(), SERVER_ADDR)
ModifiedSentence, ServerAddr = clientSocket.recvfrom(BUFSIZE)
print(ModifiedSentence.decode())
clientSocket.close()