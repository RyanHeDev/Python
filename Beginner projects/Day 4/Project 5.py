
# Fizz Buzz

for number in range(1,10):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number %5 == 0:
        print("Fizz Buzz")
    else:
        print(number)
