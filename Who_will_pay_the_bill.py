import random

# test_seed = input("Enter the random seed number: ")
# random.seed(test_seed)

names = input("Enter the names: ")

namesAsCSV = names.split(",")

# print(namesAsCSV)

gen_randint = random.randint(0,len(namesAsCSV)-1)
print(gen_randint)
print(namesAsCSV[gen_randint])


print(f"{namesAsCSV[gen_randint]} will pay the bill")

