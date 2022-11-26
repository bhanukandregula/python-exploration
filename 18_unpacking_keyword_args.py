def named(**kwargs):
    print(kwargs)

# kwargs returns a dictionary for us, as below
# kwargs will collect all the keyword args and make a dictionary for us
named(name="Bhanu", age=30)

# Let's ee another way to pass values as dictionary
def greetings(name, age):
    print(name, age)

details = { "name" : "Bhanu", "age": 30}

# ** can be used to collect named args into dictionary (or)
greetings(**details)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg} : {value}")

print_nicely(name="bhanukandregula",age=30)

print("********** let's use both, args and kwargs")
def both(*args, **kwargs):
    print(args)
    print(kwargs)
both(1,2,3, name="Bob", age=25)