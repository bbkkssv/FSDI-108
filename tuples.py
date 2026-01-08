"""
Tuples in Python

A tuple is a built-in data structure in Python, like a list.
tuples can store multiple items, but they are immutable.

my_tuple = (item1, item2, item3, ...)
"""

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

print(my_tuple[0])  # first item
print(my_tuple[2])  # third item

# length
print(len(my_tuple))

# single-item tuple
single = ("apple")
print(type(single))
print(single)

correct = ("apple",)
print(type(correct))
print(correct)

print(my_tuple[0:2])  # slicing

# Nested tuples

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
combine = (tuple1, tuple2)
print(combine)

temp_list = list(my_tuple)  # Convert to list
print(temp_list)

temp_list.append("orange")  # Modify list
my_tuple = tuple(temp_list)  # Convert back to tuple
print(my_tuple)

"""
Mini-Challenge:

1. Create a tuple called travel_bag with at least 5 items: "shirt", "socks", "pants", "jacket", "shoes".
2. Print the second and fourth items.
3. Make a new tuple called essentials with 3 must-have items.
"""
print("-------- Mini-Challenge: Tuples --------")

travel_bag = ("shirt", "socks", "pants", "jacket", "shoes")
print(travel_bag[1])  # second item
print(travel_bag[3])  # fourth item

essentials = ("passport", "wallet", "phone")
print(essentials)

