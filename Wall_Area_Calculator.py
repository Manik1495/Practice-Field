# Area Calc
# Instructions
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height ✖️ wall width) ÷ coverage per can.

# e.g. Height = 2, Width = 4, Coverage = 5

# number of cans = (2 ✖️ 4) ÷ 5

#                      = 1.6
#                      = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

# IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

# Example Input
# test_h = 3
# test_h = 3
# test_w = 9
# test_w = 9
# Example Output
# You'll need 6 cans of paint.
# You'll need 6 cans of paint.
# Hint
# 1. To round up a number:

# https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python

# Make sure you name your function/parameters the same as when it's called on the last line of code.

def paint_calc (height,width,coverage):
    number_of_cans = round((height * width) / coverage)
    return number_of_cans

wall_height = int(input("Enter the wall height:\n"))
wall_width = int(input("Enter the wall width:\n"))
coverage =5 


no_of_cans = (paint_calc(height = wall_height,width = wall_width,coverage = coverage))

print(f"\nNumber of cans required to paint your wall --> {no_of_cans}")
