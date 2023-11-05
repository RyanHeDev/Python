
import random

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

secret_number = random.randint(1, 100)
easy_attempts = 10
hard_attempts = 5

if difficulty == "easy":
    print(f"You have {easy_attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    while easy_attempts != 0:
        if guess == secret_number:
            print(f"You won with {easy_attempts} left.")
            break
        elif guess != secret_number:
            easy_attempts -= 1
            if guess > secret_number:
                print("Too high")
            else:
                print("Too low")
            print("Guess again.")
            guess = int(input("Make a guess: "))
            print(f"You have {easy_attempts} attempts remaining to guess the number.")

elif difficulty == "hard":
    print(f"You have {hard_attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    while hard_attempts != 0:
        if guess == secret_number:
            print(f"You won with {hard_attempts} left.")
            break
        elif guess != secret_number:
            hard_attempts -= 1
            if guess > secret_number:
                print("Too high")
            else:
                print("Too low")
            print("Guess again.")
            guess = int(input("Make a guess: "))
            print(f"You have {hard_attempts} attempts remaining to guess the number.")
