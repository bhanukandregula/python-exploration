#  We are going to explore three different types of collections in Python - Lists, Tuples, Sets amd Dictionaries

# Lists
# We can add or modify the elements in lists
# Lists and Tuples always keep elements in order
l = [ "New York", "Michigan", "Arkansas"]

# Tuples
# We can't modify a Tuple., that means we can't add or remove elements from tuple
# Lists and Tuples always keeps elements in order
t = ("New York", "Michigan", "Arkansas")

# Sets
# We can add or remove elements from Sets. but we can't have duplicates in Sets
# Sets don't necessarly keep elements in the order, order is not guarented
s = { "New York", "Michigan", "Arkansas"}

# We can access individual elements in lists and tuples.
# we can;t do the same for Sets, since sets don't allow us to use sudscripts to use on them
print("First element in Lists: ", l[0])
print("First element in Tuple: ", t[0])

# we can modily those Lists values
l[0] = "California"
print("This is the upated value of Lists: ", l[0])

# We can use append() function to add new elements at the end of lists
l.append("Las Vegas")
print("All the elements in Lists: ", l)

# We can also remove certain elements from lists
l.remove("Michigan")
print("Updated lists: ", l)

# Let's try to remove it with index value
l.remove(l[2])
print("Updated lists", l)

# We can't update the same as in Tuples, which will throw an error
# t[0] = "Virginia"
# print("Updated value of tuples: ", t[0])

# We can add things to sets
# Note: Sets don't maintain proper order, so expect output as it may change
# We can't have duplicates in Sets, so we can;t add the same value twice or more.
s.add("Washington")
print("Updated Sets looks like: ", s)

print("************** Difference in Sets *******************")

friends = {"Sanjay", "Shyam", "Ramyanth"}
local_friends = {"Sanjay", "Shyam"}
# local_friends = {"Sanjay", "Shyam"}

# This will have the difference of friends and abroad_friends
abroad_friends= friends.difference(local_friends)
print("My abroad friends are: ", abroad_friends)

print("************** Union in Sets *******************")
india_friends = {"Sanjay", "Shyam", "Dileep"}
usa_friends = {"Kishore", "Sunil", "Bharath"}
london_friends = {"Ramyanth"}
friends = india_friends.union(usa_friends)
print("India and US friends are: ", friends)

print("************** Intersection in Sets *******************")
# This will get the common elements we have in both the sets
arts = {"Bob", "Jen","Rolf","Charlie"}
science = {"Bob", "Jen", "Adam","Anne"}

both = arts.intersection(science)
print("Both Arts and Science: ", both)

print("************* List with three number, and sum is 100*******************")
l = ["30","60","10"]
print("Sum of three elements in the list is: ", int(l[0]) + int(l[1]) + int(l[2]) )

print("************* Create a tuple with single value in it*******************")
t = ("MyFirstTuple")
t2 = 23,
print("Only Tuple value is: ", t)
print("Another value of Tuple is: ", t2)

print("************* Sets intersection demo*******************")
set01 = {14, 5, 9,31,12,77,67,8}
# set02 = {5}
set02 = {5, 12,9,77}

# Expected intersection set is: {5,77,9,12}
result = set01.intersection(set02)
print("Final set with intersection values are: ", result)









