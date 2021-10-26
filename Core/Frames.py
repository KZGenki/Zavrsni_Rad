from tkinter import *


class Login(Frame):
    def __init__(self, cmd_login, cmd_new_user, cmd_guest, master=None):
        Frame.__init__(self, master)
        self.grid()
        # username
        self.lblUsername = Label(self, text="Korisnicko ime")
        self.lblUsername.grid(row=0, column=0)
        self.varUsername = StringVar()
        self.entUsername = Entry(self, textvariable=self.varUsername, width=30)
        self.grid(row=1, column=0)
        # password
        self.lblPassword = Label(self, text="Lozinka")
        self.lblPassword.grid(row=2, column=0)
        self.varPassword = StringVar()
        self.entPassword = Entry(self, textvariable=self.varPassword, width=30, show="*")
        self.entPassword.grid(row=3, column=0)
        # buttons
        self.btnLogin = Button(self, text="Uloguj se")
        self.btnLogin.grid(row=3, column=0)
        self.btnNewUser = Button(self, text="Novi nalog")
        self.btnNewUser.grid(row=4, column=0)
        self.btnGuest = Button(self, text="Nastavi kao gost")
        self.btnGuest.grid(row=5, column=0)
