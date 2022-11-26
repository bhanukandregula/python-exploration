# when we just declare a tuple, paranthesis is optional. But in any other case
# like when we create a list of tuples in [], then we need to have ()
x = (5, 11)
y = [(2,3), (95,8)]

# we can also destructure the variables when we create tuples
t = 7, 9
a, b = t

print("Values of the destructured variables: ", a, b)

student_attendance = {
    "Anne" : 98,
    "Anna" : 80,
    "Anil" : "98"
}

# print the dictionarie as in list
print(list(student_attendance.items()))

for student, attendance in student_attendance.items():
    print(f"{student} : {attendance}")

# In the for loop, it actually render values as tuples while executing
for t in student_attendance.items():
    print(t)

print("******** Tuple with three values each *************");
# A tuple can also have multiple values
people = [("James", 42, "Mechanic"), ("Bob", 87, "Artist"), ("Harry", 65, "Lecturer")]
for name, age, profession in people:
    print(f"Name: {name}, Age: {age} and Profession: {profession}")

print()
print("****** How to ignore values in Python, _")
# we can create a space to store variable as _ to ignore its value
employee = ("Mr. Kandregula", 30, "Software Engineer")
name, _, profession = employee
print(name, profession)

print()
print("******** Seperate single lists into two lists ********")
# First value in the list will be head, and all the other values will be in tail
head, *tail = [98, 45, 76, 56, 34, 32]
print(head)
print(tail)

# vice-verse of above situation
print()
*head, tail = [98, 45, 76, 56, 34, 32]
print(head)
print(tail)

