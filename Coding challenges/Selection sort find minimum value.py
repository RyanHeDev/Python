# selection sort
# find minimum value and replace it with the first value

def find_min(numbers):
    min_index = 0
    for x in range(len(numbers)):
        if numbers[x] < numbers[min_index]:
            min_index = x
    return numbers[min_index]
numbers = [3,2,1,5,4]
min_value = find_min(numbers)
print(f"The minimum value is {min_value}")
