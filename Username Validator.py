# 1. username is not more than 12 characters
# 2. username must not contain spaces
# 3. username mst not contain digits

user_name = input("Enter a username: ")

if len(user_name) > 12:
    print("Your username cannot be more than 12 characters")
elif not user_name.find(" ") == -1:
    print("Your username cannot contain spaces")
elif not user_name.isalpha():
    print("ONLY ALPHABET!")
else:
    print(f"Welcome {user_name} ^^")

