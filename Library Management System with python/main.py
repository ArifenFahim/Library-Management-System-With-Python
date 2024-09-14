
from library import Library
from book import Book
import utils

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Search Books by Author")
        print("5. Remove Book")
        print("6. Lend Book")
        print("7. View Lent Books")
        print("8. Return Book")
        print("9. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            authors = input("Enter authors (comma separated): ").split(',')
            isbn = input("Enter ISBN: ")
            year = utils.input_int("Enter publishing year: ")
            price = utils.input_float("Enter price: ")
            quantity = utils.input_int("Enter quantity: ")
            book = Book(title, authors, isbn, year, price, quantity)
            library.add_book(book)
        elif choice == '2':
            library.view_books()
        elif choice == '3':
            term = input("Enter title or ISBN to search: ")
            library.search_books(term)
        elif choice == '4':
            author = input("Enter author name to search: ")
            library.search_by_author(author)
        elif choice == '5':
            isbn = input("Enter ISBN of the book to remove: ")
            library.remove_book(isbn)
        elif choice == '6':
            isbn = input("Enter ISBN of the book to lend: ")
            borrower = input("Enter borrower's name: ")
            library.lend_book(isbn, borrower)
        elif choice == '7':
            library.view_lent_books()
        elif choice == '8':
            isbn = input("Enter ISBN of the book to return: ")
            library.return_book(isbn)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
