class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __str__(self):
        return f"Book: {self.title} by {self.author} (ISBN: {self.isbn})"

class PrintBook(Book):
    def __init__(self, title, author, isbn, cover_type, page_count):
        super().__init__(title, author, isbn)
        self.cover_type = cover_type
        self.page_count = page_count
    
    def __str__(self):
        return (f"PrintBook: {self.title} by {self.author} "
                f"(ISBN: {self.isbn}, {self.cover_type}, {self.page_count} pages)")

class EBook(Book):
    def __init__(self, title, author, isbn, file_format, file_size):
        super().__init__(title, author, isbn)
        self.file_format = file_format
        self.file_size = file_size  # in MB
    
    def __str__(self):
        return (f"EBook: {self.title} by {self.author} "
                f"(ISBN: {self.isbn}, Format: {self.file_format}, Size: {self.file_size}MB)")
