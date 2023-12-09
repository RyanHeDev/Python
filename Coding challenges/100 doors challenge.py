# 100 doors coding challenge
doors = [False] * 101

for x in range(1, 101):
    for y in range(x, 101, x): # outer loop counter as the initial starting point and increment value
        doors[y] = not doors[y]

for x in range(1, 101):
    if doors[x] is True:
        print(x, end="|")
