# this example is to illustrate the usage of class methods as a factory


class Book:
    bookCover = ("hard", "paperback")

    def __init__(self, name, cover, author):
        self.name = name
        self.cover = cover
        self.author = author

    @classmethod
    def hardCover(cls, name, author):
        return cls(name, cls.bookCover[0], author)

    @classmethod
    def paperback(cls, name, author):
        return cls(name, cls.bookCover[1], author)

    def __str__(self):
        return f"Book name: {self.name} is written by {self.author} and has {self.cover}"


book1 = Book.hardCover("Harry potter", "E.L.James")
print(book1)

book2 = Book.paperback("XYZ", "ABC")
print(book2)
