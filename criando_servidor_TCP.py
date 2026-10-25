import socket
import sys 

port = int(sys.argv[1])

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection.bind(("0.0.0.0", port))
connection.listen(1)

print("Aguardando conexao em 0.0.0.0:" + str(port))
connection_2, endereco= connection.accept()

print("Conectado com", endereco)

while True:
    msg = connection_2.recv(1024).decode()
    if not msg:
        print("Cliente desconectou")
        break
    
    print(msg)
    
    resposta = input("Server") +"\n"
    connection_2.sendall(resposta.encode())
    
connection_2.close()
connection.close()