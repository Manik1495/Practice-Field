import random


logo = """

  ________                                __  .__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/             \/     \/          \/            \/    \/     \/       

"""

print(logo)

user_choice = int(input("Choose a number between 1 and 100.\n"))
game_level = input("Enter your choice of game level - hard or easy\n")

def randomComp_Num():
    num = random.randint(1,100)
    return num

# result = randomComp_Num()
random_num = randomComp_Num()

def play_game(game_level,random_num,user_choice):
    
    if game_level == 'easy':
            game_tries = 10
            
            while game_tries != 0:
                  for i in range (1,game_tries + 1):
                    
                    if i == 1:
                      if user_choice == random_num:
                            game_tries -= 1
                            return f"You got it! The answer was {random_num}"
                            # break
                      elif user_choice > random_num:
                            game_tries -= 1
                            print("Too high")
                            print(f"You have {game_tries} attempts remaining to guess the number.")
                      else:
                            game_tries -= 1
                            print("Too low")
                            print(f"You have {game_tries} attempts remaining to guess the number.")
                    else:
                        user_choice = int(input("Make a guess:"))
                        if user_choice == random_num:
                            game_tries -= 1
                            return f"You got it! The answer was {random_num}"
                            # break
                        elif user_choice > random_num:
                            game_tries -= 1
                            print("Too high")
                            print(f"You have {game_tries} attempts remaining to guess the number.")
                        else:
                            game_tries -= 1
                            print("Too low")
                            print(f"You have {game_tries} attempts remaining to guess the number.")
      
    if game_level == 'hard':
            game_tries = 4
            
            while game_tries != 0:
              for i in range (1,game_tries + 1):
                    if i == 1:
                      if user_choice == random_num:
                            game_tries -= 1
                            return f"You got it! The answer was {random_num}"
                            # break
                      elif user_choice > random_num:
                            game_tries -= 1
                            print("Too high")
                            print(f"You have {game_tries} attempts remaining to guess the number.")
                      else:
                            game_tries -= 1
                            print("Too low")
                            print(f"You have {game_tries} attempts remaining to guess the number.")
                    else:
                        user_choice = int(input("Make a guess:"))
                        if user_choice == random_num:
                            game_tries -= 1
                            return f"You got it! The answer was {random_num}"
                            # break
                        elif user_choice > random_num:
                            game_tries -= 1
                            print("Too high")
                            print(f"You have {game_tries} attempts remaining to guess the number.")
                        else:
                            game_tries -= 1
                            print("Too low")
                            print(f"You have {game_tries} attempts remaining to guess the number.")

    if game_tries == 0:
        return "You've run out of guesses, you lose."

result = play_game(game_level,random_num,user_choice)
print(result)