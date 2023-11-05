import random

print("""
           __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ /_/_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
                                 """)
                                 
data = [
    {
        "name": "Instagram",
        "follower_count": 500,
        "description": "Social media platform",
        "country": "United States"
    },
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 300,
        "description": "Professional footballer",
        "country": "Portugal"
    },
    {
        "name": "Lionel Messi",
        "follower_count": 250,
        "description": "Professional footballer",
        "country": "Argentina"
    },
    {
        "name": "Neymar Jr",
        "follower_count": 200,
        "description": "Professional footballer",
        "country": "Brazil"
    }
]

score = 0
should_continue = True

def compare():
    
    option_a = random.choice(data)
    option_b = random.choice(data)
    
    
    print(f"Compare A: {option_a['name']}")
    print(option_a['description'])
    print(option_a['country'])
    
    print("\nVS\n")
    
    print(f"Compare B: {option_b['name']}")
    print(option_b['description'])
    print(option_b['country'])
    
    guess = input("Who has more followers? Type A or B: ")
    
    global score
    global should_continue
    
    if guess.upper() == 'A':
        if option_a['follower_count'] >= option_b['follower_count']:
            print("You guessed correctly! Option A has more followers.")
            score += 1
            print(f"Your score is {score}")
        else:
            print("Sorry, you guessed incorrectly. Option B has more followers.")
            should_continue = False
    elif guess.upper() == 'B':
        if option_b['follower_count'] >= option_a['follower_count']:
            print("You guessed correctly! Option B has more followers.")
            score += 1
            print(f"Your score is {score}")
        else:
            print("Sorry, you guessed incorrectly. Option A has more followers.")
            should_continue = False
    else:
        print("Invalid input. Please enter either 'A' or 'B'.")

while score < 5 and should_continue:
    compare()
