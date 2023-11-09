# Dictionaries:

# Two ways to make dicts
#1
band = {
        "vocals": "Plant",
        "guitar": "Page"
        
}
#2

band2 = dict(vocals="Plant", guitar="Page")
# printing
print("////////")
print(band)
print(band2)

# type and lenght
print("////////")
print(type(band))
print(len(band))

# Access items
#1
print("////////")
print(band["vocals"])
#2
print("////////")
print(band.get("guitar"))

#list all keys 
print("////////")

print(band.keys())
#list all values
print("////////")

print(band.values())

# list of key values as tuples
print("////////")

print(band.items())

# verify exists in dict 
print("////////")

print("guitar" in band)
print("pizza" in band)


# change values in dicts
print("////////")

band["vocals"] = "Coverdale"
# add items
print("////////")

band.update({"bass": "JPJ"})
print(band)

# remove items
print("////////")

print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)
print(band.popitem()) # tuple
print(band)

# delete and clear
print("////////")
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dicts

"""
# how to not copy them

band2 = band # creates a reference
print("Bad copy!")
print(band2)
print(band)

band2["drums"] = "Josh"
print(band)

"""

# how to create copies
print("////////")
band2 = band.copy()
band2["drums"] = "Josh"
print("Good copy!")
print(band)
print(band2)

# or use the dict() constructor function 
print("////////")
band3 = dict(band)
print("Good copy!")
print(band3)

# Nested dictionaries 
print("////////")
member1 = {
        "name": "Plant",
        "instrument": "vocals"
}

member2 = {
        "name": "Dan",
        "instrument": "guitar"
}

band = {
        "member1": member1,
        "member2": member2
}

print("////////")

print(band)
print(band["member1"]["name"])

# Sets
print("////////")
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print("////////")
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicates allowed
# it just ignores the duplicate
print("////////")
nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1 and False  is a dupe of 0
print("////////")
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# Check if a value is in a set
print("////////")

print(2 in nums)

# but you cannot refer to an element in the set with an index position or a key

# Add a new element to a set
print("////////")

nums.add(8)
print(nums)

# Add elements from one set to another
print("////////")
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples and dictionaries too.

# Merge two sets to create a new set
print("////////")

one = {1, 2, 3}
two = {4, 5, 6}

my_new_set = one.union(two)
print(my_new_set)

# Keep only the duplicates

print("////////")

one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)

# keep everything except the duplicates

one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)
