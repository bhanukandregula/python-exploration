class Book:
    # class properties
    # We have some data stored inside the class
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type} and weight is {self.weight} gm>"

    @classmethod
    def hardcover(cls, name, page_weight):
        # this returns a new object inside a class0
        return Book(name, Book.TYPES[0], page_weight * 100)

    @classmethod
    def paperback(cls, name, page_weight):
        # this returns a new object inside a class
        return Book(name, Book.TYPES[1], page_weight * 100)

# Create a book
# book = Book('Harry Potter', 'Comic Book', 20)
book = Book.hardcover("Harry Potter", 1200)
book2 = Book.paperback("Moment of Lift", 1400)

book3 = Book.hardcover("The Journey", 500)
# this will print the book name
print(book)
print(book2)
print(book3)

# this will print the book types we have in class
print(Book.TYPES)

