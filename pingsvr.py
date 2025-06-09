
# Server File
#Import library
from socket import *
import random
import sys

def createServer(port):
#     serverPort = 12000

    # Creating UDP socket
    serverSocket = socket(AF_INET, SOCK_DGRAM)

    # Binding socket to local port
    serverSocket.bind(('0.0.0.0', port))
    # Port display
    print(f"Server listenting on {port}")

    while True:
        # returns message and address of semder
        pingMsg, clientAddress = serverSocket.recvfrom(1024)

        # simulated packet loss, 30 percent loss
        if (random.randint(1, 100) <= 30):
            print(f"Packet Loss - Message Dropped")
            continue

        # received message succesfully
        if pingMsg:
             print(f"Recieved from {clientAddress}: {pingMsg.decode()}")
             response = pingMsg.decode()
             serverSocket.sendto(response.encode(), clientAddress)

    #Server is close using Ctrl C from the uyser

def main():
    # error if not enough arguments
    # exit program is this occurs
    if  len(sys.argv) != 2:
        print("Usage: python pyngsvr.py <port>")
        sys.exit(1)

    # storing port number as an int
    port = int(sys.argv[1])
    # creating server by passing port number
    createServer(port)

if __name__ == "__main__":
    main()

