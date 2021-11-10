import socket
import pickle


class DataClient:
    def __init__(self, address, port):
        self.addr = address
        self.port = port
        self.socket = None

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
