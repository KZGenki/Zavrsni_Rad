import socket
import pickle


class Kill:
    def __init__(self):
        pass


class Plug:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.s = socket.socket()
        self.s.connect((self.address, self.port))
        self.s.send(pickle.dumps(Kill()))
        self.s.close()


class ServerData:
    def __init__(self, address, port, exec_data=None):
        self.address = address
        self.port = port
        self.exec_data = exec_data
        self.socket = None
        self.conn = None
        self.addr = None

    def start_socket(self):
        self.socket = socket.socket()
        self.socket.bind((self.address, self.port))

    def wait_for_accept(self):
        self.socket.listen(1)
        self.conn, self.addr = self.socket.accept()
        return True

    def get_data(self):
        raw_data = self.conn.recv(4096)
        data = pickle.loads(raw_data)
        return data

    def send_data(self, data):
        self.conn.send(pickle.dumps(data))  # possible error here

    def close_connection(self):
        self.conn.close()

    def close_socket(self):
        self.socket.close()

