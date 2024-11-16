from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from classes import User, Book, Admin





class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1350x750")
        self.current_user = None
        self.root.iconbitmap('C:\codecuatuan\LMS_basic\picture\logo.ico')
        mainFrame = Frame(self.root)
        mainFrame.pack()
        topFrame = Frame(mainFrame, width=1350, height=70, bg='#f8f8f8', relief=SUNKEN, borderwidth=2)
        topFrame.pack(side=TOP, fill=X)





if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()