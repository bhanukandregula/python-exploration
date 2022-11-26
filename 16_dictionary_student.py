students = {
        'name': 'Jose',
        'school' : 'Computing',
        'grades' : (66,77,88)
    }

def average_grades(student):
    return sum(student['grades'])/len(student['grades'])
    # grades = data['grades']
    # return sum(grades)/len(grades)

average = average_grades(students)
print("Average grades of students is: ", average)

