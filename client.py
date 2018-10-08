from socket import *
import time

# initSocket() intializes a socket for UDP communication
def initSocket(timeout):
    s = socket(AF_INET, SOCK_DGRAM)
    s.settimeout(timeout)
    return s

# ping() executes our ping for a given number of messages
def ping(messages, socket, host, port):
    for msg_num in range(0, messages):
        msg = "PING {0}".format(msg_num)
        socket.sendto(msg.encode(), (host, port))
        try:
            start = timeMillis()
            resp, serverAddr = socket.recvfrom(2018)
        except timeout:
            print("request timed out")
            continue
        print("%d ms %s" % (timeMillis()-start, resp.decode()))

def timeMillis():
    return int(round(time.time()*1000))

def main():
    s = initSocket(1)
    ping(100, s, '127.0.0.1', 12000)
    s.close()

if __name__=="__main__":
    main()
