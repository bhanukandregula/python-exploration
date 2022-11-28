# this functools is required for every script we have decorators
import functools

user = {"username": "Mr. Bhanu Prakash Kandregula", "access_level": "guest"}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}"

        return secure_function

    return decorator


# this is for only admins
@make_secure("admin")
def get_admin_password():
    return "admin:1234"


# this is for only users
@make_secure("user")
def get_dashboard_password():
    return "user: user_password"


print(get_admin_password())
print(get_dashboard_password())
