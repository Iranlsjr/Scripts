import socket
import sys

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket()
s.connect((host,port))
print ("Conected with Host: "+ host)

while True:
    msg = input()  + "\n "
    s.sendall(msg.encode())
    
    resposta = s.recv(1024).decode()
    
    if not resposta:
        print("Servidor desconectou")
        break
    print(resposta)

s.close()