from typing import List


# Type Hinting - is a new feature from Python 3.5

# Define a function for list average calculation
# below syntax will let python know, this is a list should contain float values
# This is Type Hinting.
def list_avg(sequence: List) -> float:
    return sum(sequence)/len(sequence)

list_avg(123)


# Another example for Type Hinting, we can type hint anywhere required
class Book:
    # pass
    # We can specify the data types with the function params as below
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count

# Another example to use Type hinting
# We can also import Tuples, Sets, List etc
# to do so, we need to import List on the top of the file
# from typing import List
class Bookshelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)} books."

# Another example for Type Hinting
class Book:
    TYPES= ("Hardcover", "Paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type} and weight: {self.weight}g>"

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @staticmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)