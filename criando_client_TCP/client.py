import socket
import sys

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket()
s.connect((host,port))
print("Conected with Host: " host)

while True:
    msg = input()  + "\n"
    s.send(msg.encode())