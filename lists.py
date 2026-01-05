# Lists in Python

"""
A list is a built-in data structure in Python used to store multiple items in a single variable.
Lists are ordered, mutable, and allow duplicated values.

variable_name = [item1, item2, item3, ...]
"""

my_list = [10, 20, 30, 40]
print(my_list)

mixed_list = [1, "apple", 3.5, True]
print(mixed_list)

# Accessing elements by index
print(my_list[0])   # First element: 10
print(my_list[-1])  # Last element: 40

# Slicing lists
print(my_list[1:3])  # Elements from index 1 to 2: [20, 30]

# Modifying elements
my_list[0] = 15
print(my_list)  # [15, 20, 30, 40]

# Adding elements
my_list.append(50)      # Add to end
my_list.insert(1, 25)   # Insert at index 1
print(my_list)

# Removing elements
my_list.remove(25)      # Remove by value
my_list.pop()           # Remove last element
print(my_list)

# More examples with fruits list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Adding items
fruits.append("orange") # adds to end
print(fruits)

fruits.insert(1, "kiwi") # inserts at index 1
print(fruits)

# Removing items
fruits.remove("apple") # removes by value
print(fruits)

fruits.pop() # remove last item
print(fruits)

del fruits[0] # removes item at index 0
print(fruits)

# List methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()          # Sort ascending
print(numbers)

numbers.reverse()       # Reverse order
print(numbers)

# List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # Concatenate
print(combined)

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Length and membership
print(len(my_list))     # Number of elements
print(30 in my_list)    # Check if 30 is in list

# List length
print(len(fruits))
print(len(["colors", True, "Python", 3.1416, 2025]))

"""
Mini-Challenge: Favorite Movie

Create a list of 4 favorite movies
Replace the second movie (index 1) with a new one
Step 3: Remove one movie
Option A: Remove by value
Option B: Remove by index
"""

favorite_movies = ["Avengers", "Spider-Man", "Black Panther", "Iron Man"]
print("Original movies:", favorite_movies)


favorite_movies[1] = "Thor"
print("After replacement:", favorite_movies)


favorite_movies.remove("Black Panther")
print("After removing by value:", favorite_movies)


# -------- Assignment #2 --------