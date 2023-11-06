# Lists
my_list = ["a", "b", "c"]
data = ["i", 1, True, "x"]
num = [1, 4, 7, 9, 7, 4, 7, 6, 9, 0, 9, 7, 5, 3, 2, 1, 1]
users = ["Dan", "Mo", "Josh", "Doc"]

# Accessing list elements
print(my_list[1])  # Access the element at index 1
print(my_list.index("a"))  # Find the index of "a"

# Slicing and reversing
print(my_list[0:2])  # Get a sublist from index 0 to 1 (exclusive)
print(my_list[::-1])  # Reverse the list

# Length of a list
print(len(my_list))

# Adding elements to a list
my_list.append("d")  # Append "d" to the end of the list
print(my_list)

my_list += ["e"]  # Concatenate the list with ["e"]
print(my_list)

my_list.extend(["f", "g"])  # Extend the list with ["f", "g"]
print(my_list)

my_list.extend(data[0])  # Extend the list with individual elements of data[0]
print(my_list)

# Inserting elements into a list
my_list.insert(0, "alphabet")  # Insert "alphabet" at index 0
print(my_list)

my_list[1:1] = ["|"]  # Insert "|" at index 1
print(my_list)

my_list[1:3] = [":"]  # Replace elements at index 1 and 2 with ":"
print(my_list)

# Removing elements from a list
data.remove("x")  # Remove "x" from data list
print(data)

print(my_list.pop())  # Remove and return the last element of my_list
print(my_list)

del my_list[0]  # Delete the element at index 0
print(my_list)

# del data
# Error: data is not defined because it's deleted

data.clear()  # Remove all elements from data list
print(data)

# Sorting and reversing
num.sort()  # Sort num in ascending order
print(num)

users.sort(key=str.lower)  # Sort users in alphabetical order, ignoring case
print(users)

num.reverse()  # Reverse the order of elements in num
print(num)

# num[::-1]
# print(num)

# num.sort(reverse=True)
# print(num)

print(sorted(num, reverse=True))  # Sort num in descending order using sorted()
print(num)

# Making a copy of the same list
# 1. Using the copy() method
numcopy = num.copy()
print(numcopy)

# 2. Using the list() constructor
mynum = list(num)
print(mynum)

# 3. Using slicing
mycopy = num[:]
mycopy.sort()
print(mycopy)

print(num)

print(type(num))  # Check the type of num

# Creating a list with different data types
new_list = list([1, "Nill", False])
print(new_list)

# Tuples
my_tuple = tuple(("Dave", 42, True))  # Create a tuple with three elements
another_tuple = (1, 4, 2, 8, 2, 2)  # Create a tuple using parentheses

print(my_tuple)
print(type(my_tuple))
print(another_tuple)
print(type(another_tuple))

lista = list(my_tuple)
lista.append("Nill")
new_tuple = tuple(lista)
print(new_tuple)

# unpack
(one, *two, hey) = another_tuple
print(one)
print(two)
print(hey)

print(another_tuple.count(2))
