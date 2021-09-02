import sqlite3
from tkinter import *
from tkinter.ttk import *


def lb_select(self):
    global table
    ar1 = []
    ar2 = []
    index = 0
    for listbox in table:
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
    for listbox in table:
        listbox.select_clear(0,END)
        listbox.select_set(index)

def clear_frame():
    list = frame.grid_slaves()
    for l in list:
        l.destroy()

def sql_exec():
    global table
    conn = sqlite3.connect("knjizara.db")
    print("Opened database successffully")
    cursor = conn.execute(query.get())
    data = []
    clear_frame()
    table = []
    for row in cursor:
        cols = []
        #table.insert(0,row)
        for col in row:
            cols.append(col)
        data.append(row)
    for i in range(len(data[0])):
        table.append(Listbox(frame, selectmode=SINGLE, exportselection=0))
        for j in range(len(data)):
            table[i].insert(j, data[j][i])
    for i in range(len(table)):
        table[i].bind("<<ListboxSelect>>", lb_select)
        table[i].grid(row=1, column=i)
    print(data)
    print("Executed")
    conn.commit()
    conn.close()

main = Tk()
Label(main, text = "Query:").grid(row=0, column=0)
query = StringVar()
Entry(main, textvariable=query, width=90).grid(row=0, column=1)
Button(main,text="Execute", command=sql_exec).grid(row=0,column=2)
frame = Frame(main)
data_table=StringVar()
table = []
table.append(Listbox(frame, selectmode=SINGLE))
#table = Listbox(frame, selectmode=SINGLE, width=100)
#table.grid(sticky = (N, S, W, E))
frame.grid(row=1, column=0, columnspan=3)
main.mainloop()