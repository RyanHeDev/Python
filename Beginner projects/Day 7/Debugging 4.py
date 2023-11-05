
# Debug Fizz Buzz Exercise

for number in range(1, 101):
    # use elif instead of if in line 7 and 9 
    if number % 3 or number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        # remove [] from print([number])
        print(number)
