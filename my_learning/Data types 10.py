nums = []
count = 0

for i in range(3):
    number = int(input("Enter a number: "))
    nums.append(number)
    print(nums)
    count += 1

more_nums = input("Do you want to last number you entered to be saved? ").lower()

if more_nums == "no":
    nums.remove(number)
    print(nums)
