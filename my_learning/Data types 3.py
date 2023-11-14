
subjects = ["maths","physics","chemestry","sport","cybersecurity","engineering"]

print(subjects)

user = input("Which one do you hate: ").lower()

subjects.remove(user)
print(subjects)
