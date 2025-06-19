from socket import *
import sys

# Import the socket module for networking operations
import socket

# Set the target IP address (Google DNS in this case)
target = "8.8.8.8"  # Google DNS (example public IP)

# The range for which the ports will be scanned
portLow = 10
portHigh = 20

# Set the port number to scan (53 is used for DNS)
#port = 53  # DNS port, typically open on DNS servers

def tcpScanner(portLow, portHigh, target):
    # Looping from lowest port to high port, i = port
    for i in range(portLow, portHigh + 1):
  
      # Create a TCP socket 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout for 2 seconds
        sock.settimeout(2)  


        try:
            # Connect to the target and port
            result = sock.connect_ex((target, i))

            # If result is 0, the port is open
            if result == 0:
                print(f"Port {i} Open")
            else:
                # Any non-zero result means the port is closed or filtered
                print(f"Port {i} is Closed")

        # Handle case where connection times out
        except socket.timeout:
            print(f"Connection to {target}:{i} TIMED OUT")

        # Handle any other unexpected exceptions
        except Exception as e:
            print(f"Error occurred: {e}")

        # This block always runs; ensure the socket is properly closed
        finally:
            sock.close()
            
def udpScanner(portLow, portHigh, target):
    
    for i in range(portLow, portHigh, target):
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        sock.settimeout(2)

        try:
            print(f"Port {i} Open")
        
        except socket.timeout:
            print(f"Port {i} Closed")
            
        except Exception as e:
            print(f"Port {i} Closed")
        
        finally:
            sock.close()
            
            

def main():
    if len(sys.argv) != 5:
        print("Usage: python3 portscan.py <hostname> <protocol> <portlow> <porthigh>")
        sys.exit(1)
        
    # portScan <hostname> <protocol> <portlow> <porthigh>
    
    hostname = sys.argv[1]
    
    protocol = sys.argv[2]

    portLow = int(sys.argv[3])
    
    portHigh = int(sys.argv[4])
    
    hostName = socket.gethostbyname(hostname)
    
    if (protocol == "tcp"):
        tcpScanner(portLow, portHigh, hostName)
    elif (protocol == "udp"):
        udpScanner(portLow, portHigh, hostName)