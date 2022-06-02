# Random Dice Game
import random
min_val = 1
max_val = 6
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dices...")
    print("The Values are :")
    print(random.randint(min_val, max_val))
    print(random.randint(min_val, max_val))
    if min_val+max_val<10:
        print("You Win")
    else:
        print("i win")
        
    roll_again = input("Roll the Dices Again?") 