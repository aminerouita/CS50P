
def main():
    time = input("What time is it? ")
    convert(time) 

def convert(time):
    h , m = time.split(":")
    float_time = float(h) + float(m)/60
    if 07.00 <= float_time <= 8.0:
        print("Breakfast time!")
    elif 12.00 <= float_time <= 13.0:
        print("Lunch time!")
    elif 18.00 <= float_time <= 19.0:
        print("Dinner time!")

    

main()






