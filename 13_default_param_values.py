# We can pass the few values from function definition and other param values when we invoke the function
def addition(x, y=10):
    print(f"sum of {x} and {y} is : ", x + y)

# but we can't the value for y, since we already have it function declaration
# or we can't provide Y value here, that will override
addition(x=18)

print("*********** We can't override default values over execution ***********")
# Let's create a default value for a variable
default_y=5

def add(x, y=default_y):
    print(f"sum of {x} and {y} is: ", x + y)

add(4)

# we can't override the default value again for the same valle
default_y=10
# this will return 2 + 5 = 7, but not 2+10 = 12
# hence the default_y value can't override over execution
add(2)


