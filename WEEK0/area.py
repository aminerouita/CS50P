def main():
    print("Welcome to the room area calculator!")
    length = float(input("Please enter the length of your room in meters: "))
    width = float(input("Please enter the width of your room in meters: "))
    room_area = area(length, width)
    print(f"The area of your room is: {round(room_area,2)} square meters!")
    
def area(length, width):
    return length * width
    

main()
