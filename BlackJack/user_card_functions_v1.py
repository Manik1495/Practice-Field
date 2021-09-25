
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


i=0
# user_str = ''
comp_str = ''

def get_usercards():
    user_cards = []
    for i in range (0,2):
        user_cards.append(random.choice(cards))      
    return user_cards

def get_compcards():
    computer_cards = []
    for i in range (0,1):
        computer_cards.append(random.choice(cards))               
    return computer_cards

# def get_usercards_second():
#     sum_firstusercards = 0
#     user_cards_second = []        
#     for i in range (0,1):
#         user_cards_second.append(random.choice(cards))      
#     return user_cards_second

def get_usercards_second(user_firstcards):
    sum_firstusercards = 0
    user_cards_second = []
    for i in range (0,1):
        user_cards_second.append(random.choice(cards))      
        
    print(user_cards_second)  
    user_temp = []
    user_temp = user_firstcards.copy()
    user_temp.extend(user_cards_second)
    user_cards_second = user_temp.copy()
    if sum(user_firstcards) == 21:
        if user_cards_second[2] == 11:
            user_cards_second[2] = 1
            
    else:
        pass
    return user_cards_second


def get_compcards_second():
    comp_cards_second = []
    for i in range (0,2):
        comp_cards_second.append(random.choice(cards))      
    return comp_cards_second

# print(get_compcards_second())
# print(get_usercards_second())