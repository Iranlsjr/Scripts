import socket
import sys

host = sys.argv[1]
port = int(sys.argv[2])

connection  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
connection.connect((host,port))

print ("Conected with Host: "+ host)

while True:
    msg = input("Client:")  + "\n "
    connection.sendall(msg.encode())
    
    resposta = connection.recv(1024).decode()
    print(resposta)