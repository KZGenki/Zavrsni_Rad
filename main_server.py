import Server
import threading
from tkinter import *

HOST = '127.0.0.1'
PORT = 50000


class Host(threading.Thread):
    def __init__(self, name="Host", trigger=None):
        threading.Thread.__init__(self)
        self.name = name
        self.trigger = trigger
        self.services = []
        self.service_id = 0
        self.working = True

    def run(self):
        print("Host has started")
        s = Server.ServerData(HOST, PORT, Server.exec_data)
        s.start_socket()
        while self.working:
            if s.wait_for_accept():
                t = Service(name="Service" + str(self.service_id), server_data=s, trigger=self.trigger)
                self.service_id += 1
                self.services.append(t)
                t.start()
                # s = Server.ServerData(HOST, PORT, Server.exec_data)
                s.start_socket()
                self.trigger()

        pass


class Service(threading.Thread):
    def __init__(self, name="Service", server_data=None, trigger=None):
        threading.Thread.__init__(self)
        self.name = name
        self.server_data = server_data
        self.trigger = trigger
        self.status = "Ready"
        if server_data is not None:
            self.addr = self.server_data.addr

    def run(self):
        print(str(self) + " has started")
        self.status = "Receiving..."
        self.trigger()
        data = self.server_data.get_data()
        self.status = "Executing..."
        self.trigger()
        new_data = Server.exec_data(data)
        self.status = "Sending..."
        self.trigger()
        self.server_data.send_data(new_data)
        self.server_data.close_connection()
        self.status = "Done."
        self.trigger()
        pass

    def __str__(self):
        return self.name + " Status:" + self.status + " Connection:" + str(self.addr)


def start():
    global host_thread
    label.set("Host pokrenut")
    host_thread = Host(trigger=update_listbox)
    host_thread.working = True
    host_thread.start()
    pass


def stop():
    label.set("Host obustavljen")
    host_thread.working = False

    pass


def update_listbox():
    lb.delete(0, END)
    if host_thread is not None:
        for service in host_thread.services:
            lb.insert(END, service)
    pass


host_thread = None
server = Tk()
server.rowconfigure(1, weight=1)
server.columnconfigure(1, weight=1)
server.columnconfigure(2, weight=1)
Button(server, text="Start", command=start).grid(row=0, column=0, columnspan=2, sticky="ew")
Button(server, text="Stop", command=stop).grid(row=0, column=2, columnspan=2, sticky="ew")
sb = Scrollbar(server)
lb = Listbox(server, yscrollcommand=sb.set)
sb.config(command=lb.yview)
lb.grid(row=1, column=0, columnspan=3, sticky="nsew")
sb.grid(row=1, column=3, sticky="ns")
label = StringVar()
label.set("Kliknite Start da bi ste pokrenuli Host servis")
Label(server, textvariable=label).grid(row=2, column=0, columnspan=4, sticky="w")
server.mainloop()
