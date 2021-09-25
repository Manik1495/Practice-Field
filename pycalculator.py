logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
from clear_console import clear

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

def maths_operation(first_num,second_num):
    if calc_op == '+':
        result = add(first_num,second_num)
        return result
    elif calc_op == '-':
        result = sub(first_num,second_num)
        return result
    elif calc_op == '*':
        result = mul(first_num,second_num)
        return result
    else:
        result = div(first_num,second_num)
        return result

first_num = int(input("enter the first number.\n"))

print("+\n -\n *\n /\n")
calc_op = input("pick an operation for calculation.\n")
second_num = int(input("enter the second number.\n"))

output = maths_operation(first_num, second_num)





is_continue = True

while is_continue:
    
    user_input = input(f"the result is {output}. Press y to continue with {output} or press n for starting new calculation.\n")
    if user_input == 'y':
        clear()
        first_num = output
        calc_op = input("pick an operation for calculation.\n")
        second_num = int(input("enter the second number.\n"))
        output = maths_operation(first_num, second_num)
    else:
        is_continue = False
        print(f"the value calculated is --> {output}")




