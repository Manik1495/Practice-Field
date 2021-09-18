print("Welcome to Python Pizza Delivery Service")

size =  input("Enter your choice of Pizza size: - S,M,L:  ")

add_pepperoni = input("Do you want pepperoni to be added? ->Y or N: ")

extra_cheese = input("Do you want extra cheese?-->Y or N: ")

pizza_rate = 0
if size == 'S':
    pizza_rate = 15
elif size == 'M':
    pizza_rate = 20
else:
    pizza_rate = 25

if add_pepperoni == 'Y' and size == 'S':
    pizza_rate += 2

if add_pepperoni == 'Y' and size == 'M':
    pizza_rate += 3

if add_pepperoni == 'Y' and size == 'L':
    pizza_rate += 3

if extra_cheese == 'Y' :
    pizza_rate += 1


print(f"Your final bill for Pizza is : ${pizza_rate}")