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


class ClientData:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr

    def get_data(self):
        raw_data = self.conn.recv(4096)
        data = pickle.loads(raw_data)
        return data

    def send_data(self, data):
        self.conn.send(pickle.dumps(data))

    def close_connection(self):
        self.conn.close()

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
        self.socket.listen(5)

    def wait_for_accept(self):
        conn, addr = self.socket.accept()
        return conn, addr

    def close_socket(self):
        self.socket.close()

