
#*Each device on local network is given an ip address
#This is to differentiate devices on local network
import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

#!Send message
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    #!Have to make sure message is 64 bytes long
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

'''
#!Input can be used to send once at a time
input("Type message: ")
send("Hello World!")
#!When the disconnect message is sent, the client is removed.
input()
send("Hello everyone")
input()
send(DISCONNECT_MESSAGE)
'''

current_message = ""
while current_message != DISCONNECT_MESSAGE:
    current_message = input("Type message: ")
    send(current_message)