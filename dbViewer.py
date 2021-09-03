from Models import *
import sqlite3
from tkinter import *
from tkinter.ttk import *


def sql_exec():
    global table, sliders,frame_max_width, frame_max_height
    conn = sqlite3.connect("knjizara.db")
    print("Opened database successffully")
    cursor = conn.execute(query.get())
    data = []
    for row in cursor:
        cols = []
        for col in row:
            cols.append(col)
        data.append(row)
    data_grid_view(frame, frame_max_width, frame_max_height, data)
    print(data)
    print("Executed")
    conn.commit()
    conn.close()


main = Tk()
frame_max_width = int(main.config("width")[3].__str__())
frame_max_height = 50
Label(main, text="Query:").grid(row=0, column=0)
query = StringVar()
Entry(main, textvariable=query, width=90).grid(row=0, column=1)
Button(main, text="Execute", command=sql_exec).grid(row=0, column=2)
frame = Frame(main, height=0, width=frame_max_width)

data_table = StringVar()
table = []
sliders = []
table.append(Listbox(frame, selectmode=SINGLE))
# table = Listbox(frame, selectmode=SINGLE, width=100)
# table.grid(sticky = (N, S, W, E))
frame.grid(row=1, column=0, columnspan=3)
main.mainloop()