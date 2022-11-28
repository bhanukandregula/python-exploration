# this functools is required for every script we have decorators
import functools

user = {"username": "Mr. Bhanu Prakash Kandregula", "access_level": "guest"}


def make_secure(func):
    # use it for everywhere when we have decorators in the script
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function


@make_secure
def get_password(panel):
    if panel == "admin":
        return "09876"
    elif panel == "bulling":
        return "super_secure_password"


print(get_password("billing"))
