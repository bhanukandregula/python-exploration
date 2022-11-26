print("***** Creating and Invoking sample function definition ********")# Creating a function with name hello
def hello():
    print("Hello !!!")


hello()

print()
print("****** Display user age in seconds with functions ********")
# Let's create another function
def user_age_in_seconds():
    user_age = int(input("Please enter your age "))
    age_in_seconds = user_age * 365 * 24 * 60 * 60
    print("Your age in seconds is: ", age_in_seconds)


user_age_in_seconds()

print()
print("****** Add friend to friends list from a function *******")
# add some friends from a function
friends = []


def add_friends():
    friends.append("Mr. Potter")
    friends.append("Mr. weasly")


add_friends()
print("Friends list as follows: ", friends)

