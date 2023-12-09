# selection sort

def selection_sort(numbers):
    for x in range(len(numbers) - 1):
        min_index = x
        for y in range(x + 1, len(numbers)):
            if numbers[y] < numbers[min_index]:
                min_index = y
        numbers[x], numbers[min_index] = numbers[min_index], numbers[x]
    
    
    
numbers = [3,2,1,5,4]
print(numbers)
selection_sort(numbers)
print(numbers)

# A pythonic way to check if a list is sorted without relying on using python own sorting methods to compare
print(all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1)))
