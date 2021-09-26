import random
from game_data import data
from art import logo, vs
from clear_console import clear

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
score_player = 0
#add the values of dictionary in list

is_game = True

def func_compareA():
        compare_A = random_nameGen()
        return compare_A

def random_nameGen():
        list = []
        dataDict_fromList = random.choice(data)
        for key in dataDict_fromList:
            list.append(dataDict_fromList[key])
        return list

def func_againstB():
        against_B = random_nameGen()
        return against_B



def calc_winnerScore(user_choice, winner,score):
        fun_score = score
        if user_choice == 'A' and winner == 'A':
            fun_score += 1
            print(fun_score)
            return fun_score

        elif user_choice == 'B' and winner == 'B':
            fun_score += 1
            print(fun_score)
            return fun_score

        else:
            return None
            # (f"You lose and your score is {fun_score}")

def who_got_moreFollow(followers_A,followers_B):
        if followers_A > followers_B:
            winner = 'A'
            return winner

        else:
            winner = 'B'
            return winner      

while is_game:
    print(logo)
    if score >= 1:
        print(f"You're right! Current score: {score}")
        result_A = []
        result_A = result_B.copy()
        # print(result_A)
        name_fromdict = result_A[0]
        follower_countdictA = result_A[1]
        description_fromdict = result_A[2]
        country_fromdict = result_A[3]

        print(f"Compare A: {name_fromdict}, a {description_fromdict}, from {country_fromdict}.")
    else:
        result_A = func_compareA()
        # print(result_A)
        name_fromdict = result_A[0]
        follower_countdictA = result_A[1]
        description_fromdict = result_A[2]
        country_fromdict = result_A[3]
         

        print(f"Compare A: {name_fromdict}, a {description_fromdict}, from {country_fromdict}.")
        


    print(vs)
    

    result_B = func_againstB()
    print(result_B)
    name_fromdict = result_B[0]
    follower_countdictB = result_B[1]
    description_fromdict = result_B[2]
    country_fromdict = result_B[3]
    print(f"Against B: {name_fromdict}, a {description_fromdict}, from {country_fromdict}.")

    user_choice = input("Who has more followers? Type 'A' or 'B':")

   
    winner = who_got_moreFollow(follower_countdictA,follower_countdictB)

    # print(winner)

    
    score_player = calc_winnerScore(user_choice,winner,score_player)

    if score_player != None:
        score = score_player
        clear()
    else:
        clear()
        print(logo)
        print(f"You lose and your score is {score}")
        is_game = False
    # print(score_player)
    
    