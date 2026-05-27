# Classes and Objects
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return f"{self.title} by {self.author} ({self.pages} pages)"

    def is_long(self):
        return self.pages > 300

book = Book("Python 101", "John Doe", 250)
print(book.description())
print(f"Long book: {book.is_long()}")
