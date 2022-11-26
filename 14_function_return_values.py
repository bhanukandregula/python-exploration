def addition(x, y):
    print(x + y)

addition(2,3)

# We need to assign the result values to return keyword, so we can invoke functions in a better way
# If wee return with no value, it will return none and rest of the function execution will stop
# return
def addition(x, y):
    return x + y

sum_value = addition(2, 3)
print(f"Sum value: ", sum_value)


# Let's create another function for subtractions
def subtraction(x, y):
    if x>y:
        return x - y
    else:
        return y - x

# When we have return statement, we can't invoke the function without assigning value for it
# subtraction(4,2)
sub_value = subtraction(45, 90)
print("Sub value", sub_value)


# Sample divide function
def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "It won't work like that, please check"

divide_value = divide(15,0)
print("Divide value: ", divide_value)


# Sample multiplication function as part of exercise
def multiplication(x, y):
    return x * y

mul_value = multiplication(3,2)
print(f"Multiplication value is: ", mul_value)
