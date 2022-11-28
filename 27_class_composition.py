# # Composition is a counterpart to Inheritance to build out classes that use other classes
# class Bookshelf:
#     def __init__(self, quantity):
#         self.quantity = quantity
#
#     def __str__(self):
#         return f"Bookshelf with {self.quantity} books."
#
#
# shelf = Bookshelf(300)
# print(shelf)
#
# class Book(Bookshelf):
#     def __init__(self, name, quantity):
#         super().__init__(quantity)
#         self.name = name
#
#     # If we don't have str here, Book() will fetch str from super class and make use of it.
#     # A Bookshelf has many books, but not every book is in the Bookshelf
#     def __str__(self):
#         return f"Book: {self.name}"
#
# book =  Book("Happry Potter", 1200)
# print(book)

# Composition is a counterpart to Inheritance to build out classes that use other classes
class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."

#
# shelf = Bookshelf(300)
# print(shelf)

class Book:
    def __init__(self, name):
        self.name = name

    # If we don't have str here, Book() will fetch str from super class and make use of it.
    # A Bookshelf has many books, but not every book is in the Bookshelf
    def __str__(self):
        return f"Book: {self.name}"

book01 =  Book("Happry Potter")
book02 = Book("The Moment of Lift")
shelf = Bookshelf(book01, book02)
print(shelf)