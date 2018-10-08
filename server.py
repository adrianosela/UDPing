from socket import *
from time import sleep
from random import randint
import random

# initUDPServer() initializes a socket for UDP communication
def initUDPServer(port):
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(('', port))
    print("UDP server running on port %d" % port)
    return s

# shutdownUDPServer() gracefully shuts down the UDP server
def shutdownUDPServer(socket):
    print("Shutting down UDP server...")
    socket.close()
    print("...done")
    exit(0)

# handleUDP() is our UDP request handler function
def handleUDP(socket):
    requestMsg, clientAddress = socket.recvfrom(2048)
    responseMsg = requestMsg.decode() # resp message is echoed req message
    delayMillis(5, 50)
    if (dropRequest(0.1)):
    	return
    socket.sendto(responseMsg.encode(), clientAddress)

def delayMillis(lowerBound, upperBound):
    sleep(randint(lowerBound,upperBound)/1000) # the sleep func takes seconds

def dropRequest(p):
    return random.random() < p

def main():
    s = initUDPServer(12000)
    while True:
        try:
            handleUDP(s)
        except KeyboardInterrupt:
    	    shutdownUDPServer(s)
    		
if __name__=="__main__":
    main()
