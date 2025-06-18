from socket import *
import sys

# Import the socket module for networking operations
import socket

# Set the target IP address (Google DNS in this case)
target = "8.8.8.8"  # Google DNS (example public IP)

# Set the port number to scan (53 is used for DNS)
port = 53  # DNS port, typically open on DNS servers

# Create a TCP socket using IPv4 addressing
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set a timeout for the socket operation (in seconds)
sock.settimeout(2)  # Wait up to 2 seconds before giving up

try:
    # Try to connect to the target and port
    # connect_ex() returns 0 if connection is successful, else an error code
    result = sock.connect_ex((target, port))

    # If result is 0, the port is open
    if result == 0:
        print(f"Port {port} is OPEN on {target}")
    else:
        # Any non-zero result means the port is closed or filtered
        print(f"Port {port} is CLOSED or FILTERED on {target}")

# Handle case where connection times out
except socket.timeout:
    print(f"Connection to {target}:{port} TIMED OUT")

# Handle any other unexpected exceptions
except Exception as e:
    print(f"Error occurred: {e}")

# This block always runs; ensure the socket is properly closed
finally:
    sock.close()



def main():
    if len(sys.argv) != 5:
        print("Usage: python3 portscan.py <hostname> <protocol> <portlow> <porthigh>")
        sys.exit(1)