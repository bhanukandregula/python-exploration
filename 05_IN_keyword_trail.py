# IN Keyword, used to check for membership, if something is exists in lists, tuple or sets
friends = ["Sanjay", "Shyam", "Bob"]

# This will return boolean value
print("Sanjay" in friends)

# This is a set
movies_watched = {"Titanic", "Avatar", "Adipurush"}
user_movie = input("Please enter the movie you have watched recently: ")

print(user_movie in movies_watched)

if user_movie in movies_watched:
    print(f"Glad you watched {user_movie}")
else:
    print("You can do when are free")