from Models import *
from tkinter import *
from Core import *
import sqlite3

button_col = 0
upper_half_row = 0
lower_half_row = upper_half_row + 1


# commands
def sql_exec(query, master):
    conn = sqlite3.connect("knjizara.db")
    print("Opened database successffully")
    cursor = conn.execute(query)
    sql_data = []
    headers = []
    for header in cursor.description:
        headers.append(header[0])
    sql_data.append(headers)
    for row in cursor:
        cols = []
        for col in row:
            cols.append(col)
        sql_data.append(row)
    conn.commit()
    conn.close()
    data_grid_view(master, 0, 0, sql_data=sql_data)
    pass


def users():
    pass


def books():
    pass


def authors():
    pass


def advanced():
    def adv_exec():
        sql_exec(query.get(), adv_frame)
        pass
    advanced_window = Toplevel()
    advanced_window.grab_set()
    advanced_window.wm_title("Advanced")
    advanced_window.columnconfigure(1, weight=1)
    advanced_window.rowconfigure(1, weight=1)
    Label(advanced_window, text="Query:").grid(row=0, column=0)
    query = StringVar()
    query.set("select * from company")
    Entry(advanced_window, textvariable=query, width=40).grid(row=0, column=1, sticky="nsew")
    Button(advanced_window, text="Execute", command=adv_exec).grid(row=0, column=2)
    adv_frame = Frame(advanced_window, height=200, background="grey")
    adv_frame.grid(row=1, column=0, columnspan=3, sticky="nsew")
    pass


# main server window
prozor = Tk()
prozor.wm_title("Server")
prozor.columnconfigure(1, weight=1)
prozor.rowconfigure(0, weight=1)
prozor.rowconfigure(1, weight=0)
# 14x9
# upper half
#   upper left quarter
upl = Frame(prozor)
Label(upl, text="Show").grid(row=upper_half_row + 0, column=button_col)
Button(upl, text="Users", width=10, command=users).grid(row=upper_half_row + 1, column=button_col)
Button(upl, text="Books", width=10, command=books).grid(row=upper_half_row + 2, column=button_col)
Button(upl, text="Authors", width=10, command=authors).grid(row=upper_half_row + 3, column=button_col)
Button(upl, text="Advanced", width=10, command=advanced).grid(row=upper_half_row + 4, column=button_col)
upl.grid(row=upper_half_row, column=button_col, sticky="nw")
#   upper right quarter
frame = Frame(prozor, width=400, height=200, relief=SUNKEN, background="grey")
frame.grid(row=upper_half_row, column=1, sticky="nesw")
# lower half
Label(prozor, text="Log").grid(row=lower_half_row, column=button_col, sticky="n")
log = Listbox(prozor)
log.grid(row=lower_half_row, column=button_col + 1, sticky="nesw")
prozor.mainloop()
