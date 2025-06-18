# This is a simple Python script that greets the user.
def main():
    ## Ask user for their name
    name = input("What's your full name? ")

    #remove whitespace from str and capitalize user's name
    name= name.strip().title()

    #Split user's name into first and last name
    fname, lname = name.split()

    ## Greet user
    hello(fname)

#Define the hello function
def hello(to="World"):
    print(f"Hello, {to} !")

#running the main function
main()

 