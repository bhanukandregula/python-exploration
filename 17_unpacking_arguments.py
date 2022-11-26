# We can pass any number of arguments, and they will be loaded into args params
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

mul_value = multiply(1,2,3)
print(mul_value)

# Another way to play with args
def add(x, y):
    return x + y

nums = [3,5]
sum_value = add(*nums)
print("Sum value is: ", sum_value)

# We can also send named params when we use args
def add(x, y):
    return x + y

nums = [3,5]
sum_value = add(x=5, y=3)
print("Sum value is: ", sum_value)

# let's try to pass the values in dictionary
def add(a, b):
    return a + b

nums = {
    "x" : 15,
    "y" : 16
}

sum_value_dict_01 = add(nums["x"], nums["y"])
print("Sum value from dictionary 01 is: ", sum_value_dict_01)

nums02 = {
    "x" : 15,
    "y" : 16
}

# we can also send the params values with **
# This throws an error, - yet to solve

# sum_value_dict_02 = add(**nums02)
# print("Sum value from dictionary 02 is: ", sum_value_dict_02)

print("******* - Using the *args param and operator")
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

def apply(*args, operator):
    if operator == "*":
        # * is important here, else we will get the tuple of tuples instead multiply of all the values in the tuple
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"

print(apply(1,2,3,4, operator="*"))