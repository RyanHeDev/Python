numbers = []
for number in range(1, 101):
    current_number = number
    if current_number % 15 == 0:
        numbers.append("FizzBuzz")
    elif current_number % 5 == 0:
        numbers.append("Buzz")
    elif current_number % 3 == 0:
        numbers.append("Fizz")
    else:
        numbers.append(current_number)  # No need to convert to string

print(", ".join(map(str, numbers)))
