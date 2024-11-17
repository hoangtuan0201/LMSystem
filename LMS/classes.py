import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

class Book:
    def __init__(self, book_id, title, author, year, isbn, status="Available", issuer_id=None, borrow_date=None,
                 return_date=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.status = status
        self.issuer_id = issuer_id
        self.borrow_date = borrow_date
        self.return_date = return_date

    def borrow(self, user_id):
        if self.status == "Available":
            self.status = "Issued"
            self.issuer_id = user_id
            self.borrow_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.return_date = None  # Clear any existing return date
            return True
        return False

    def return_book(self, user_id):
        if self.status == "Issued" and self.issuer_id == user_id:
            self.status = "Available"
            self.issuer_id = None
            self.return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
        return False


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

    def borrow_book(self, book_id):
        for book in books:
            if book.book_id == book_id:
                return book.borrow(self.user_id)
        return False

    def return_book(self, book_id):
        for book in books:
            if book.book_id == book_id:
                return book.return_book(self.user_id)
        return False


class Admin(User):
    def add_book(self, title, author, year, isbn, status="Available", issuer_id=None):
        book_id = len(books) + 1
        new_book = Book(book_id, title, author, year, isbn, status, issuer_id)
        books.append(new_book)
        messagebox.showinfo("Success", "Book added successfully!")