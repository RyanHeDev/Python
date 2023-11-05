
#Adding Evens

# v 1.0
total = 0

for n in range(2,101,2):
    total += n
print(total)

#Adding Evens

# v 2.0
total = 0

for n in range(1,101):
    if n % 2 == 0:
        total += n
print(total)
