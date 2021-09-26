import random
from game_data import data
from art import logo, vs

# Define a function for random key-value generation from the list --> def random_nameGen()

dataDict_fromList = {}


#declare variables
name_fromdict = ''
follower_countdictA = 0
follower_countdictB= 0
description_fromdict = ''
country_fromdict = ''
list = []
compare_A = []
against_B = []
result_A = []
result_B = []
winner = ''
score = 0
#add the values of dictionary in list

def random_nameGen():
    list = []
    dataDict_fromList = random.choice(data)
    for key in dataDict_fromList:
        list.append(dataDict_fromList[key])
    return list
    # name_fromdict = list[0]
    # return name_fromdict
    # follower_countdict = list[1]
    # return follower_countdict
    # description_fromdict = list[2]
    # return description_fromdict
    # country_fromdict = list[3]
    # return country_fromdict

def func_compareA():
    compare_A = random_nameGen()
    return compare_A
    # name_fromdict = compare_A[0]
    # follower_countdictA = compare_A[1]
    # description_fromdict = compare_A[2]
    # country_fromdict = compare_A[3]

    # return (f"Compare A: {name_fromdict}, a {description_fromdict}, from {country_fromdict}.")

result_A = func_compareA()
print(result_A)
name_fromdict = result_A[0]
follower_countdictA = result_A[1]
description_fromdict = result_A[2]
country_fromdict = result_A[3]

print(f"Compare A: {name_fromdict}, a {description_fromdict}, from {country_fromdict}.")

def func_againstB():
    against_B = random_nameGen()
    # name_fromdict = against_B[0]
    # follower_countdictB = against_B[1]
    # description_fromdict = against_B[2]
    # country_fromdict = against_B[3]
    # print(f"Against B: {name_fromdict}, a {description_fromdict}, from {country_fromdict}.")
    return against_B
result_B = func_againstB()
print(result_B)
name_fromdict = result_B[0]
follower_countdictB = result_B[1]
description_fromdict = result_B[2]
country_fromdict = result_B[3]
print(f"Against B: {name_fromdict}, a {description_fromdict}, from {country_fromdict}.")


def who_got_moreFollow(followers_A,followers_B):
    if followers_A > followers_B:
        winner = 'A'
        return winner

    else:
        winner = 'B'
        return winner

user_choice = input("Who has more followers? Type 'A' or 'B':")

winner = who_got_moreFollow(follower_countdictA,follower_countdictB)



def who_is_winner(user_choice, winner,result_B):
    fun_score = 0
    is_game = True
    while is_game:
        if user_choice == 'A' and winner == 'A':
            result_A = result_B
            name_fromdict = result_B[0]
            follower_countdictA = result_B[1]
            description_fromdict = result_B[2]
            country_fromdict = result_B[3]

            print(f"Compare A: {name_fromdict}, a {description_fromdict}, from {country_fromdict}.")


            result_B = func_againstB()
            name_fromdict = result_B[0]
            follower_countdictB = result_B[1]
            description_fromdict = result_B[2]
            country_fromdict = result_B[3]
            print(f"Against B: {name_fromdict}, a {description_fromdict}, from {country_fromdict}.")
            fun_score += 1
            print(fun_score)
            user_choice = input("Who has more followers? Type 'A' or 'B':")


        elif user_choice == 'B' and winner == 'B':
            result_A = result_B
            name_fromdict = result_B[0]
            follower_countdictA = result_B[1]
            description_fromdict = result_B[2]
            country_fromdict = result_B[3]

            print(f"Compare A: {name_fromdict}, a {description_fromdict}, from {country_fromdict}.")


            result_B = func_againstB()
            name_fromdict = result_B[0]
            follower_countdictB = result_B[1]
            description_fromdict = result_B[2]
            country_fromdict = result_B[3]
            print(f"Against B: {name_fromdict}, a {description_fromdict}, from {country_fromdict}.")
            # print(compare_A)
            fun_score += 1
            print(fun_score)
            user_choice = input("Who has more followers? Type 'A' or 'B':")

        else:
            is_game = False
            return (f"You lose and your score is {fun_score}")
            

print(who_is_winner(user_choice,winner,result_B))

