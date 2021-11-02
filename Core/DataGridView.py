import Core
from tkinter import *


class DataGridView(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, height=120, bg="grey", relief=SUNKEN)
        self.data = None
        self.lb_group = []
        self.btn_group = []
        self.lb_min_width = 20

    def show_data(self, sql_data):
        Core.clear_master(self)
        self.data = sql_data
        self.lb_group = []
        self.btn_group = []
        columns = len(self.data[0])
        rows = len(self.data)-1
        lb_width = self.lb_min_width
        for i in range(columns):
            self.btn_group.append(Button(self, width=int(lb_width*0.8), height=1, text=self.data[0][i], command=lambda j=i: self.btn_header(j)))
            self.lb_group.append(Listbox(self, selectmode=SINGLE, exportselection=0, height=rows, width=lb_width))
            for j in range(rows):
                self.lb_group[i].insert(j+1, self.data[j+1][i])
        for i in range(len(self.lb_group)):
            self.btn_group[i].grid(row=0, column=i)
            self.lb_group[i].bind("<<ListboxSelect>>", self.lb_select)
            self.lb_group[i].bind("<Double-Button-1>", self.lb_double_click)
            self.lb_group[i].grid(row=1, column=i)

    def btn_header(self, arg=None):
        print(self, arg)

    def lb_select(self, arg):
        ar1 = []
        ar2 = []
        index = 0
        for listbox in self.lb_group:
            if len(ar1) == 0:
                if len(listbox.curselection()) > 0:
                    ar1.append(listbox.curselection()[0])
                else:
                    ar1.append(0)
            else:
                if len(listbox.curselection()) > 0:
                    if ar1[0] == listbox.curselection()[0]:
                        ar1.append(listbox.curselection()[0])
                    else:
                        ar2.append(listbox.curselection()[0])
        if len(ar1) < len(ar2):
            index = ar1[0]
        else:
            if len(ar2) > 0:
                index = ar2[0]
            else:
                index = ar1[0]
        for listbox in self.lb_group:
            listbox.select_clear(0, END)
            listbox.select_set(index)
        pass

    def lb_double_click(self, arg):
        # print("DataGridView doubleclick", self, arg)
        pass
