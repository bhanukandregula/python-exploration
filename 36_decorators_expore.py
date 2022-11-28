# decorators allow us to modify the functions

# Create a dictionary
user = {"username": "Mr. Bhanu Prakash Kandregula", "access_level": "guest"}


# Create a function to get admin password
def get_admin_password():
    return "09876"


# # mostly users who have guest access won't be able to see the admin password.
# # for a user to get admin password, user should have admin as his/her access_level
# def secure_admin_password():
#     if user["access_level"] == "admin":
#         print(get_admin_password())
#
#
# # invoke secure admin password function
# secure_admin_password()

# we can use fist class functions for the same use case implementation
# we can also define a function inside a function in python
def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"

    # here we are returning complete function itself, rather than just the function call/ any value.
    return secure_function


get_admin_password = make_secure(get_admin_password)

# Print the admin password
print(get_admin_password())
