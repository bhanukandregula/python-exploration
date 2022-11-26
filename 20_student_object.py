class Student:
    # def __init__(self):
    #     self.name = "Mr. Kandregula"
    #     self.grades  =(78,98,89,87,90)

    def __init__(self, name, grades):
        self.name = name
        self.grades =  grades


    def average_grade(self):
        return sum(self.grades) / len(self.grades)

#
# student = Student()
# # print("Name: " , student.name)
# # print("Grades: ", student.grades)
# # print("Student grades average: ", Student.average(student))
# print("Student grades average: ", student.average_grade())

student01 =  Student("Anne", (87,67,89,98))
student02 = Student("Bob", (56,76,87,89))
print("Student 01 average grade: ", student01.average_grade())
print("Student 02 average grade: ", student02.average_grade())


class Employee:
    def __init__(self, name):
        self.name = name

employee = Employee("Bhanu")
print("Current employee name: ", employee.name)




