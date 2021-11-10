from Server import *

HOST = '127.0.0.1'
PORT = 50007

s = ServerData(HOST, PORT)
while True:
    s.wait_for_accept()
    data = s.get_data()
    # do something with data
    exec_data(data)
    s.send_data(data)
    s = ServerData(HOST, PORT)
