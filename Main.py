from tkinter import *
from Core import *

errLbl = None
user = None
loginFrame = None



def login_screen():
    global loginFrame
    loginFrame = LoginFrame(MainWindow)
    loginFrame.grid()


MainWindow = Tk()
MainWindow.wm_title("Knjizara")
login_screen()
MainWindow.mainloop()
