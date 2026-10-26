#!/usr/bin/env python3

import socket
import sys
import ipaddress

alvo = sys.argv[1]

ports = [21, 22, 23, 25, 53, 80, 110, 111, 139, 143, 443, 445,
         993, 995, 3306, 3389, 5432, 5900, 6379, 8000, 8080, 8443, 32768]

def pegar_banner(s):
    try:
        s.settimeout(0.2)
        dados = s.recv(1024)
        return dados.decode(errors="replace").strip()
    except   (socket.timeout, ConnectionResetError, OSError):
        return ""

def escanear(ip):
    for porta in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.2)
        if s.connect_ex((ip, porta)) == 0:
            banner = pegar_banner(s)
            if  banner:
                print(ip, porta, "Aberta", "-", banner)
            else:
                print(ip, porta, "Aberta")
        s.close()

if "/" in alvo:
    # É uma rede, ex.: 192.168.1.0/24
    rede = ipaddress.ip_network(alvo, strict=False)
    for ip in rede.hosts():
        escanear(str(ip))
else:
    try:
        ip = str(ipaddress.ip_address(alvo))
    except ValueError:
        # Não é IP, tenta resolver como domínio
        try:
            ip = socket.gethostbyname(alvo)
            print(f"Resolvendo {alvo} -> {ip}")
        except socket.gaierror:
            print(f"Nao foi possivel resolver {alvo}")
            sys.exit(1)
    escanear(ip)