from socket import *
import sys

def main():
    if len(sys.argv) != 5:
        print("Usage: python3 portscan.py <hostname> <protocol> <portlow> <porthigh>")
