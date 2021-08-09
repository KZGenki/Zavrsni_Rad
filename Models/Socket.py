from abc import abstractmethod
import socket
import pickle

class Socket:
    def __int__(self, address = None, port = None):
        self.addr = address
        self.port = port
    def setup(self, address, port):
        self.addr = address
        self.port = port
    @abstractmethod
    def get_data(self):
        pass
    @abstractmethod
    def send_data(self):
        pass

class SocketServer(Socket):
    def __init__(self, address = None, port = None):
        super().__int__(address,port)
    def get_data(self):
        self.socket = socket.socket()
        self.socket.bind((self.addr, self.port))
        self.socket.listen(1)
        conn, addr = self.socket.accept()
        print("Got connection from ", addr)
        raw_data = conn.recv(4096)
        data = pickle.loads(raw_data)
        conn.close()
        self.socket.close()
        return data
    def send_data(self, data):
        self.socket = socket.socket()
        self.socket.bind((self.addr, self.port))
        self.socket.listen(1)
        conn, addr = self.socket.accept()
        print("Got connection from ", addr)
        conn.send(pickle.dumps(data)) #error
        conn.close()
        self.socket.close()

class SocketClient(Socket):
    def __init__(self, address = None, port = None):
        super().__int__(address,port)
    def get_data(self):
        self.socket = socket.socket()
        self.socket.connect((self.addr, self.port))
        raw_data = self.socket.recv(4096)
        data = pickle.loads(raw_data)
        self.socket.close()
        return data
    def send_data(self, data):
        self.socket = socket.socket()
        self.socket.connect((self.addr, self.port))
        self.socket.send(pickle.dumps(data))
        self.socket.close()