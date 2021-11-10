import socket
import pickle


class ClientData:
    def __init__(self, address, port):
        self.addr = address
        self.port = port
        self.socket = None

    def wait_for_connect(self):
        self.socket = socket.socket()
        self.socket.connect((self.addr, self.port))
        return True

    def get_data(self):
        raw_data = self.socket.recv(20000)
        data = pickle.loads(raw_data)
        return data

    def send_data(self, data):
        self.socket.send(pickle.dumps(data))

    def close(self):
        self.socket.close()

    def send_receive(self, data):
        self.socket = socket.socket()
        self.socket.connect((self.addr, self.port))
        self.socket.send(pickle.dumps(data))
        raw_data = self.socket.recv(20000)
        data = pickle.loads(raw_data)
        return data
        self.socket.close()
