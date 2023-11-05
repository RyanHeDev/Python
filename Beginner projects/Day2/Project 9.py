
print("Welcome to Treasure Hunt")


direction = input("Do you want to turn left or right? ").lower()

if direction == "right":
    action_one = input(" Do you want to swim across the river or find a boat? ").lower()
    if action_one == "boat":
        action_two = input("You have crossed the river successfully,you found a hunted house 🛖 do you want to get in or go forward? ").lower()
        if action_two == "get in":
            print("You found the treasure! ")
        else:
            print("You met a monster and killed you 💀")
    else:
       print(" You die, a crocodile ate you 💀")
else:
    print(" You die 💀 ")
