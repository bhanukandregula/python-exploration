print("********** Creating and Accessing dictionaries *****************")

# We will check on the dictionaries here
# mostly used to store data in key-value format
friend_ages = {"Bhanu": 30, "Bob" : 25, "Anne": 27}
# Accessing dictionary values
print(friend_ages["Bob"])

# Adding new elements to dictionary
friend_ages["Bradley"] = 28
print(friend_ages["Bradley"])

# Complete dictionary
print(friend_ages)

# Let's make a list of dictionary with all the friends
friends = [
    {"name": "Bill", "age": 50},
    {"name": "Thomas", "age": 60},
    {"name": "Curie", "age": 48}
]

# print all the friends
print(friends)

# print specific from list of dictionary with index as reference
print(friends[1])
print(friends[1]["name"])

print("********** Iteriate over the dictionary *****************")
#  let's create a dictionary of student and their attendence percenatges
student_attendence = {
    "Rob" : 96,
    "Bob" : 80,
    "Anna": 100
}

# This will get the key value from the dictionary
for student in student_attendence:
    print(student)
    print(f"{student} : {student_attendence[student]}")

# Another way to access the keys and values in the dictionaries
for student, attendance in student_attendence.items():
    print(f"{student}: {attendance}")

print("****** Find how many lectures student attended *************")

student_lectures = {
    "Bhanu": 40,
    "Anil" : 50,
    "Rob" : 25
}

# loop through the above dictionarie
for student, lectures in student_lectures.items():
    print(f" {student} attended {lectures} lectures in current semester.")

# check with Rob is active enrolled student
if "Rob" in student_lectures:
    print(f"Our current student Rob : {student_lectures['Rob']}")
else:
    print("Rob is not a current tern student")

print("****** Class average percentage of results  *********")
student_percentages = {
    "Anne" : 30,
    "Bob" : 70,
    "Caron" : 90,
    "David": 45,
    "Edger" : 86
}

# Get the values of all the keys in dictionarie
for student, percentage_value in student_percentages.items():
    print(f"{percentage_value}")

# Another approach to get the values of all keys in dictionarie
print(student_percentages.values())
student_average = sum(student_percentages.values()) / len(student_percentages)
print("All students average is: ", student_average)

