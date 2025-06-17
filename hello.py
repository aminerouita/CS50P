# This is a simple Python script that greets the user.
## Ask user for their name
name = input("What's your full name? ")

#remove whitespace from str and capitalize user's name
name= name.strip().title()

#Split user's name into first and last name
fname, lname = name.split()

## Greet user
print(f"hello, {fname} !")

