# This is a program that prompts the user for an arithmetic expression 
# Then calculates and outputs the result as a floating-point value formatted to one decimal place

# Prompting the user for x and y values and outputting the result

def main():
    expression = input(" I can calculate whatever you want. Try me! ").strip()
    x, y, z = expression.split(" ")
    calculate(x, y, z)

#calculating and outputting the result

def calculate(x, y, z):
    if "+" in y:
        result = float(x) + float(z)
        print(f"{result:.1f}")
    elif "-" in y:
        result = float(x) - float(z)
        print(f"{result:.1f}")
    elif "*" in y:
        result = float(x) * float(z)
        print(f"{result:.1f}")
    elif "/" in y:
        if float(z) == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = float(x) / float(z)
            print(f"{result:.1f}")
    else:
        print("Error: Invalid operation. Please use +, -, *, or /.")

# Starting the program

main()
