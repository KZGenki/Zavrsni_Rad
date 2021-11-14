import Server
import threading
import time
from tkinter import *

HOST = '127.0.0.1'
PORT = 50000
host_thread = None
execLock = threading.Lock()
listboxLock = threading.Lock()


class Refresher(threading.Thread):
    def __init__(self, command):
        threading.Thread.__init__(self)
        self.command = command
        self.working = True

    def run(self):
        while self.working:
            self.command()
            time.sleep(1)
        update_history(self)
        update_current()


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
        r = Refresher(self.trigger)
        self.services.append(self)
        self.services.append(r)
        r.start()
        s.start_socket()
        while self.working:
            conn, addr = s.wait_for_accept()
            c = Server.ClientData(conn, addr)
            t = Service(name="Service" + str(self.service_id), client_data=c, trigger=self.trigger)
            self.service_id += 1
            self.services.append(t)
            t.start()
            s.start_socket()
            self.trigger()
        s.close_socket()
        r.working = False
        update_history(self)
        update_current()


class Service(threading.Thread):
    def __init__(self, name="Service", client_data=None, trigger=None):
        threading.Thread.__init__(self)
        self.name = name
        self.client_data = client_data
        self.trigger = trigger
        self.status = "Ready"
        self.type = ""
        if client_data is not None:
            self.addr = self.client_data.addr

    def run(self):
        self.status = "Receiving..."
        self.trigger()
        data = self.client_data.get_data()
        self.type = data.__class__.__name__
        self.status = "Executing..."
        self.trigger()
        execLock.acquire()
        # time.sleep(20)  # for testing load
        new_data = Server.exec_data(data)
        execLock.release()
        if new_data != "kill":
            self.status = "Sending..."
            self.trigger()
            self.client_data.send_data(new_data)
        self.client_data.close_connection()
        self.status = "Done."
        update_history(self)
        self.trigger()

    def __str__(self):
        return self.name + " Type:" + self.type + " Status:" + self.status + " Connection:" + str(self.addr)


def start():
    global host_thread, message
    message = "Host pokrenut"
    label.set(message + " Broj aktivnih niti:" + str(threading.active_count()))
    if host_thread is None or not host_thread.working:
        host_thread = Host(trigger=update_current)
        host_thread.working = True
        host_thread.start()
    pass


def stop():
    global message
    if host_thread is not None and host_thread.working:
        message = "Host obustavljen"
        label.set(message + " Broj aktivnih niti:" + str(threading.active_count()))
        host_thread.working = False
        Server.Plug(HOST, PORT)
    update_current()


def on_close():
    stop()
    exit(0)


def update_current():
    label.set(message + " Broj aktivnih niti:" + str(threading.active_count()))
    lb_current.delete(0, END)
    if host_thread is not None:
        for service in host_thread.services:
            if service.is_alive():
                lb_current.insert(END, service)
                lb_current.see(END)


def update_history(service):
    listboxLock.acquire()
    lb_history.insert(END, service)
    lb_history.see(END)
    listboxLock.release()


if __name__ == '__main__':
    server = Tk()
    server.title("Server")
    server.protocol("WM_DELETE_WINDOW", on_close)
    server.rowconfigure(2, weight=1)
    server.columnconfigure(0, weight=1)
    server.columnconfigure(2, weight=1)
    Button(server, text="Start", command=start).grid(row=0, column=0, columnspan=2, sticky="ew")
    Button(server, text="Stop", command=stop).grid(row=0, column=2, columnspan=2, sticky="ew")
    Label(text="Aktivni servisi").grid(row=1, column=0, columnspan=2, sticky="ew")
    Label(text="Gotovi servisi").grid(row=1, column=2, columnspan=2, sticky="ew")
    sb_current = Scrollbar(server)
    sb_history = Scrollbar(server)
    lb_current = Listbox(server, yscrollcommand=sb_current.set, width=50)
    lb_history = Listbox(server, yscrollcommand=sb_history.set, width=50)
    sb_current.config(command=lb_current.yview)
    sb_history.config(command=lb_history.yview)
    lb_current.grid(row=2, column=0, sticky="nsew")
    sb_current.grid(row=2, column=1, sticky="ns")
    lb_history.grid(row=2, column=2, sticky="nsew")
    sb_history.grid(row=2, column=3, sticky="ns")
    label = StringVar()
    message = "Kliknite Start da bi ste pokrenuli Host servis"
    label.set(message)
    Label(server, textvariable=label).grid(row=3, column=0, columnspan=4, sticky="w")
    server.mainloop()
