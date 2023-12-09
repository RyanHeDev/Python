def linear_search(data, target):
    # enumerate gives both the index and value in a data type such as a list.
    for index, element in enumerate(data):
        if element == target:
            return index
    return -1

data = [4, 5, 2, 7, 1, 8]
target = 1
result = linear_search(data, target)

if result == -1:
    print("Item not found")
else:
    print(f"Item found at position {result}.")
