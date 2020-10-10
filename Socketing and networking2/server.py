import socket
import threading
#Allows to run multiple threads at once

HEADER = 64
PORT = 5050
#*Automatically gets ip address
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

#Make socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

#*Handle information comming in
#!Handles individual connections
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True

    while connected:
        #*Active when something is received
        #!Every time message is sent, message is encoded.
        #!To receive, we have to decode
        msg_length = conn.recv(HEADER).decode(FORMAT)
        #print(msg_length)
        #!If I continue to print the above, I will never see my message
        #!Have to check whether valid message is sent before trying to int it
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            
            #!Check if disconnected
            if msg == DISCONNECT_MESSAGE:
                connected = False
                conn.send("You disconnected".encode(FORMAT))

            else:
                conn.send("Message received".encode(FORMAT))

                

            print(f"[{addr}]: {msg}")

    conn.close()

#*New connection starts
#!Handles all the connections and distributes
def start():
    #Listen connection
    server.listen(1)
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        #*Number of active connections
        #!Since the start thread is always running, have to subtract 1
        print(f"\n[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

        



print('Server is starting...')
start()

#*Disable firewall

