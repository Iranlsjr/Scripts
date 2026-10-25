#!/bin/python3

import socket
import sys

ports = [ 21,22,23,22,53,80,110,111,139,143,443,445,
    993,995,3306,3389,5432,5900,8000,8080,8443,32768]

for portas in ports:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    code = mysocket.connect_ex((sys.argv[1], portas))
    
    if code == 0:
        print(portas, "Abertas")
