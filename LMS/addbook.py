from tkinter import *
from tkinter import messagebox
import sqlite3
con =sqlite3.connect('library.db')
cur = con.cursor()
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
############INPUT##############
        #name
        self.lbl_name = Label(self.bottom_frame, text='Name: ', font='Arial 15 bold',bg='#D4BDAC')
        self.lbl_name.place(x=40, y=40)
        self.entry_name = Entry(self.bottom_frame, width=30,bd=4)
        self.entry_name.insert(0,'Please enter a book name')
        self.entry_name.place(x=150, y=45)
        #author
        self.lbl_author = Label(self.bottom_frame, text='Author: ', font='Arial 15 bold', bg='#D4BDAC')
        self.lbl_author.place(x=40, y=80)
        self.entry_author = Entry(self.bottom_frame, width=30, bd=4)
        self.entry_author.insert(0, 'Please enter author name')
        self.entry_author.place(x=150, y=85)
        #button
        self.button = Button(self.bottom_frame, text='ADD', command=self.addBook)
        self.button.place(x=270,y=125)

    def addBook(self):
        name = self.entry_name.get()
        author = self.entry_author.get()
        if name and author !="":
            try:
                query="INSERT INTO 'books' (book_name, book_author) VALUES(?, ?)"
                cur.execute(query, (name, author))
                con.commit()
                messagebox.showinfo('Success', 'Book added successfully', icon='info')
            except:
                messagebox.showinfo('Error', 'Cant add to the database', icon='warning')
        else:
            messagebox.showinfo('Error', 'Please fill in all fields', icon='warning')