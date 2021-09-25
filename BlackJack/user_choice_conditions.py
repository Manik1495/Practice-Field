
from user_cards_function import get_usercards, get_compcards,get_compcards_second,get_usercards_second


def user_choice_condition(user_choice):
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