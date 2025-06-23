#In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, 
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. 
# Otherwise output No.

#Prompting the user for the answer

def main():
    answer = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")).strip().lower()
    verdict(answer)

#Judging his answer and returning the verdict

def verdict (answer):
    if answer == "42":
        print("YES!")
    elif answer ==  "forty-two":
        print("YES!")
    elif answer == "forty two":
        print("YES!")
    else:
        print("NO.")

#Starting the program    

main()
