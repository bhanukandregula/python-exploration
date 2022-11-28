
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can not be 0")
    else:
        return dividend / divisor

students = [
    {
        "name" : "Bob",
        "grades" : [79,98]
    },
    {
        "name": "Anne",
        "grades": [45,65]
    },
    {
        "name" : "Ishie",
        "grades": []
    }
]

try:
    for student in students:
        name = student['name']
        grades = student['grades']
        average = divide(sum(grades), len(grades))
        print(f"{name} average is: {average}")
except ZeroDivisionError as e:
    print(f"Error: {name} has no grades", e)
else:
    print("** All student averages were calculated **")
finally:
    print("*** End of the student average calculation ***")