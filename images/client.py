import socket
import threading

nickname = input("enter nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1",49327))

def receive():
    while True:
        try:
            message = client.recv(2024).decode('escii')
            if message == "NICK":
                client.send(nickname.encode('escii'))
            else:
                print(message)
        except:
            print("An error occured")
            client.close()
            break


def write():
    while True:
        message = f"{nickname}: {input("")}"
        client.send(message.encode("escii"))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()


