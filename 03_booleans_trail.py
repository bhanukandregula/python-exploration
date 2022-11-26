# Booleans - 1,0, true and false
print("Boolean value is: ", 5 == 5)
print("Boolean value is: ", 5 < 2)
print("Boolean value is: ", 23 > 90)
print("Boolean value is: ", 34 > 5)
print("Boolean value is: ", 10 != 10)

# Comparisions: == , != , >= , <= , < , >

# Let's check with lists
friends = ["Bhanu","Bob"]
old_friends = ["Bhanu", "Bob"]
new_friends = friends
print("Friends and Old friends are same: ", friends == old_friends)
print("Friends and New friends are same: ", friends == new_friends)

# this will return false, since in memory each lis has its unique mmeory allocations.
# IS will check excalty same thing rather than same elements/similar.
# Never use IS to compare
print("Friends and Old friends are same: ", friends is old_friends)