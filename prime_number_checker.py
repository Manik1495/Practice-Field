

get_num = int(input("Enter the number: \n"))

def check_prime_num(num):
    i = 2
    status = ''
    if num == i:
        print(f"{num} is a prime number")
    
    while i < num:
        if num % i == 0:
            status = "Not prime"
            break
        else: 
            i += 1

    if status == "Not prime":
        print ("Not Prime")
    else:
        print("Prime")


    # if num % 1 == 0 and num % num == 0:
    #     for i in range (,10):
    #         if num % i == 0:
    #            print(f"{num} is not a prime number") 
    #            break
    #         else:
    #             pass
    # else:
    #     print(f"{num} is a prime number")


check_prime_num(num = get_num)