import socket
import pickle


class ServerData:
    def __init__(self, address, port):
        self.addr = address
        self.port = port
        self.socket = None

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
        print("Gor connection from ", addr)
        conn.send(pickle.dumps(data))  # possible error here
        conn.close()
        self.socket.close()