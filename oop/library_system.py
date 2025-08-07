class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class EBook(Book):  # Must inherit from Book
    def __init__(self, title, author, isbn, file_format, file_size):
        super().__init__(title, author, isbn)
        self.file_format = file_format
        self.file_size = file_size

class PrintBook(Book):  # Must inherit from Book
    def __init__(self, title, author, isbn, cover_type, page_count):
        super().__init__(title, author, isbn)
        self.cover_type = cover_type
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []  # Must initialize as empty list

    def add_book(self, book):
        self.books.append(book)  # Must use append()

    def list_books(self):
        return self.books  # Must return the list
