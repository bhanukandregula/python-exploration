# create a dictionary as below
student = {
    "name" : "Mr. Potter",
    "grades" : (89,78,87,98,90)
}

# define a function that caliculate the average
def average(sequence):
    return sum(sequence)/len(sequence)

# print the result value of average
print(average(student["grades"]))

