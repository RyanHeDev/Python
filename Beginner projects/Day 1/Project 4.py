
# tip calculator

bill = float(input("What was the total bill? $"))

tip = float(input("What percentage tip would you like to give? 10,12, or 15? "))

people = float(input("How many people to split the bill? "))

percentage = tip / 100
amount = bill * percentage 
total = bill + amount 
bill_per_person = total/ people

final_amount = round(bill_per_person, 2)

print(f"Each person should pay:${final_amount}")
