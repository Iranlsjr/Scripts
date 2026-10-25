#!/bin/python3

import socket
import sys

rHost = input("Insert IP or name of website: ")
rHostIP = socket.gethostbyname(rHost)

rPorts = [
    21,22,23,22,53,80,110,111,139,143,443,445,
    993,995,3306,3389,5432,5900,8000,8080,8443,32768
]

doorsOpen = 0

print("-" * 55)
print("Please wait, scanning in progress..." + str(rHost) +"!")
print("-" * 55)

try:
    for ports in rPorts:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        
        resultado = s.connect_ex((rHostIP,ports)) # if doors is open = 0 closed = 1
        
        if resultado == 0:
            print("The door {} is open" .format(ports))
            doorsOpen += 1
            s.close()
            
except KeyboardInterrupt:
    print("\n Program closed for the user!")
    print("-" * 55)
    sys.exit()
    
    
print("-" * 55)

if doorsOpen == 0:
    print("No open ports were found in " +str((rHostIP)))
else:
    print("Scan complete: {} open port(s).".format(doorsOpen))
    
print("_" *55)
        