# Rock paper Scissors 
import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1 
    PAPER = 2
    SCISSORS = 3


"""
print(RPS(2))
print(RPS.ROCK)
print(RPS["ROCK"])
print(RPS.ROCK.value)
sys.exit()
"""

print("")
player_choice = int(input("Enter...\n 1 for Rock 🪨,\n 2 for Paper 📃,\n 3 for Scissors ✂️: \n\n"))
computer_choice = random.randint(1,3)

if player_choice < 1 or player_choice > 3:
    sys.exit("Choice out of range !!! \n You must enter 1, 2 or 3.")
    
print("")
print(f"You chose {str(RPS(player_choice)).replace('RPS.', ' ')}.")
print("Vs")
print(f"Python chose {str(RPS(computer_choice)).replace('RPS.', ' ')}.")
print("")

if player_choice == 1 and computer_choice == 3:
    print("You win. 🥳")
elif player_choice == 2 and computer_choice == 1:
    print("You win. 🥳")
elif player_choice == 3 and computer_choice == 2:
    print("You win. 🥳")
elif player_choice == computer_choice:
    print("Tie. 😮")
else:
    print("You lose. 🐍")
