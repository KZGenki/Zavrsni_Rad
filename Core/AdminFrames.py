from tkinter import *

import Core


class AdminFrame(Frame):
    def __init__(self, master=None, user=None):
        Frame.__init__(self, master)
        self.user = user
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        # buttons
        self.btn_user = Button(self.master.top_row, text="Korisnik", command=self.tk_user, relief=SUNKEN)
        self.btn_user.grid(row=0, column=0, sticky="e")
        self.btn_operator = Button(self.master.top_row, text="Operator", command=self.tk_operator)
        self.btn_operator.grid(row=0, column=1, sticky="e")
        self.btn_advanced = Button(self.master.top_row, text="Napredno", command=self.tk_advanced)
        self.btn_advanced.grid(row=0, column=2, sticky="e")

        self.working_frame = Core.Workspace(self)
        self.working_frame.grid(row=1, column=0, sticky="nsew")

    def tk_user(self):
        if self.btn_user["relief"] != SUNKEN:
            self.working_frame.destroy()
            self.working_frame = Core.Workspace(self)
            self.working_frame.grid(sticky="nsew")
            self.raise_buttons()
            self.btn_user["relief"] = SUNKEN

    def tk_advanced(self):
        if self.btn_advanced["relief"] != SUNKEN:
            self.working_frame.destroy()
            self.working_frame = Core.AdvancedFrame(self)
            self.working_frame.grid(sticky="nsew")
            self.raise_buttons()
            self.btn_advanced["relief"] = SUNKEN

    def tk_operator(self):
        if self.btn_operator["relief"] != SUNKEN:
            self.working_frame.destroy()
            self.working_frame = OperatorFrame(self)
            self.working_frame.grid(sticky="nsew")
            self.raise_buttons()
            self.btn_operator["relief"] = SUNKEN

    def raise_buttons(self):
        self.btn_user["relief"] = RAISED
        self.btn_advanced["relief"] = RAISED
        self.btn_operator["relief"] = RAISED


class AdvancedFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)


class OperatorFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)