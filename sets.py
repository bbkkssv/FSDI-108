"""
Sets in Python

A set is a built-in data structure in Python used to store unique items.
sets are unordered, unindexed and do not allow duplicate values.

my_set = {item1, item2, item3, ...}

"""

fruit = {"apple", "banana", "cherry"}
print(fruit)

fruits = {"apple", "banana", "cherry", "apple"} # duplicate "apple" will be ignored
print(fruits)
print("banana" in fruits) # Check membership
fruits.add("orange") # Add item
print(fruits)

fruits.update(["mango", "grape"]) # Add multiple items (square brackets)
print(fruits)

fruits.remove("banana") # Remove item (error if not found)
print(fruits)

fruits.discard("kiwi") # Remove item (no error if not found)
print(fruits)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))       # Union
print(set1.intersection(set2)) # Intersection
print(set1.difference(set2))   # Difference
print(set1.symmetric_difference(set2)) # Symmetric Difference

# length
print(len(fruits)) # Number of unique items in the set

# copying sets
new_set = set1.copy()
print(new_set)

# clearing sets
set1.clear()
print(set1)