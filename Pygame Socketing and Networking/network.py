import socket

class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.PORT = 5555
        self.HEADER = 2048
        self.FORMAT = 'utf-8'
        self.ADDR = (self.SERVER, self.PORT)
        #*Should be 'Connect'
        self.pos = self.connect()


    def connect(self):
        try:
            self.client.connect(self.ADDR)
            return self.client.recv(self.HEADER).decode(self.FORMAT)
        except:
            pass

    def send(self, data):
        try:
            #Alternate: self.client.send(str.encode(data))
            self.client.send(data.encode(self.FORMAT))
            return self.client.recv(self.HEADER).decode(self.FORMAT)

        except socket.error as e:
            print(e)

    def get_pos(self):
        return self.pos


