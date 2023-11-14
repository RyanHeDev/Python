
food = {}
n = 0
for i in range(4):
    n += 1
    fav_food = input("Enter your favorite food: ")
    food[n] = fav_food

print(food)

dislike = int(input("Which food do you hate of these: "))

del food[dislike]
print(sorted(food.values()))
