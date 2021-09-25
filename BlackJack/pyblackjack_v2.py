
import random
from user_cards_function import get_usercards, get_compcards,get_compcards_second,get_usercards_second




start_blackJack = True


i=0


def cloning_user():
    user_cards = []
    user_cards = get_usercards()
    # user_cards.extend(get_usercards())
    return user_cards

def cloning_comp():
    comp_cards = []
    comp_cards = get_compcards()
    # user_cards.extend(get_usercards())
    return comp_cards

def final_score(lis):
    sum = 0
    for num in range (0, len(lis)):
        sum += lis[num]
    return sum
def winner(score_user, score_comp):
    if score_user > 21 and score_comp > 21:
        if score_user < score_comp:
            return 'user'
        elif score_user == score_comp:
            return 'draw'
        else:
            return 'comp'
    elif score_user < 21 and score_comp < 21:
        if score_user > score_comp:
            return 'user'
        elif score_user == score_comp:
            return 'draw'
        else:
            return 'comp'

    else:
        if score_user > 21:
            return 'comp'
        else:
            return 'user'

while start_blackJack:
    user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if user_choice == 'y':
        start_blackJack = True
        
        user_cardlist = cloning_user()
        comp_cardlist = cloning_comp()
        print(f"user cards --> {user_cardlist}")
        print(f"computer cards -->{comp_cardlist}")
        user_input = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_input == 'y':
            user_card_new = []
            comp_card_new = []
            total_userCards = []
            total_compCards = []
            sum_user = 0
            sum_comp = 0
            user_card_new = get_usercards_second()
            comp_card_new = get_compcards_second()

            user_cardlist.extend(user_card_new)
            comp_cardlist.extend(comp_card_new)

            print(f"You final cards are  --> {user_cardlist}")
            sum_user = final_score(user_cardlist)
            print(f"User final score -->{sum_user}")
            

            print(f"computer inal cards are -->{comp_cardlist}")
            sum_comp = final_score(comp_cardlist)
            print(f"Computer final score -->{sum_comp}")

            result_winner =winner(sum_user,sum_comp)

            if result_winner == 'user':
                print("user win")
            else:
                print("comp win ")
        else:
            comp_card_new = get_compcards_second()
            comp_cardlist.extend(comp_card_new)
            
            print(f"You final cards are  --> {user_cardlist}")
            sum_user = final_score(user_cardlist)
            print(f"User final score -->{sum_user}")
            

            print(f"computer inal cards are -->{comp_cardlist}")
            sum_comp = final_score(comp_cardlist)
            print(f"Computer final score -->{sum_comp}")

            result_winner =winner(sum_user,sum_comp)
            if result_winner == 'user':
                print("user win")
            else:
                print("comp win ")

            start_blackJack = True
    else:
        start_blackJack = False

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
