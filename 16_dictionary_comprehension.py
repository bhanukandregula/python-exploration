# Dictionary =  Key, Values pair.

# Create a list of users, where each user will be stored in each tuple
users = [
    (0, "Bob", "password"),
    (1, "Anne", "password@Anne"),
    (2, "Anna", "PasswordFor@Anna"),
    (3, "Robson", "RobWord@pass")
]

# we need to map for id with username
# keys = username
# values =  all the tuple value for each user
username_mapping = { user[1] : user for user in users}
# this will print complete object
print("Username_mapping values:: ", username_mapping)

# print just one value with username
print("Just one user log:: ", username_mapping["Anne"])

print("**** - Verification of user credentails from the dictionary")
username_input = input("Please enter your username: ")
password_input = input("Please enter your password: ")

# This will ignore the id value, since it is declared as _
_, username, password = username_mapping[username_input]

# print(username)
# print(password)

if password_input == password:
    print("Your credentials are valid !")
else:
    print("Your credentials are invalid !!!")

