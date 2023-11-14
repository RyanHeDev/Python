party_names = []

for _ in range(3):
    names = input("Enter the names of three people that you would like to invite to a party: ")
    party_names.append(names)

more_names = input("Do you want to enter more names? ")
more = True
while more:
    if more_names.lower() == "yes":
        for _ in range(3):
            names = input("Enter the names of three more people that you would like to invite to a party: ")
            party_names.append(names)
        more_names = input("Do you want to enter more names? ")
    elif more_names.lower() == "no":
        more = False
        print("Party guests:")
        for name in party_names:
            print(name)
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        more_names = input("Do you want to enter more names? ")
