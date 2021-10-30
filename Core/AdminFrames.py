from tkinter import *

import Core


class AdminFrame(Frame):
    def __init__(self, master=None, user=None):
        Frame.__init__(self, master)
        self.user = user
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        # buttons
        self.button_row = Frame(self.master.top_row)
        self.btn_user = Button(self.button_row, text="Korisnik", command=self.tk_user, relief=SUNKEN)
        self.btn_user.grid(row=0, column=0, sticky="e")
        self.btn_advanced = Button(self.button_row, text="Napredno", command=self.tk_advanced)
        self.btn_advanced.grid(row=0, column=1, sticky="e")
        self.button_row.grid(row=0, column=3, sticky="ne")
        self.working_frame = Core.Workspace(self)
        self.working_frame.grid(row=1, column=0, sticky="nsew")

    def tk_user(self):
        if self.btn_user["relief"] != SUNKEN:
            self.working_frame.destroy()
            self.working_frame = Core.Workspace(self)
            self.working_frame.grid(sticky="nsew")
            self.btn_user["relief"] = SUNKEN
            self.btn_advanced["relief"] = RAISED
        pass

    def tk_advanced(self):
        if self.btn_advanced["relief"] != SUNKEN:
            self.working_frame.destroy()
            self.working_frame = Core.Frame(self, bg="red")
            self.working_frame.grid(sticky="nsew")
            self.btn_user["relief"] = RAISED
            self.btn_advanced["relief"] = SUNKEN
        pass