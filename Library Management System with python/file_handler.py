
import json
from book import Book

BOOKS_FILE = 'books.json'
LENT_BOOKS_FILE = 'lent_books.json'

def load_books():
    try:
        with open(BOOKS_FILE, 'r') as f:
            data = json.load(f)
            return [Book(**book) for book in data]
    except FileNotFoundError:
        return []

def save_books(books):
    with open(BOOKS_FILE, 'w') as f:
        json.dump([book.__dict__ for book in books], f)

def record_lent_book(book, borrower):
    lent_books = load_lent_books()
    lent_books.append({'book': book.title, 'borrower': borrower})
    with open(LENT_BOOKS_FILE, 'w') as f:
        json.dump(lent_books, f)

def record_returned_book(book):
    lent_books = load_lent_books()
    for entry in lent_books:
        if entry['book'] == book.title:
            lent_books.remove(entry)
            break
    with open(LENT_BOOKS_FILE, 'w') as f:
        json.dump(lent_books, f)

def load_lent_books():
    try:
        with open(LENT_BOOKS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
