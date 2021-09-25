"""
Days in Month
Instructions
In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

days_in_month(year=2022, month=2)
days_in_month(year=2022, month=2)
And it will use this information to work out the number of days in the month, then return that as the output, e.g.:

28
28
The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.
"""

def leap_year(year):
    if(year % 4 == 0):
        if(year % 100 != 0):
            # print(f"{year} is a leap year")
            return True
        elif(year % 100 == 0 and year % 400 == 0):
            # print(f"{year} is a leap year")
            return True
        else:
            return False
    else:
        return False


no_of_days = [31,28,31,30,31,30,31,31,30,31,30,31]
result = 0

def no_of_days_result(month):
    # for mon in range(1,len(no_of_days)+1):
    result = no_of_days[month+1]
    return result

def days_in_months(year, month):
        # Jan,Mar,May,July,Aug,Oct,Dec
        # Feb
        # Apr,Jun,Sep,Nov
    
    # month = str.lower(month)
    is_leap_year = leap_year(year)
    
    if is_leap_year:
        if month == 2:
            days = 29
            return days
        else:
            # for mon in range(1,len(no_of_days)+1):
            #     result = no_of_days[mon]
            days = no_of_days_result(month)
            return days
    else:
        days = no_of_days_result(month)
        return days

choice_year = int(input("Enter your choice of year. \n"))
choice_month = int(input("Enter your choice of month. \n"))

days_result = days_in_months(choice_year, choice_month)
print(days_result)