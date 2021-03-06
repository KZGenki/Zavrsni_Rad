from Core import *
# import Operations
import Client as Operations


class MainFrame(Frame):
    def __init__(self, master=None, user=None):
        Frame.__init__(self, master, padx=5, pady=5)
        self.user = user
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.top_row = Frame(self)
        if self.user.type == 0:
            self.btnLogout = Button(self, text="Nazad", command=self.login_screen)
            self.lblMessage = Label(self, text="Dobrodošli")
        else:
            self.btnLogout = Button(self, text="Odjava", command=self.login_screen)
            self.lblMessage = Label(self, text="Dobrodošli, " + self.user.username)
        self.btnLogout.grid(row=0, column=0, sticky="w")
        self.lblMessage.grid(row=0, column=1, sticky="w")
        self.top_row.grid(row=0, column=2, sticky="ew")
        if self.user.type == 3:
            self.workspace = Core.AdminMainFrame(self, user)
        elif self.user.type == 2:
            self.workspace = Core.OperatorFrame(self)
        else:
            self.workspace = Workspace(self)
        self.workspace.grid(row=1, column=0, columnspan=3, sticky="nsew")

    def login_screen(self):
        Core.clear_master(self.master)
        LoginFrame(self.master).grid()
        pass


class LoginFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, padx=5, pady=5)
        self.errLbl = Label(self)
        # self.grid()
        # username
        self.lblUsername = Label(self, text="Korisničko ime")
        self.lblUsername.grid(row=0, column=0)
        self.varUsername = StringVar()
        self.entUsername = Entry(self, textvariable=self.varUsername)
        self.entUsername.grid(row=1, column=0, sticky="ew")
        # password
        self.lblPassword = Label(self, text="Lozinka")
        self.lblPassword.grid(row=2, column=0)
        self.varPassword = StringVar()
        self.entPassword = Entry(self, textvariable=self.varPassword, show="*")
        self.entPassword.grid(row=3, column=0, sticky="ew")
        # buttons
        self.btnLogin = Button(self, text="Uloguj se", command=self.tk_login, width=30)
        self.btnLogin.grid(row=4, column=0)
        self.btnNewUser = Button(self, text="Novi nalog", command=self.tk_new_user, width=30)
        self.btnNewUser.grid(row=5, column=0)
        self.btnGuest = Button(self, text="Nastavi kao gost", command=self.tk_guest, width=30)
        self.btnGuest.grid(row=6, column=0)

    def tk_login(self):
        self.tk_check_user_pass()
        result = Operations.login(self.varUsername.get(), self.varPassword.get())
        if isinstance(result, Core.LoginError):
            self.tk_error_label(result)
        else:
            self.main_frame(result)

    def tk_new_user(self):
        self.tk_check_user_pass()
        result = Operations.new_user(self.varUsername.get(), self.varPassword.get())
        if isinstance(result, Core.LoginError):
            self.tk_error_label(result)
        else:
            self.main_frame(result)

    def tk_guest(self):
        result = Operations.login()
        if isinstance(result, Core.LoginError):
            self.tk_error_label(result)
        else:
            self.main_frame(result)

    def main_frame(self, result):
        Core.clear_master(self.master)
        MainFrame(self.master, user=result).grid(sticky="nsew")

    def tk_check_user_pass(self):
        if self.varUsername.get() == "":
            raise Core.LoginError("Korisničko polje ne sme biti prazno")
        if self.varPassword.get() == "":
            raise Core.LoginError("Polje za lozinku ne sme biti prazno")

    def tk_error_label(self, message):
        self.errLbl.destroy()
        self.errLbl = Label(self, text=message)
        self.errLbl.grid(row=7, column=0)


if __name__ == '__main__':
    MainWindow = Tk()
    MainWindow.wm_title("Knjižara")
    MainWindow.rowconfigure(0, weight=1)
    MainWindow.columnconfigure(0, weight=1)
    LoginFrame(MainWindow).grid(row=0, column=0, sticky="nsew")
    MainWindow.mainloop()
