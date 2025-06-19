#In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).




def main():
    slownsteady = input("Wanna say somethinhg? ")
    slownsteady = slownsteady.replace(" ", "...")
    print("So what you are saying is : " + slownsteady, "?" , sep="...")

main()
