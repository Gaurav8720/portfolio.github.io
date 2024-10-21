import socket
import threading


host = "127.0.0.1" #localhost
port = 49327

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname}' "left the chat!".encode('escii'))
            nicknames.remove(nickname)
            break



def receive():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')


        client.send("NICK".encode('escii'))
        nickname = client.recv(1024).decode("escii")
        nicknames.append(nickname)
        clients.append(client)

        print(f"nickname of the client is {nickname}!")
        broadcast(f'{nickname} joined the chat!'.encode('escii'))
        client.send('connected to the server!'.encode('escii'))


        thread = threading.Thread(target=handle, agrs=(client, ))
        thread.start()


print("server is listening.....")

receive()


