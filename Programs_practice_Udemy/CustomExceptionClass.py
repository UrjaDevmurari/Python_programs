class TooManyPagesException(ValueError):
    pass


class Book:
    def __init__(self, name, totalPages: int):
        self.name = name
        self.totalPages = totalPages
        self.pagesRead = 0

    def __repr__(self):
        return f"{self.name} has total {self.totalPages} pages."

    def read(self, noOfPages: int):
        if self.pagesRead + noOfPages > self.totalPages:
            raise TooManyPagesException(
                f"You are trying to read {self.pagesRead + noOfPages} pages where the book has only {self.totalPages} pages."
            )

        self.pagesRead += noOfPages
        print(f"I read {self.pagesRead} out of {self.totalPages} of {self.name} book.")


book1 = Book("Harry Potter1", 1500)
try:
    book1.read(120)
    book1.read(2000)
except TooManyPagesException as e:
    print(e)
