print(" *** Solution 01 to place double the values in lists")

# numbers = [1, 3, 5]
# doubled = []
# new_number = 0
#
# for number in numbers:
#     new_number = number * 2
#     doubled.append(new_number)
# print("List with double the value: ", doubled)
#

print(" *** Solution 02 to place double th values in new lists")

# numbers = [1, 3, 5]
# doubled = []
#
# for number in numbers:
#     doubled.append(number * 2)
# print("Updated lists of double[] : ", doubled)

print(" *** Solution 03 to place double th values in new lists")
print(" *** // list comprehension demo is this ")
#
# numbers = [1, 3, 5]
# # what it will do, it will keep (number * 2) in new list for each item
# doubled = [number * 2 for number in numbers]
# print("Updated lists of double[] : ", doubled)

print(" *** Another solution for list comprehension")
# Let's keep the friends name which starts with "S" in starts_s lists

print(" *** Solution 01")
# friends = ['Bhanu', "Samantha", "Sam", "Saurabh", "Jen"]
# starts_s = []
#
# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)
# print("New friends name starts with S: ", starts_s)

print(" *** Solution 02")

friends = ['Bhanu', "Samantha", "Sam", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]
print("New friends name starts with S: ", starts_s)

print("friends: ", id(friends), "starts_s: ", id(starts_s))







