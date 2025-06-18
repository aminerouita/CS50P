# This script takes an input from the user and square it.
def main():
    ## Ask user for the number to square
    x = int(input("What's X? "))
    print(f"X squared is: {square(x):,} !")

    #define the square function
def square(x):
    return x * x

#Print the result
main()
