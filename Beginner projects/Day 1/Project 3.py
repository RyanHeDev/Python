
# Your life in weeks 
age = int(input("What is your current age? "))

# Time left
time = 90 - age 
days = 365 * time
weeks = 52 * time
months = 12 * time

print(f" You have {days}, {weeks} and {months} left ")
