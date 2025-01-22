class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return f"You've borrowed '{self.title}'."
        return f"'{self.title}' is currently unavailable."

    def return_book(self):
        self.is_available = True
        return f"'{self.title}' has been returned."


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]


# Example usage
library = Library()
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library.add_book(book1)
library.add_book(book2)

print("Books in the library:", library.list_books())
print(book1.borrow())  # Borrow 1984
print(book1.borrow())  # Try borrowing again
print(book1.return_book())  # Return 1984
