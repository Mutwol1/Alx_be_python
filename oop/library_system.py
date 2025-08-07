import unittest
from library_system import Book, Library

class TestLibraryImplementation(unittest.TestCase):
    def test_library_initialization(self):
        # Check if self.books is initialized as an empty list
        library = Library()
        self.assertTrue(hasattr(library, "books"), "Library should have a 'books' attribute")
        self.assertEqual(library.books, [], "Library.books should initialize as an empty list")

    def test_add_book_uses_append(self):
        # Check if add_book() uses list.append()
        library = Library()
        book = Book("Title1", "Author1", 1234567890)
        
        # Manually inspect the source code (alternative: mock list.append)
        with open("library_system.py", "r") as f:
            content = f.read()
            self.assertIn("self.books.append(", content, "add_book() should use self.books.append()")

    def test_list_books_exists(self):
        # Check if list_books() exists and returns the correct list
        library = Library()
        book1 = Book("Title1", "Author1", 1234567890)
        book2 = Book("Title2", "Author2", 9876543210)
        
        library.add_book(book1)
        library.add_book(book2)
        
        self.assertTrue(hasattr(library, "list_books"), "Library should have a list_books() method")
        books_list = library.list_books()
        self.assertEqual(len(books_list), 2, "list_books() should return all added books")
        self.assertIn(book1, books_list, "list_books() should include added books")
        self.assertIn(book2, books_list, "list_books() should include added books")

if __name__ == "__main__":
    unittest.main()
