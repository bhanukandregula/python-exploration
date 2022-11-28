# this functools is required for every script we have decorators
import functools

user = {"username": "Mr. Bhanu Prakash Kandregula", "access_level": "guest"}


def make_secure(func):
    # use it for everywhere when we have decorators in the script
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function


@make_secure
def get_admin_password():
    return "09876"


print(get_admin_password())

# function name will change internally
print(get_admin_password.__name__)
