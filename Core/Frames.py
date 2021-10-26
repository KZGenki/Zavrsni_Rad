from tkinter import *


class Main(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.leftHalf = Frame(self)
        # left half
        self.leftTopQuarter = Frame(self.leftHalf)
        Label(self.leftTopQuarter, text="Hello, user").grid(row=0, column=0)
        self.leftTopQuarter.grid(row=0, column=0)
        self.leftBottomQuarter = Frame(self.leftHalf)
        Label(self.leftBottomQuarter, text="Bottom quarter").grid(row=0, column=0)
        self.leftBottomQuarter.grid(row=1, column=0)
        self.leftHalf.grid(row=0, column=0)
        self.rightHalf = Frame(self)
        # right half
        Label(self.rightHalf, text="Right Half").grid(row=0, column=0, rowspan=2)
        self.rightHalf.grid(row=0, column=1)


class Login(Frame):
    def __init__(self, cmd_login, cmd_new_user, cmd_guest, master=None):
        Frame.__init__(self, master)
        # self.grid()
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
        self.btnLogin = Button(self, text="Uloguj se", command=cmd_login)
        self.btnLogin.grid(row=3, column=0)
        self.btnNewUser = Button(self, text="Novi nalog", command=cmd_new_user)
        self.btnNewUser.grid(row=4, column=0)
        self.btnGuest = Button(self, text="Nastavi kao gost", command=cmd_guest)
        self.btnGuest.grid(row=5, column=0)
