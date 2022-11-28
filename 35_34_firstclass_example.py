from operator import itemgetter


# search function which looks for an element in the sequence
def search(sequence, expected, finder):
    for element in sequence:
        if finder(element) == expected:
            return element
    raise RuntimeError(f"Could not find an element {expected}")


# let's have a list of friends
friends = [
    {
        "name": "Bob",
        "age": 30
    },
    {
        "name": "Anne",
        "age": 27
    },
    {
        "name": "Apple",
        "age": 12
    }
]


# get a friend name
def get_friend_name(friend):
    return friend["name"]


# here we are passing get_friend_name as a parameter, which is a function name
print(search(friends, "Anne", get_friend_name))

# we can also use lambda functions in this case, instead of passing function name as param
print(search(friends, "Bob", lambda friend: friend["name"]))

# we can use itemgetter which is a builtin functionality from operator
# please import "from operator import itemgetter" in this file to use this functionality
print(search(friends, "Apple", itemgetter("name")))
