# how to generate randow word

#create number of blanks equal to random word.

# convert the word to list

#  inout from user to guess an alphabet

    # if its present in the random word,replace that char position of blank with the alphabet.
    #  else reduce number of games.



import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

sel_word = random.choice(WORDS)
our_word = sel_word.decode("utf-8") 
print(type(our_word))
print(our_word)


length_word = len(our_word)

list_word = list(our_word)
print(list_word)

blank_lines = "_" * length_word
print(blank_lines)

list_blank_lines = list(blank_lines)



def get_indices_elem_inlist(list_of_elems, char):
    index_pos = 0
    index_list = []
    while True:
        try:
            index_pos = list_of_elems.index(char, index_pos)
            index_list.append(index_pos)
            index_pos += 1

        except ValueError as e:
            break
    
    return index_list

#list_of_elems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test', 'Ok']




# print(index_pos_list)
range = 0
while range < 6 :
    choose_char = input("select an alphabet:\n")
    index_pos_list = get_indices_elem_inlist(list_word, choose_char) 
    print(index_pos_list)
    for elem in index_pos_list:
        list_blank_lines[elem] = choose_char
    if(list_blank_lines.__contains__("_")):
        print("continue")   
    else:
        break 
    range +=1


print(range)
print(list_blank_lines)

if(list_blank_lines.__contains__('_')):
    print("You lose")
else:
    print("you win")

# for num in range(1,6):
#     print(list_blank_lines)
#     choose_char = input("select an alphabet:\n")
#     for char in list_word:
#         print(char)
#         print(f"current index --> {list_word.index(char)}")
#         print(type(choose_char))
#         if(choose_char == char):
#             index = list_word.index(char)
#             print(index)
#             list_blank_lines[index] = char
#             char = ''
            



# for char in our_word_list:

