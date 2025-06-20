## This program checks if a number is even or odd
# Prompt the user to enter a number 
# Check if the number is even or odd with a function and print the result

def main():
    x = int(input("Enter a number X : "))
    if is_even(x):
        print("X is even!")
    else:
        print("X is odd!")

# This function checks if a number is even

def is_even(n):
    return n % 2 == 0 
  


main()

