# ?mplement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. 
# Assume that the user will input an integer.

def main():
    # Prompt the user for mass in kilograms
    mass = int(input("Enter mass in kilograms: "))
    # Calculate the equivalent energy in Joules using E = mc^2
    c = 300000000 # Speed of light in m/s
    energy = mass * c ** 2
    # Output the energy as an integer
    print(energy)   

main()

