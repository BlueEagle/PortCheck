#!/usr/bin/env python
import nmap
import socket
from tabulate import tabulate
import subprocess
import sys
import pyfiglet
import time
from datetime import datetime

# variables and informing the user
firstPort = 1 # 21 # 1
lastPort = 65535 # 443 # 65535
waitTime = 3


# Handling multiple or no arguments
if len(sys.argv)>1:
    remoteServer = sys.argv[1]
else:
    remoteServer = "localhost"


def main():
    # clear the screen
    subprocess.call('clear', shell=True)

    # create and run scanner on port range
    scanner = nmap.PortScanner()
    scanner.scan(remoteServer, str(firstPort)+"-"+str(lastPort))

    # make csv to parse...
    scanInfo = scanner.csv()

    # split 'CSV' into lines and remove emtpy elements
    lines = scanInfo.split('\r\n')
    lines = list(filter(None, lines))

    # Print stuff
    print(pyfiglet.figlet_format('PortCheck'))
    print('Scanning ports on machine: {}\t(IP: {})\n\n'.format(remoteServer, socket.gethostbyname(remoteServer)))

    # Titles
    #print('Port:\t\tProtocol:\t\tService:\t\tState:\t\tProduct:\t\tVersion:\t\tExtra Info:\t\tCPEs:')
    header = ['Port:','Protocol:','Service:','State:', 'Product:', 'Version:','Extra Info:', 'CPEs:']

    # delete title line
    lines.pop(0)
    alsoLines = []
    for line in lines:

        # make it look pretty, vars for you sir!
        line = line.split(';', -1)
        port = line[4]
        protocol = line[3]
        service = line[5]
        state = line[6]
        product = line[7]
        version = line[10]
        extra_info = line[8]
        cpes = line[12]

        # generate modified line
        line = [port,protocol,service,state,product,version,extra_info,cpes]

        # make it real, bro
        alsoLines.append(line)
        


    print(tabulate(alsoLines, headers=header))
    #print(tabulate(lines, headers=header))
    


main()
while False:
    main()

    try:
        time.sleep(waitTime)

    except KeyboardInterrupt:
        print("\n\nExcuse me! I was about to refresh!")
        sys.exit()

    except socket.error:
        print ("\n\nSomething went wrong, generic error text here...")
        sys.exit()