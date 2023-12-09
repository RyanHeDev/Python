# Brute Force Algorithm
# Brute Force Search
# method 1
"""
for n in range(101):
    if n % 2 == 0:
        print(f"{n} is even ")

# method 2
num = 0
while num != 100:
    num += 1
    if num % 2 == 0:
        print(f"{num} is even")
"""
# method 3 : this is the best practice
for n in range(2, 101, 2):
    print(f"{n} is even")
