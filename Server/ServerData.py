import socket
import pickle


class ServerData:
    def __init__(self, address, port, exec_data):
        self.address = address
        self.port = port
        self.exec_data = exec_data
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
        return data

    def send_data(self, data):
        print("Got connection from ", self.addr)
        self.conn.send(pickle.dumps(data))  # possible error here

    def close(self):
        self.conn.close()
        self.socket.close()

    def receive_send(self):
        self.socket = socket.socket()
        self.socket.bind((self.address, self.port))
        self.socket.listen(1)
        self.conn, self.addr = self.socket.accept()
        print("Got connection from ", self.addr)
        raw_data = self.conn.recv(4096)
        data = pickle.loads(raw_data)
        new_data = self.exec_data(data)
        self.conn.send(pickle.dumps(new_data))
        self.conn.close()
        self.socket.close()

