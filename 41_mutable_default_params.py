from typing import List, Optional


# class Student:
#     # This is a very bad idea
#     # never make a parameter by a mutable value by default
#     def __init__(self, name: str, grades: List[int] = []):
#         self.name = name
#         self.grades = grades
#
#     def take_exam(self, result):
#         self.grades.append(result)
#
#
# # this will print 90 for babu as well, even babu didn't take the exam
# bob = Student("Bob")
# banu = Student("Banu")
# bob.take_exam(90)
# print(banu.grades)
# print(bob.grades)


class Student:
    # This is a very bad idea
    # never make a parameter by a mutable value by default
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result):
        self.grades.append(result)


# this will print 90 for babu as well, even babu didn't take the exam
bob = Student("Bob")
banu = Student("Banu")
bob.take_exam(90)
print("Banu grades: ", banu.grades)
print("Bob grades: ", bob.grades)
