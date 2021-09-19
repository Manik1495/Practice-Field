import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_c = input("what do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: ")

player_choice = int(player_c)

if player_choice == 0:
    print(rock)

if player_choice == 1:
    print(paper)

if player_choice == 2:
    print(scissors)

computer_random = random.randint(0,2)

print(computer_random)

if computer_random == 0:
    print(scissors)

elif computer_random == 1:
    print(paper)

elif computer_random == 2:
    print(rock)



#Rules

if(player_choice ==0 and computer_random == 0):
    print("You win")

elif(player_choice == 0 and computer_random == 1):
    print("You lose")

elif(player_choice == 1 and computer_random == 0):
    print("You lose")

elif(player_choice == 1 and computer_random == 2):
    print("You win")

elif(player_choice == 2 and computer_random == 1):
    print("You win")

elif(player_choice == 2 and computer_random == 2):
    print("You lose")

elif (player_choice >=3):
    print("You have choosen invalid number.")

else:
    print("Draw")

