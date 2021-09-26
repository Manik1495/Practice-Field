import random
from game_data import data

name_fromdict = ''
follower_countdict = 0
description_fromdict = ''
country_fromdict = ''
list = []
compare_A = []
against_B = []
#add the values of dictionary in list

def random_nameGen():
    list = []
    dataDict_fromList = random.choice(data)
    for key in dataDict_fromList:
        list.append(dataDict_fromList[key])
    return list
compare_A = random_nameGen()
against_B = random_nameGen()

print(compare_A,against_B)