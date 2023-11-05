
print("Welcome to the match checker")

name_one = input("What is your name? \n").lower()
name_two = input("What is their name? \n").lower()

combine_names = name_one + name_two
t = combine_names.count("t")
r = combine_names.count("r")
u = combine_names.count("u")
e = combine_names.count("e")

true = t + r + u + e

f = combine_names.count("f")
r = combine_names.count("r")
i = combine_names.count("i")
e = combine_names.count("e")
n = combine_names.count("n")
d = combine_names.count("d")

friend = f + r + i + e + n + d

score = int(str(true) + str(friend))


if (score < 10) or score > 90:
    print(f"Your score is {score}%. You go together like Coke and Mentos!")
elif (score >=40) or (score <= 50):
    print(f"Your score is {score}%. You are alright together.")
else:
    print(f"Your score is {score}%.")
