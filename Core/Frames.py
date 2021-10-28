from tkinter import *

import Core


class MainFrame(Frame):
    def __init__(self, master=None, user=None):
        Frame.__init__(self, master)
        self.master = master
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        if user.username == "Guest":
            self.btnLogout = Button(self, text="Nazad", command=self.login_screen)
            self.lblMessage = Label(self, text="Dobrodosli")
        else:
            self.btnLogout = Button(self, text="Odjava", command=self.login_screen)
            self.lblMessage = Label(self, text="Dobrodosli, " + user.username)
        self.btnLogout.grid(row=0, column=0)
        self.lblMessage.grid(row=0, column=1)

    def login_screen(self):
        Core.clear_master(self.master)
        LoginFrame(self.master).grid()
        pass


class LoginFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.errLbl = Label(self)
        self.master = master
        # self.grid()
        # username
        self.lblUsername = Label(self, text="Korisnicko ime")
        self.lblUsername.grid(row=0, column=0)
        self.varUsername = StringVar()
        self.entUsername = Entry(self, textvariable=self.varUsername, width=30)
        self.entUsername.grid(row=1, column=0)
        # password
        self.lblPassword = Label(self, text="Lozinka")
        self.lblPassword.grid(row=2, column=0)
        self.varPassword = StringVar()
        self.entPassword = Entry(self, textvariable=self.varPassword, width=30, show="*")
        self.entPassword.grid(row=3, column=0)
        # buttons
        self.btnLogin = Button(self, text="Uloguj se", command=self.tk_login, width=30)
        self.btnLogin.grid(row=4, column=0)
        self.btnNewUser = Button(self, text="Novi nalog", command=self.tk_new_user, width=30)
        self.btnNewUser.grid(row=5, column=0)
        self.btnGuest = Button(self, text="Nastavi kao gost", command=self.tk_guest, width=30)
        self.btnGuest.grid(row=6, column=0)

    def tk_login(self):
        try:
            self.tk_check_user_pass()
            result = Core.login(self.varUsername.get(), self.varPassword.get())
        except Core.LoginError as e:
            self.tk_error_label(e)
        else:
            Core.clear_master(self.master)
            MainFrame(self.master, user=result).grid()
        pass

    def tk_new_user(self):
        try:
            self.tk_check_user_pass()
            result = Core.new_user(self.varUsername.get(), self.varPassword.get())
        except Core.LoginError as e:
            self.tk_error_label(e)
        else:
            Core.clear_master(self.master)
            MainFrame(self.master, user=result).grid()
        pass

    def tk_guest(self):
        try:
            result = Core.login()
        except Core.LoginError as e:
            self.tk_error_label(e)
        else:
            Core.clear_master(self.master)
            MainFrame(self.master, user=result).grid()

    def tk_check_user_pass(self):
        if self.varUsername.get() == "":
            raise Core.LoginError("Korisnicko polje ne sme biti prazno")
        if self.varPassword.get() == "":
            raise Core.LoginError("Polje za lozinku ne sme biti prazno")

    def tk_error_label(self, message):
        self.errLbl.destroy()
        self.errLbl = Label(self, text=message)
        self.errLbl.grid(row=7, column=0)
