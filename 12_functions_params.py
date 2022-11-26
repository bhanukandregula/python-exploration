# create a function that has parameters
# pass means - it does nothing
def add(a, b):
    result = a + b
    print(result)


add(5, 10)


# Create a function which accepts a string as a parameter
def say_hello(name):
    print(f"Hello {name}")


say_hello("Mr. Potter")


# order will follow the parameter allocation from where we invoke the function
def full_name(name, surname):
    print(f"Name: {name} and Surname: {surname}")


full_name("Mr. Harry", "Potter")


# this will assign the respective param name as mentioned when we invoke
def student_profile(name, surname, dept):
    print(f" Student Name: {name}, Surname: {surname}, Branch: {dept}")


student_profile(surname="Kandregula", name="Bhanu", dept="CSE")






