from Models import *
from tkinter import *

button_col = 0
upper_half_row = 0
lower_half_row = upper_half_row + 1

# commands


def users():
    pass


def books():
    pass


def authors():
    pass


# main server window
prozor = Tk()
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
upl.grid(row=upper_half_row, column=button_col, sticky="nw")
#   upper right quarter
frame = Frame(prozor, width=400, height=200, relief=SUNKEN, background="grey")
frame.grid(row=upper_half_row, column=1, sticky="nesw")
# lower half
Label(prozor, text="Log").grid(row=lower_half_row, column=button_col, sticky="n")
log = Listbox(prozor)
log.grid(row=lower_half_row, column=button_col + 1, sticky="nesw")
prozor.mainloop()
