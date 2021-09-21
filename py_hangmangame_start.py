import random
import requests
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

sel_word = random.choice(WORDS)
word_list = sel_word.decode("utf-8") 
# word_list = ["aar", "bab", "cam"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# chosen_word = random.choice(word_list)
chosen_word = word_list


display = []

end_of_game = False
print("entering while")
len_chosen_word = len(chosen_word)
for i in range(1, len_chosen_word + 1):
    display.append("_")

print(display)

len_stages = len(stages)

player_chance_inGame = 6

no_of_lives = 6
i = 0
while i < player_chance_inGame :
    
    guess = input("guess a letter: \n")
    guess = guess.lower()

    # print(chosen_word)
    if guess in display:
        print(f"You have selected '{guess}' letter")
    else:
        pos = 0
        stages_pos = 0
        for pos in range(len_chosen_word):
            char = chosen_word[pos]
            if char == guess:
                # index = chosen_word.index(char)
                # print("right")
                display[pos] = char
            else:
                pass
                
        # if chosen_word not in display:
        #     # no_of_lives -= 1
        #     stages[no_of_lives]

        if guess not in chosen_word:
            no_of_lives -= 1
            print(stages[no_of_lives])
            i += 1

    

        print(display)

        if  '_' not in display:
        # if display.__contains__("_"):
            end_of_game = True
            print("you win")
            break
        elif no_of_lives == 0:
            print(f"You lose. The correct word was {chosen_word}")