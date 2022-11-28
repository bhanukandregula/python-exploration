# In python, all things are mutable, since everything is an object
# unless we change the properties of the objects
# mutating = changing

a = []
# b = a
# Now the values and its memory values will be different as a and b are different
b = []

# tuples don;t have an append method.
a.append(34)

# ID value will give us back the location o the variable in the memory
# we will observe the same memory values for these two variables, a = [] and b = a
print(id(a))
print(id(b))

# this will prnt the same value as well for both the a, b variables
print(a)
print(b)

a = "hello"
b = a

print(id(a))
print(id(b))

a += "World"

print(id(a))

