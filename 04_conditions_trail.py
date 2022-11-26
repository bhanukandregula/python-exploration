# Check habits based on the user days
print("***************** IF  Conditions **********************")

day_of_week = input("What day of the week is it today ? ").lower()
# print(f"Today is {day_of_week}: ", day_of_week == "Monday")

if day_of_week == "monday":
    print("Stay home and Relax")
elif day_of_week == "Tuesday":
    print("Please visit Temple")
else:
    print("Please go for workout")
