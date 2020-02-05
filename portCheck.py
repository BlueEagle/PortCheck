#!/usr/bin/env python
import socket
import subprocess
import sys
import pyfiglet
from datetime import datetime


# clear the screen
subprocess.call('clear', shell=True)

# variables and informing the user
firstPort = 1
lastPort = 65535

# Handling multiple or no arguments
if len(sys.argv)>1:
    remoteServer = sys.argv[1]
else:
    remoteServer = "localhost"


remoteServerIP = socket.gethostbyname(remoteServer)
print(pyfiglet.figlet_format("PortCheck"))
print("Scanning ports on machine: ", remoteServer, "\t(IP: ", remoteServerIP, ")\n\n")

# keeping time
startScanTime = datetime.now()

try:
    print("Port:\t\tService:")
    for port in range(firstPort, lastPort):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print(port, "\t\tN/A")
        sock.close()

except KeyboardInterrupt:
    print("\n\nExcuse me! I wasn't finished!")
    sys.exit()

except socket.gaierror:
    print("\n\nTarget hostname could not resolve, try something else.")
    sys.exit()

except socket.error:
    print ("\n\nSomething went wrong, generic error text here...")
    sys.exit()

# still keeping time
endScanTime = datetime.now()

# let me tell you how slow I am
elapsedTime = endScanTime - startScanTime

# wrapping things up, for now...
print("\n\nTotal scan time: ", elapsedTime)