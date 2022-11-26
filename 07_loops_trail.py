print("*********** While Loop Demo ****************")
# final_number = 18
# # user_input = input("Would you like to play ? (Y/n)")
#
# # while user_input != "n":
# while True:
#     user_input = input("Would you like to play ? (Y/n)")
#
#     if user_input == "n":
#         break
#
#     user_number = int(input("Guess your number: "))
#     if user_number == final_number:
#         print("You guessed correctly, congratulations")
#     elif abs(final_number - user_number) == 1:
#         print("You were off by one")
#     else:
#         print("sorry, you got incorrect guess!")

print("*********** For Loop Demo ****************")

# friends = ["Bhanu", "Bob", "Bobby", "Anne"]
#
# print("*** This is the manual process without loops")
# print(f"{friends[0]} is my friend")
# print(f"{friends[1]} is my friend")
# print(f"{friends[1]} is my friend")
#
# print("*** Let use For loop to loop through the lists we have")
# for friend in friends:
#     print(f"{friend} is my friend")
#
# # this will give us the number for each element in list
# for friend in range(2):
#     print(f"{friend} is also my friend")
print("lets caliculate the average grade of this class")

# grades = [35,54,67,54,56,87,90,32]
# total = 0
# averageGrade = 0;
# # total number of grades we have (list count)
# amount = len(grades)
# print(f"{amount} is amount value")
# for grade in grades:
#     total = 00000total + grade
# averageGrade = total/amount
#
# print("Average of all grades is: ", averageGrade)

# grades = [35,54,67,54,56,87,90,32]
# print("Average grade of the class is: ",sum(grades)/len(grades))

print("************ Problem 01 ****************")
numbers=[1,2,3,4,5,6,7,8,9]
evens=[]
for number in numbers:
    if (number%2) == 0:
        evens.append(number)
print("This is evens list: ", evens)

print("************ Problem 02 ****************")
user_input = input("Enter your choice: ").lower()
if user_input == "a":
    print("Add")
elif user_input == "q":
    print("Quit")
else:
    print("Thanks for participation in games,")

