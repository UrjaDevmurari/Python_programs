# class composition is better approach than class inheritance


class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"The bookshelf has total {len(self.books)} books in it."

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} has {self.pages} pages."


book1 = Book("Harry Potter", 1234)
book2 = Book("Hello World!", 50)
shelf1 = Bookshelf(book1, book2)
print(book1)
print(book2)
print(shelf1)