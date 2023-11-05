
import random

option = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

options = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

print(options[option])

random_option = random.randint(0, 2)
print(options[random_option])

if option == random_option:
    print("Draw")
elif (option == 0 and random_option == 2) or (option == 1 and random_option == 0) or (option == 2 and random_option == 1):
    print("You win!")
else:
    print("You lose!")
