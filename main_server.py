import Server

HOST = '127.0.0.1'
PORT = 50007

while True:
    s = Server.ServerData(HOST, PORT, Server.exec_data)
    s.receive_send()
