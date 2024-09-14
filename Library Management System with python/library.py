
import file_handler
from book import Book

class Library:
    def __init__(self):
        self.books = file_handler.load_books()

    def add_book(self, book):
        self.books.append(book)
        file_handler.save_books(self.books)

    def view_books(self):
        for book in self.books:
            print(book)

    def search_books(self, term):
        results = [book for book in self.books if term.lower() in book.title.lower() or term.lower() in book.isbn.lower()]
        for book in results:
            print(book)

    def search_by_author(self, author):
        results = [book for book in self.books if any(author.lower() in a.lower() for a in book.authors)]
        for book in results:
            print(book)

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                file_handler.save_books(self.books)
                return
        print("Book not found")

    def lend_book(self, isbn, borrower):
        for book in self.books:
            if book.isbn == isbn and book.quantity > 0:
                book.quantity -= 1
                file_handler.save_books(self.books)
                file_handler.record_lent_book(book, borrower)
                return
        print("Not enough books available to lend")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.quantity += 1
                file_handler.save_books(self.books)
                file_handler.record_returned_book(book)
                return
        print("Book not found")

    def view_lent_books(self):
        lent_books = file_handler.load_lent_books()
        for entry in lent_books:
            print(f"{entry['book']} lent to {entry['borrower']}")
