import random

cards = [11]

user_str = [11,10]
def get_usercards_second():
    sum_firstusercards = 0
    user_cards_second = []
    for i in range (0,1):
        user_cards_second.append(random.choice(cards))      
        
    print(user_cards_second)  
    user_temp = []
    user_temp = user_str.copy()
    user_temp.extend(user_cards_second)
    user_cards_second = user_temp.copy()
    if sum(user_str) == 21:
        if user_cards_second[2] == 11:
            user_cards_second[2] = 1
            
    else:
        pass
    print(user_cards_second)

get_usercards_second()