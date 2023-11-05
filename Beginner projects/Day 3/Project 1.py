
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names separated by a comma: ")
names = namesAsCSV.split(", ")

random.shuffle(names)
person_who_will_pay = names[0]
print(f"{person_who_will_pay} is going to buy the meal today.")
