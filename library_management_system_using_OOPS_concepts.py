class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True

    def is_available(self):
        return self.available

    def check_out(self):
        if self.available:
            self.available = False
            return True
        else:
            return False

    def return_book(self):
        self.available = True


class User:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def display_user_details(self):
        print(f"Name: {self.name}")
        print(f"Member ID: {self.member_id}")

    def display_borrowed_books(self):
        if not self.borrowed_books:
            print("You have not borrowed any books.")
        else:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print(f"- {book.title}")

    def borrow_book(self, book):
        if book.is_available():
            self.borrowed_books.append(book)
            book.check_out()
            print(f"{self.name} has borrowed '{book.title}' successfully.")
        else:
            print(f"'{book.title}' is not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
            print(f"{self.name} has returned '{book.title}' successfully.")
        else:
            print(f"'{book.title}' is not in your borrowed books list.")


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        self.users.append(user)

    def search_books(self, keyword):
        found_books = []
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                found_books.append(book)
        return found_books

    def display_available_books(self):
        available_books = [book for book in self.books if book.is_available()]
        if not available_books:
            print("No books available in the library.")
        else:
            print("Available Books:")
            for book in available_books:
                print(f"- {book.title}")


# Example usage:

# Create books
book1 = Book("Book 1", "Author 1", "Fiction")
book2 = Book("Book 2", "Author 2", "Mystery")
book3 = Book("Book 3", "Author 3", "Fantasy")

# Create users
user1 = User("User 1", "M001")
user2 = User("User 2", "M002")

# Create library
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Register users
library.register_user(user1)
library.register_user(user2)

# Borrow books
user1.borrow_book(book1)
user2.borrow_book(book2)

# Return books
user1.return_book(book1)

# Search for books by title or author
search_result = library.search_books("Author 1")
for book in search_result:
    print(f"Found: {book.title} by {book.author}")

# Display available books
library.display_available_books()

# Display user details and borrowed books
user1.display_user_details()
user1.display_borrowed_books()


# RUN IT FOR OUTPUT
