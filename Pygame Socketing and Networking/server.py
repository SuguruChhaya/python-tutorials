import socket
import sys
import threading

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


#!Convert string into tuple
def read_pos(str):
    '''
    Input is something like '45, 67'
    Return as tuple with integer
    '''
    str = str.split(',')
    return int(str[0]), int(str[1])

#!Convert tuple into string
def make_pos(tup):
    '''
    Input: (45, 67)
    Output: '45, 67'
    '''
    return str(tup[0]) + ',' + str(tup[1])

#!Starting position of the 2 players
pos = [(0, 0), (100, 100)]
def threader_client(conn, player):
    connected = True
    #!Need to understand encoding format
    #*After first connection, loses connection when nothing else is going to be sent
    conn.sendall(make_pos(pos[player]).encode(FORMAT))
    while connected:
        
        try:
            #!The player position will be sent from client.py in "45, 67" form. 
            #*We have to turn that into a tuple
            #?Issue somewhere is code because except is reached
            reply = read_pos(conn.recv(HEADER).decode(FORMAT))
            try:
                #!Updating the tuple list so it contains current location
                pos[player] = reply
            except:
                print('error 1')

            
            if reply:
                if player == 1:
                    try:
                        sending = pos[0]
                    except:
                        print('error 2')
                else:
                    try:
                        sending = pos[1]
                    except:
                        print('error 3')
                print("Recevied: ", reply)
                print("Sending: ", sending)

                #!Have to be careful about format or will go to except

                #!Error right here
                conn.sendall(make_pos(sending).encode(FORMAT))
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
    
