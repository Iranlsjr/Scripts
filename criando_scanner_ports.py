#!/usr/bin/env python3

import socket
import sys
import ipaddress

rede = ipaddress.ip_network(sys.argv[1], strict=False)

ports = [21, 22, 23, 53, 80, 110, 111, 139, 143, 443, 445,
         993, 995, 3306, 3389, 5432, 5900, 8000, 8080, 8443, 32768]

for ip in rede.hosts():
    for porta in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((str(ip), porta)) == 0:
            print(ip, porta, "Aberta")
        s.close()