import socket
#*Use pickle to send objects
import pickle
#*We can serialize information

class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.PORT = 5555
        self.HEADER = 2048
        self.FORMAT = 'utf-8'
        self.ADDR = (self.SERVER, self.PORT)
        #*Should be 'Connect'
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.ADDR)
            #*Instead of decoding and encoding, we have to use pickle to encode and decode objects
            return pickle.loads(self.client.recv(self.HEADER))
        except:
            pass

    def send(self, data):
        try:
            #Alternate: self.client.send(str.encode(data))
            #self.client.send(data.encode(self.FORMAT))
            #!Instrad of encoding and sending, pickle using dumps
            self.client.sendall(pickle.dumps(data))
            return pickle.loads(self.client.recv(self.HEADER))

        except socket.error as e:
            print(e)




