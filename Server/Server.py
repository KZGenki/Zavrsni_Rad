import socket
import pickle


class ServerData:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.socket = None
        self.conn = None
        self.addr = None

    def wait_for_accept(self):
        self.socket = socket.socket()
        self.socket.bind((self.address, self.port))
        self.socket.listen(1)
        self.conn, self.addr = self.socket.accept()
        return True

    def get_data(self):
        print("Got connection from ", self.addr)
        raw_data = self.conn.recv(4096)
        data = pickle.loads(raw_data)
        self.conn.close()
        self.socket.close()
        return data

    def send_data(self, data):
        self.socket = socket.socket()
        self.socket.bind((self.address, self.port))
        self.socket.listen(1)
        conn, addr = self.socket.accept()
        print("Got connection from ", addr)
        conn.send(pickle.dumps(data))  # possible error here
        conn.close()
        self.socket.close()
