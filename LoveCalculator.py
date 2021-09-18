print("Welcome to Python Love Calculator \n")

girl_name = input("Enter the lady's name: ")

boy_name = input("Enter the guy's name: ")

girl_name = girl_name.lower()

boy_name = boy_name.lower()

#print(girl_name)

super_name = girl_name + boy_name
# print(super_name)

total_t = super_name.count("t")
total_r = super_name.count("r")
total_u = super_name.count("u")
total_e = super_name.count("e")

total_l = super_name.count("l")
total_o = super_name.count("o")
total_v = super_name.count("v")
total_e = super_name.count("e")

sum_of_true = total_t + total_r + total_u + total_e
sum_of_love = total_l + total_o + total_v + total_e

score_str = f"{sum_of_true}{sum_of_love}"
score = int(score_str)

print(score)

if score < 10 or score > 90:
    print(f"your score is {score} , you go together like coke and mentos.")

elif score >= 40 and score <= 50:
    print(f"your score is {score} , you are alright together")

else:
    print(f"your score is {score}")