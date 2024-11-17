from tkinter import *
from tkinter import ttk
from datetime import datetime
from classes import User, Book, Admin
import sqlite3
#are used to establish a connection to a SQLite database and create a cursor object for executing SQL commands. Here's a detailed explanation:


con=sqlite3.connect('library.db')
cur=con.cursor()



class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root


        #frame for app
        mainFrame = Frame(self.root)
        mainFrame.pack()
        #topFrame
        #SUNKEN pressed inward, creating a visual impression of depth.
        topFrame = Frame(mainFrame, width=1350, height=70, bg='#f8f8f8', relief=SUNKEN, borderwidth=2)
        topFrame.pack(side=TOP, fill=X)
        #centerFrame
        centerFrame = Frame(mainFrame, width=1350, relief=RIDGE, bg='#D4BDAC', height=680)
        #RIDGE creates a raised border that gives a 3D effect.
        centerFrame.pack(side=TOP)
        #CENTER Left Frame
        centerLeftFrame = Frame(centerFrame, width=900, height=700, bg='#D4BDAC', borderwidth=2, relief=SUNKEN)
        centerLeftFrame.pack(side=LEFT)
        #CENTER Right Frame
        centerRightFrame = Frame(centerFrame, width=450, height=700, bg='#D4BDAC', borderwidth=2, relief=SUNKEN)
        centerRightFrame.pack()


        #search bar
        search_bar = LabelFrame(centerRightFrame, width=440, height=75, text='Search Box', bg="#FFF1DB")
        search_bar.pack(fill=BOTH)
        self.searchLabel = Label(search_bar, text="Search :", font='arial 12 bold', bg="#FFF1DB")
        self.searchLabel.grid(row=0, column=0, pady=10)
        self.searchEntry = Entry(search_bar, font='arial 12', width=25, bd=5)
        self.searchEntry.grid(row=0, column=1, columnspan=3,padx=20,  pady=10)
        self.searchBtn = Button(search_bar, text='Search', font='arial 12 bold', bg='#D4BDAC')
        self.searchBtn.grid(row=0, column=4)

        #list bar
        list_bar = LabelFrame(centerRightFrame, width=440, height=175, text='List Box', bg="#88C273")
        list_bar.pack(fill=BOTH)
        self.label_list = Label(list_bar, text='Sort By', font='arial 16 bold', fg='#FFFFFF',bg='#88C273')
        self.label_list.grid(row=0, column=2)

        self.listChoice = IntVar()
        self.radioBtn1 = Radiobutton(list_bar,text='All books', var=self.listChoice, value=1, bg='#88C273' )
        self.radioBtn2 = Radiobutton(list_bar,text='In Library', var=self.listChoice, value=2, bg='#88C273' )
        self.radioBtn3 = Radiobutton(list_bar,text='Borrowed Books', var=self.listChoice, value=3, bg='#88C273' )
        self.radioBtn1.grid(row=1, column=0)
        self.radioBtn2.grid(row=1, column=1)
        self.radioBtn3.grid(row=1, column=2)
        self.btnList = Button(list_bar,text='List Books', bg='#2488ff',fg='white', font='arial 12')
        self.btnList.grid(row=1, column=3, padx=40, pady=10)


        #TITLE AND IMG
        image_bar = Frame(centerRightFrame, width=440, height=350)
        image_bar.pack(fill=BOTH)
        self.title_right = Label(image_bar, text='Welcome to our Library', font='arial 16 bold')
        self.title_right.grid(row=0)
        self.img_library =PhotoImage(file='pictures/library.png', height=300, width=440)
        self.img_label = Label(image_bar, image=self.img_library)
        self.img_label.grid(row=1)


#####################TOOL BAR ##########################
        #addbook
        self.addBookPic=PhotoImage(file='pictures/addbook.png', )
        self.btnBook = Button(topFrame, text='Add Book', image=self.addBookPic, compound=LEFT, font='arial 12 bold')
        self.btnBook.pack(side=LEFT,padx=5)
        #addmember
        self.addMemberPic=PhotoImage(file='pictures/addmember.png')
        self.btnMember = Button(topFrame, text='Add Member', image=self.addMemberPic, compound=LEFT, font='arial 12 bold')
        self.btnMember.pack(side=LEFT)
        #givebook
        self.btnGiveBook = Button(topFrame, text='Give Book', font='arial 12 bold',pady=16)
        self.btnGiveBook.pack(side=LEFT,padx=5)

####################CENTER LEFT BODY #####################
        #body
        self.header = ttk.Notebook(centerLeftFrame, width=900, height=660)
        self.header.pack()
        self.tab1_icon = PhotoImage(file='pictures/libraryicon.png')
        self.tab2_icon = PhotoImage(file='pictures/statistic.png')
        self.tab1 = ttk.Frame(self.header)
        self.tab2 = ttk.Frame(self.header)
        self.header.add(self.tab1, text='Library Management', image=self.tab1_icon, compound=LEFT)
        self.header.add(self.tab2, text='Statistics', image=self.tab2_icon, compound=LEFT)

####################TAB1############################
        #list books
        self.list_books = Listbox(self.tab1, width=40, height=30, borderwidth=3, font='times 12 bold')
        self.scrollBar = Scrollbar(self.tab1, orient=VERTICAL)

        # Place the Listbox in the grid at row 0, column 0 with padding and stick it to the north
        self.list_books.grid(row=0, column=0, padx=(10, 0), pady=10, sticky=N)

        # Configure the Scrollbar to control the Listbox's yview
        self.scrollBar.config(command=self.list_books.yview)

        # Configure the Listbox to update the Scrollbar
        self.list_books.config(yscrollcommand=self.scrollBar.set)

        # Place the Scrollbar in the grid at row 0, column 0, and stretch it to the north, south, and east
        self.scrollBar.grid(row=0, column=0, sticky=N + S + E)

        #list details
        self.list_details=Listbox(self.tab1, width=80, height=30, bd=5, font='times 12 bold')
        self.list_details.grid(row=0, column=1, padx=(10, 0), pady=10, sticky=N)

######################TAB2:STATISTICS############################
        self.lbl_book_count=Label(self.tab2,text="", pady=20, font='times 14 bold')
        self.lbl_book_count.grid(row=0)

        self.lbl_member_count=Label(self.tab2,text="", pady=20, font='times 14 bold')
        self.lbl_member_count.grid(row=1, sticky=W)

        self.lbl_taken_count=Label(self.tab2, text="", pady=20, font='times 14 bold')
        self.lbl_taken_count.grid(row=2, sticky=W)


def main():
    root = Tk()
    app = LibraryManagementSystem(root)
    root.title("Library Management System")
    root.geometry("1350x750")
    root.iconbitmap('pictures/logo.ico')
    root.mainloop()

if __name__ == "__main__":
    main()