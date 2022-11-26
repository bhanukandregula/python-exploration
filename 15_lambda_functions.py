# Lambda function is a name, that doesn't have a name and only return value
def addition(x, y):
    return x + y

addition_value = addition(6,8)
print(addition_value)

print("***** Lambda syntax examples ******")
# Let's write a lambda function for the above logic
# we don't need to specify the return keyword for lambda functions
lambda x, y: x + y

# we can also assign a variable for lambda function
mul = lambda x, y: x * y

# using/ invoking a lambda function
(lambda x, y: x+y)(3,2)

# we can use this format inside the print, for logs
print((lambda x, y: x + y)(5,10))

# double the values in below list
print()
print("*** - Using for loop")
sequence = [1, 2, 3, 4, 5]
double_sequence = []

for x in sequence:
    double_sequence.append(x*2)

print("Double sequence: ", double_sequence)

print()
print("*** - Using a function definition")

def double_the_sequence(x):
    return x*2

sequence = [1,2,3,4,5]
double_sequence = []

for x in sequence:
    double_sequence.append(double_the_sequence(x))

print("Double sequence: ", double_sequence)

print()
print("*** - Using list comprehension")

def double(x):
    return x*2

sequence = [1,2,3,4,5]
# #49 This is an example for list comprehension
doubled = [double(x) for x in sequence]
print("Doubled list is: ", doubled)

print()
print("*** - Using Lambda functions")

sequence = [1,2,3,4,5]
double_sequence = []

for a in sequence:
    double_sequence.append((lambda a: a*2)(a))

print("Double sequence from Lambda: ", double_sequence)

print()
print("*** - Using Map and Lambda")
sequence  =[1,2,3,4,5]
# doubled = [(lambda a:a*2)(a) for a in sequence]
doubled = list(map(lambda a:a*2, sequence))
print("Doubled list value from Map, Lambda: ", doubled)


