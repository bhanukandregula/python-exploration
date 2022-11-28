# this will import divide function we have, from mymodule file.
# from mymodule import divide

# this will import all the functionalities in mymodule.py
import mymodule

# this is a system import
import sys

# print(divide(10,2))

# __name__ will be printed as __main__ depends on from where we are executing the py file.
# print(__name__)

# this has all the paths where python is going look at
# this pick the python path, from environment variables
# print(sys.path)
print(sys.modules)