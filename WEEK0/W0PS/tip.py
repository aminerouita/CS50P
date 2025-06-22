def main():
    dollars = input("How much was the meal? ")
    dollars = dollars_to_float(dollars)
    percent = input("What percentage would you like to tip? ")
    percent = percent_to_float(percent)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    dollars = float(dollars.strip("$").strip())
    return dollars   


def percent_to_float(percent):
    percent = float(percent.strip("%".strip()))
    percent = percent / 100
    return percent


main()