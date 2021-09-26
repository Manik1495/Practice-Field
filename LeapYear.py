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



    # # def is_leap(year):
    # leap = False
    
    # # Write your logic here
    # # Write a function in Python - Hacker Rank Solution START
    # if year%400==0 :
    #     leap = True;
    # elif year%4 == 0 and year%100 != 0:
    #     leap = True;
    # return leap