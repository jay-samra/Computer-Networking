# Client File
from socket import *
import sys
import time

# createClient function takes in ip and port number
def createClient(svr_ip, svr_port):
    serverName = ''
    serverPort = 12000

    # Create UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    # client watis for one second until reply,
    # if no reply, then packet was lost
    clientSocket.settimeout(1)

    totalPackets = 0
    for i in range(1, 11):
        # storing the starting time of the message using time()
        beginningTime = time.time()
        message = "PING" + str(i)

        # using try statement for timeout waiting time
        try:
               clientSocket.sendto(message.encode(), (svr_ip, svr_port))
               response, filler = clientSocket.recvfrom(1024)
               endingTime = time.time()
               # inrementing packets
               totalPackets += 1
               # calculating RTT for packet
               RTT = (endingTime - beginningTime) * 1000
               print(f"Recieved from( {filler}): ({response.decode()}) - RTT: {RTT:.1f} ms ")
        # timeout message saying packet was lost
        except timeout:
               print(f"Request timed out for Ping {i}")

    # closing socket after all pings are sent
    clientSocket.close()
    #total packets lost
    totalLost = 10 - totalPackets
    # packets lost as a percentage
    percentageLost = (totalLost/10) * 100
    # Displaying total message statistics
    print("\nPing Statistics")
    print(f"Packets Sent: 10, Packets Recieved: {totalPackets}, Packets Lost:{totalLost} ({percentageLost:.1f})% lost ")
def main():
    # Exiting program if invalid num of arguments
    if len(sys.argv) != 3:
        print("Usage: python pingcli.py <server_ip> <server_port>")
        sys.exit(1)

   # ip stored as  string
    svr_ip = sys.argv[1]
    # port stored an int
    svr_port = int(sys.argv[2])

    createClient(svr_ip, svr_port)
# running main
if __name__ == "__main__":
    main()
