
import random
from user_cards_function import get_usercards, get_compcards,get_compcards_second

from user_card_functions_v1 import get_usercards_second
from pyart import logo

print(logo)


start_blackJack = True
i=0


#Step 1 --> Create functions for first set of user cards and computer cards

def cloning_user():
    """
    This function is used for getting the user card values 
    and store into an empty list.
    """
    user_cards = []
    user_cards = get_usercards()
    # user_cards.extend(get_usercards())
    return user_cards
#Step 2 --> Create functions for first set of user cards and computer cards
def cloning_comp():
    """
    This function is used for getting the computer card values 
    and store into an empty list.
    """
    comp_cards = []
    comp_cards = get_compcards()
    # user_cards.extend(get_usercards())
    return comp_cards

#Step 4 --> Create function to calculate final sum of user and computer.
def final_score(lis):
    """
    This function is used for calculating the computer/user card values 
    and return the sum.
    """
    sum = 0
    for num in range (0, len(lis)):
        sum += lis[num]
    return sum

#Step 5 --> Create function to calculate final sum of user and computer.
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


#Step 3 --> Create code to start logic with while true of something
while start_blackJack:
    user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if user_choice == 'y':
        start_blackJack = True
        
        # first set of values

        user_cardlist = cloning_user()
        comp_cardlist = cloning_comp()
        print(f"user cards --> {user_cardlist}")
        print(f"computer cards -->{comp_cardlist}")

        # condition to check whether user has already 21.
        if sum(user_cardlist) == 21 and len(user_cardlist) == 2:
            print("user wins")
            start_blackJack = True

        else:
            user_input = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_input == 'y':
                user_card_new = []
                comp_card_new = []
                total_userCards = []
                total_compCards = []
                sum_user = 0
                sum_comp = 0
                user_card_new = get_usercards_second(user_cardlist)
                comp_card_new = get_compcards_second()

                #adding second values to user and computer

                user_cardlist = user_card_new.copy()
                comp_cardlist.extend(comp_card_new)


                #final card details of user and sum of cards
                print(f"You final cards are  --> {user_cardlist}")
                sum_user = final_score(user_cardlist)
                print(f"User final score -->{sum_user}")
                
                #final card details of computer and sum of cards
                print(f"computer final cards are -->{comp_cardlist}")
                sum_comp = final_score(comp_cardlist)
                print(f"Computer final score -->{sum_comp}")

                #find the winner --> call the function winner
                result_winner =winner(sum_user,sum_comp)

                if result_winner == 'user':
                    print("user win")
                elif result_winner == 'comp':
                    print("comp win ")
                else:
                    print("its a draw")
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
