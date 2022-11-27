class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # this will be invoked when we need to print object as a string
    def __str__(self):
        return f"Person {self.name}, is {self.age} years old !!!"

    # goal is unambiguous
    # This will return a string that allow us to recreate the original object very easily
    # To test this repr, comment the __str__ and check on the print logs
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"

bob = Person("Bob", 30)
print("Person is :: ", bob )