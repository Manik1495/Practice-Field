year = int(input("Enter the year of your wish: "))


if(year % 4 == 0):
    if(year % 100 != 0):
        print(f"{year} is a leap year")
    elif(year % 100 == 0 and year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print("Not a leap year")
else:
    print("Not a leap year")