# first class functions:
# functions are just variables we can pass then as an arguments to another functions

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can not be 0")
    return dividend / divisor


# *values is a tuple, all the params we pass to this *values will be saved as a tuple format
# this calculate function takes any number of values,
def calculate(*values, operator):
    return operator(*values)


# invoke the function and print the result value
# operator value we are passing here is: divide which is a function name.
# hence we are passing a function name as a variable in another function

# this function only can take two params as an input, not more than that.
result = calculate(10000000, 23, operator=divide)
print(result)
