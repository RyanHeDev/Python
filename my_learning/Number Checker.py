import random

numbers = [1,3,5,7,9,11,13,15]

real_answer = False
n = 0
while real_answer != True:
    num1 = random.choice(numbers)
    num2 = random.choice(numbers)
    num3 = random.choice(numbers)
    answer = num1 + num2 + num3
    n += 1
    print(f"Test answer {n}")
    if answer == 30:
        print(f"The answer is: {num1} + {num2} + {num3} = 30")
        real_answer = True
