
class Book:
    def __init__(self, title, authors, isbn, year, price, quantity):
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.year = year
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f" {self.title} by {', '.join(self.authors)} (ISBN: {self.isbn}, Year: {self.year}, Price: {self.price}, Quantity: {self.quantity})"
