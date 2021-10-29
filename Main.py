from tkinter import *
from Core import *

if __name__ == '__main__':
    MainWindow = Tk()
    MainWindow.wm_title("Knjizara")
    MainWindow.rowconfigure(0, weight=1)
    MainWindow.columnconfigure(0, weight=1)
    LoginFrame(MainWindow).grid(row=0, column=0, sticky="nsew")
    MainWindow.mainloop()
