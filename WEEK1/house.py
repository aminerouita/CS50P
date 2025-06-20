# This program asks the user for their name and tells them which house they belong to at Hogwarts.

def main():
   #ask the user for their name

    name = input("What's your name? ").capitalize()

    # Check the name and print the corresponding house at Hogwarts

    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Hello, " + name + "! You are house Gryffindor!")
        case "Draco":
            print("Hello, Draco! You are house Slytherin!")
        case _:
            print("Hello, " + name + "! You are not a member of any house at Hogwarts.")
    
main()
