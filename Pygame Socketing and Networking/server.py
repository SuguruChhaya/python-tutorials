import socket
from _thread import *
import sys

'''
Socket allows information to come into a server.
'''
#ipconfig ipv4 address
server = '192.168.0.16'
#Using this port to connect
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Binding
try:
    s.bind((server, port))

except socket.error as e:
    str(e)

#Open up a port
#arg is for how many people can connect to server
s.listen(2)
print('Waiting for connection, Server started!')


def threaded_connection(conn):
    #*Continually run while user is connected. 
    conn.send(str.encode("Connected"))
    reply = ''
    while True:
        #Receiving bits
        try:
            data = conn.recv(2048)
            #Have to encode information
            reply = data.decode("utf-8")
            if not data:
                print('Disconnect')
                break

            else:
                print('Received', reply)
                print('Sending', reply)

            #encode
            conn.send_all(str.encode(reply))

        except:
            break

    print('Lost connection')
    conn.close()

while True:
    #*Continuosly look for activity

    #Access incoming connection and ip address
    conn, addr = s.accept()
    print('Connected to: ' + str(addr))

    start_new_thread(threaded_connection, (conn, ))

    '''
    Usually, if a function is called in a while loop, the function has to finish executing, then the while loop gets executed. 
    But we don't want that since there are multiple connections going on at the same time.
    So, we start a new thread so it doens't have to wait.
    '''
