import Core
from tkinter import *


class DataGridView(Frame):
    def __init__(self, master=None, click=None, double_click=None):
        Frame.__init__(self, master, height=120, bg="grey", relief=SUNKEN)
        self.data = None
        self.first_time = True
        self.lb_group = []
        self.btn_group = []
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.corner = Frame(self)
        self.tray = Frame(self)
        self.var_scale_v = IntVar()
        self.var_scale_h = IntVar()
        self.scale_v = Scale(self, variable=self.var_scale_v, orient=VERTICAL, showvalue=0, resolution=1, from_=0,
                             to=1000, sliderlength=20, command=self.slider, width=15)

        self.scale_h = Scale(self, variable=self.var_scale_h, orient=HORIZONTAL, showvalue=0, resolution=1, from_=0,
                             to=1000, sliderlength=20, command=self.slider, width=15)
        self.scale_v.grid(row=0, column=1, sticky="ns")
        self.scale_h.grid(row=1, column=0, sticky="ew")
        self.corner.grid(row=1, column=1, sticky="nsew")
        self.tray.place(x=0, y=0)
        self.lb_min_width = 20
        self.click = click
        self.double_click = double_click
        self.bind("<Configure>", self.set_scales)

    def slider(self, arg):
        self.tray.place_configure(x=-self.var_scale_h.get(), y=-self.var_scale_v.get())
        pass

    def show_data(self, sql_data):
        Core.clear_master(self.tray)
        self.data = sql_data
        self.lb_group = []
        self.btn_group = []
        try:
            columns = len(self.data[0])
            rows = len(self.data)-1
            lb_width = self.lb_min_width
            for i in range(columns):
                self.btn_group.append(Button(self.tray, height=1, text=self.data[0][i], relief=FLAT,
                                             command=lambda j=i: self.btn_header(j)))
                self.lb_group.append(Listbox(self.tray, selectmode=SINGLE, exportselection=0, height=rows,
                                             width=lb_width))
                for j in range(rows):
                    self.lb_group[i].insert(j+1, self.data[j+1][i])
            for i in range(len(self.lb_group)):
                self.btn_group[i].grid(row=0, column=i, sticky="ew", padx=0.5)
                self.lb_group[i].bind("<<ListboxSelect>>", self.lb_select)
                self.lb_group[i].bind("<Double-Button-1>", self.lb_double_click)
                self.lb_group[i].grid(row=1, column=i)
            self.set_scales()
        except IndexError:
            pass

    def set_scales(self, arg=None):
        self.tray.update()
        self.scale_h.update()
        self.scale_v.update()
        self.update()
        tray_width = self.tray.winfo_width()
        tray_height = self.tray.winfo_height()
        scale_width = self.scale_h.winfo_width()
        scale_height = self.scale_v.winfo_height()
        horizontal_limit = tray_width - scale_width
        vertical_limit = tray_height - scale_height
        horizontal_slider_size = int(scale_width/tray_width*scale_width)
        vertical_slider_size = int(scale_height/tray_height*scale_height)
        self.scale_h.config(sliderlength=horizontal_slider_size, to=horizontal_limit)
        self.scale_v.config(sliderlength=vertical_slider_size, to=vertical_limit)
        if tray_height < self.winfo_height():
            self.scale_v.config(width=0)
        else:
            self.scale_v.config(width=15)
        if tray_width < self.winfo_width():
            self.scale_h.config(width=0)
        else:
            self.scale_h.config(width=15)

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
        self.index(index)
        pass

    def lb_double_click(self, arg):
        if self.double_click is not None:
            self.double_click(self.lb_group[0].curselection()[0])
        pass

    def index(self, new_index=None):
        if new_index is None:
            try:
                return self.lb_group[0].curselection()[0]
            except IndexError:
                return -1
        else:
            for listbox in self.lb_group:
                listbox.select_clear(0, END)
                listbox.select_set(new_index)