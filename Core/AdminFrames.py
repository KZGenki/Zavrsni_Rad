from tkinter import *
import sqlite3
import Core


class AdminMainFrame(Frame):
    def __init__(self, master=None, user=None):
        Frame.__init__(self, master)
        self.user = user
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        # buttons
        self.btn_user = Button(self.master.top_row, text="Korisnik", command=self.tk_user)
        self.btn_user.grid(row=0, column=0, sticky="e")
        self.btn_operator = Button(self.master.top_row, text="Operator", command=self.tk_operator)
        self.btn_operator.grid(row=0, column=1, sticky="e")
        self.btn_admin = Button(self.master.top_row, text="Admin", command=self.tk_admin)
        self.btn_admin.grid(row=0, column=2, sticky="e")
        self.btn_advanced = Button(self.master.top_row, text="Napredno", command=self.tk_advanced)
        self.btn_advanced.grid(row=0, column=3, sticky="e")

        self.working_frame = Frame(self)  # Core.Workspace(self)
        # self.working_frame.grid(row=1, column=0, sticky="nsew")
        self.tk_admin()

    def tk_user(self):
        if self.btn_user["relief"] != SUNKEN:
            self.working_frame.destroy()
            self.working_frame = Core.Workspace(self)
            self.working_frame.grid(row=1, column=0, sticky="nsew")
            self.raise_buttons()
            self.btn_user["relief"] = SUNKEN

    def tk_advanced(self):
        if self.btn_advanced["relief"] != SUNKEN:
            self.working_frame.destroy()
            self.working_frame = Core.AdvancedFrame(self)
            self.working_frame.grid(row=1, column=0, sticky="nsew")
            self.raise_buttons()
            self.btn_advanced["relief"] = SUNKEN

    def tk_operator(self):
        if self.btn_operator["relief"] != SUNKEN:
            self.working_frame.destroy()
            self.working_frame = Core.OperatorFrame(self)
            self.working_frame.grid(row=1, column=0, sticky="nsew")
            self.raise_buttons()
            self.btn_operator["relief"] = SUNKEN

    def tk_admin(self):
        if self.btn_admin["relief"] != SUNKEN:
            self.working_frame.destroy()
            self.working_frame = AdminFrame(self)
            self.working_frame.grid(row=1, column=0, sticky="nsew")
            self.raise_buttons()
            self.btn_admin["relief"] = SUNKEN

    def raise_buttons(self):
        self.btn_user["relief"] = RAISED
        self.btn_advanced["relief"] = RAISED
        self.btn_operator["relief"] = RAISED
        self.btn_admin["relief"] = RAISED


class AdvancedFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        Label(self, text="Query").grid(row=0, column=0, sticky="w")
        self.varQuery = StringVar()
        Entry(self, textvariable=self.varQuery, width=40).grid(row=0, column=1, sticky="ew")
        Button(self, text="Execute", command=self.query).grid(row=0, column=2, sticky="e")
        self.DataGridView = Core.DataGridView(self)
        self.DataGridView.grid(row=1, column=0, columnspan=3, sticky="nsew")

    def query(self):
        conn = sqlite3.connect("knjizara.db")
        cursor = conn.execute(self.varQuery.get())
        data = []
        headers = []
        try:
            for header in cursor.description:
                headers.append(header[0])
        except:
            conn.commit()
            conn.close()
        else:
            data.append(headers)
            for row in cursor:
                cols = []
                for col in row:
                    cols.append(col)
                data.append(row)
            conn.commit()
            conn.close()
            self.DataGridView.show_data(data)
        pass


class AdminFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)