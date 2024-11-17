from tkinter import *
from tkinter import messagebox
import sqlite3

#A Toplevel widget is used to create a window on top of all other windows
class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750")
        self.title("Add Book")
        self.resizable(False,False)

#########################frames##################
        #top frame
        self.top_frame = Frame(self, height=150,bg='white')
        self.top_frame.pack(fill=X)
        #bottom frame
        self.bottom_frame = Frame(self, height=600, bg='#D4BDAC')
        self.bottom_frame.pack(fill=X)
        #heading, image
        self.top_image = PhotoImage(file='pictures/addbook.png')
        self.top_image_lbl = Label(self.top_frame, image=self.top_image, bg='white')
        self.top_image_lbl.pack()
        self.heading = Label(self.top_frame, text=' Add Book ', font='Arial 22 bold', bg='white')
        self.heading.pack()

