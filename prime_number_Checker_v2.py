

num = int(input("enter your number: \n"))

def prime_num_checker(num):
    is_prime = True
    for i in range(2,num-1):
        if num % i == 0:
            is_prime = False

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

prime_num_checker(num)
