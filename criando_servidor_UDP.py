import socket
import sys 

port = int(sys.argv[1])

connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
connection.bind(("0.0.0.0", port))


print("Aguardando conexao em 0.0.0.0:" + str(port))

while True:
    data, endereco = connection.recvfrom(1024)
    print(f"{endereco}: {data.decode()}")
    resposta = input("Server: ") + "\n"
    connection.sendto(resposta.encode(), endereco)
    
connection.close()