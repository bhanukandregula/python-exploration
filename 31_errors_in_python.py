# def divide(dividend, divisor):
#     if divisor == 0:
#         print("Divisor can not be 0")
#         return
#     else:
#         return dividend / divisor
#
# # invoke the divide function
# # divide(10, 0)
#
# # grades = [78, 98, 90, 78, 67]
# grades = []
# print("welcome to the average grade program.")
# average = divide(sum(grades), len(grades))
# print(f"The average grade is: ", {average})

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can not be 0")
    else:
        return dividend / divisor


# # grades = [78, 98, 90, 78, 67]
# grades = []
# print("welcome to the average grade program.")
# try:
#     average = divide(sum(grades), len(grades))
#     print(f"The average grade is: ", {average})
# except ZeroDivisionError as e:
#     print("There are no grades yet in your list: ", e)


# Another way to handle average value case
grades = [78, 98, 90, 78, 67]
# grades = []
print("welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print("There are no grades yet in your list: ", e)
else:
    print(f"The average grade is: ", {average})
finally:
    print("Thanks for using our product to your average calculations.")
