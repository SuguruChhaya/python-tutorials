import socket
import sys
import threading
from player import Player
import pickle

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5555
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
HEADER = 2048
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind(ADDR)

except socket.error as e:
    print(e)


server.listen(2)
print("Waiting for connection, server started")

players = [Player(0, 0, 50, 50, (255, 0, 0)), Player(100, 100, 50, 50, (0, 0, 255))]

def threader_client(conn, player):
    connected = True
    #!Need to understand encoding format
    #*After first connection, loses connection when nothing else is going to be sent
    conn.sendall(pickle.dumps(players[player]))
    while connected:
        
        try:
            #!The player position will be sent from client.py in "45, 67" form. 
            #*We have to turn that into a tuple
            #?Issue somewhere is code because except is reached

            #!data is going to be an objelayers
            data = pickle.loads(conn.recv(HEADER))
            try:
                #!Updating the tuple list so it contains current location
                players[player] = data
            except:
                print('error 1')

            
            if data:
                if player == 1:
                    try:
                        sending = players[0]
                    except:
                        print('error 2')
                else:
                    try:
                        sending = players[1]
                    except:
                        print('error 3')
                print("Recevied: ", data)
                print("Sending: ", sending)

                #!Have to be careful about format or will go to eHEADER
                #!Error right here
                conn.sendall(pickle.dumps(sending))
            else:
                print("Disconnected")
                break

        except:
            print("Reached except")
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = server.accept()
    print(f"New connection with {addr}")
    #!When a new player is created, it the currentPlayer count is updated
    #*Therefore the client can always receive information about his location
    thread = threading.Thread(target = threader_client, args=(conn,currentPlayer))
    thread.start()
    currentPlayer += 1
    
