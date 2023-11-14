nums = []

for i in range(3):
    number = int(input("Enter a number: "))
    nums.append(number)

more_nums = input("Do you want to last number you entered to be saved? ").lower()

if more_nums == "no":
    nums.pop(2)
    print(nums)
