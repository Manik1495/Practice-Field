age = int(input("Enter the age: "))

big_age = 90

#days,week,months

big_year = big_age - age

days = big_year * 365
weeks = big_year * 52
months = big_year * 12

print(f"{days}, {weeks}, {months}")