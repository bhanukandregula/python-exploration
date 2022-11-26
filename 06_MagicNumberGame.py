# Small number guess game
final_number  = 18
user_wanna_play = input("Would you like to play the number game ? Please type YES or NO ")

# We can use the tuples and place possibilities we are willing to accept from user input
#if user_wanna_play == "YES":
if user_wanna_play in ("YES", "yes", "Yes"):
    #Game logic  begins
    user_number = int(input("Please enter any random number less than 100 "))
    if user_number < 100:
        if user_number == final_number:
            print("You have guesses correctly, good job")
        # elif final_number - user_number in (1, -1):
        elif abs(final_number - user_number) == 1:
            print("You are off by just one value")
            print("Sorry, better luck next time")
        else:
            print("Sorry, better luck next time")
    else:
        print("Please enter the number less than 100 ")
else:
    print("Sorry to see you go, have a great day!")

