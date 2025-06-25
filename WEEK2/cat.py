def main():
    meows = int(input("How many meows do tou want? "))
    miaw(meows)

def miaw(meows):
    while True:
        if meows < 0:
            meows = int(input("Please enter a positive number: "))
        elif meows == 0:
            meows = int(input("No meows for you!\nPlease enter a positive number: "))
        else:
            for _ in range(meows):
                print("Meow!")
            break


main()


