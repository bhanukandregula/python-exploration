# Working with numbers
value = 18
price = 200
discount = 0.2
result = price * (1-discount)
print("This is the total price value: ", result)
print("************************************************")

# Working with strings
name = "Bhanu Kandregula"
name = "Raghu Babu Kandregula"
print('Name of the stundent is: ', name *2)
print("************************************************")

# Working with numeric values
a = 23
b = a
print("value of a is: ", a)
print("value of b is: ",b)
print("************************************************")

# working for excercise
var1 = 12
var2 = var1
print("Value of var1 is: ", var1)
print("Value of var2 is: ", var2)
print("************************************************")

# working to multiply two numbers that results 16
num1 = 2
num2 = 8;
result = num1 * num2
print(result)
print("************************************************")

# string formatting
name = "Bhanu Prakash"
surname = f"Kandregula, {name}"
print("Full name of student is: ", surname)
print("************************************************")

name = "Bhanu prakash"
fullname = "Kandregula, {}"
with_fulname = fullname.format(name)
with_fullname_brother = fullname.format("Raghu Babu")
print("Here is the complete name: ", with_fulname)
print("We can resue the template like this: ",with_fullname_brother)
print("************************************************")

longer_phrase = "Hello Mr, {}. This is Python from {} "
formatted = longer_phrase.format("Bhanu Kandregula", "Internet")
print("Full formatter value:", formatted )
print("************************************************")

# How to get user input
# name = input("Please enter your name: ")
# print(name)
print("************************************************")

# Input function always returns string value, hence we need to convert string to integer value
# size_input = input("How big is your house (in square feet) ")
# squate_feet = int(size_input)
# squate_meters = squate_feet / 10.8
# print(squate_meters)
# print(f"{squate_feet} squate feet is {squate_meters} squate meters equalavalent")
# # this will scale the decimals upto 2
# print(f"{squate_feet} squate feet is {squate_meters: .2f} squate meters equalavalent")
print("************************************************")

# user_age = input("Please enter your age")
# years = int(user_age)
# months = years * 12
# print(f" Your age {years} is equal to {months} months")

# we can also convert string value from input function dirctly to int like this
# print("************************************************")
# user_age = int(input("Please enter your age: "))
# months = user_age * 12
# print(f"Your age {user_age} years is equal to {months} months")
print("************************************************")
# Lets see how many seconds a person with certain age lived long
user_age = int(input("Please enter your age: "))
months =user_age * 12
days = months * 30
minutes = days * 24
seconds = minutes * 60
print(f" Your age {user_age} years is equal to {seconds} seconds")
print("************************************************")

