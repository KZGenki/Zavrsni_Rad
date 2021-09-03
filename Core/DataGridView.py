from tkinter import *

lb_group = []


def lb_select(self):
    global lb_group
    ar1 = []
    ar2 = []
    index = 0
    for listbox in lb_group:
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
    for listbox in lb_group:
        listbox.select_clear(0, END)
        listbox.select_set(index)


def clear_master(master):
    slaves = master.grid_slaves()
    for slave in slaves:
        slave.destroy()


def data_grid_view(master, max_width, max_height, data):
    global lb_group
    lb_group = []
    clear_master(master)
    lb_min_width = 20
    columns = len(data[0])
    rows = len(data)
    lb_width = int(max_width/columns)
    if lb_width < lb_min_width:
        lb_width = lb_min_width
    for i in range(columns):
        lb_group.append(Listbox(master, selectmode=SINGLE, exportselection=0, height=rows, width=lb_width))
        for j in range(rows):
            lb_group[i].insert(j, data[j][i])
    #for lb in lb_group:
    #    lb.bind("<<ListboxSelect>>", lb_select)
    #    lb.grid(row=1, column=i)
    for i in range(len(lb_group)):
        lb_group[i].bind("<<ListboxSelect>>", lb_select)
        lb_group[i].grid(row=1, column=i)
