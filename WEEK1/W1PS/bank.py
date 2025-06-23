# This is a program that prompts the user for a greeting. 
# If the greeting starts with “hello”, output $0. 
# If the greeting starts with an “h” (but not “hello”), output $20. 
# Otherwise, output $100.


#prompt the user for a greeting and output the appropriate response
def main():
    greeting = input("Hello sir! ").strip().lower()
    bigbux(greeting)

def bigbux(greeting):
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

main()

