def main():
    print_square(H,W)
H = int(input("Enter the height of the square: "))
W = int(input("Enter the width of the square: "))


def print_square(h,w):
    for i in range(H):
        for j in range (W):
            print("#", end="")
        print()
        

main()

