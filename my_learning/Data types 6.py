
digits = [393, 102, 488, 652]

for digit in digits:
    print(digit)

user_digit = int(input("Enter a three digit number: "))
if user_digit in digits:
    print(digits.index(user_digit))

else:
    print("That is not in the list.")


