# Comment test

print("Hello, World!")

# ----- Variables and Concatenation -----
name = "Angela"
age = 28
print(name)  # Prints the variable value

print("My name is " + name + " and I am " + str(age))

first_name = "Michael"
middle_name = "John"
last_name = "Scott"
age = 46
print("My name is " + first_name + " " + middle_name + " " + last_name + " and I am " + str(age))

# ----- F-String (cleaner way to format strings)-----
print(f"hello")
print(f"My name is {first_name} {middle_name} {last_name} and I am {age} years old.")

# Multi-line f-string
print(f"""
My name is {first_name} {middle_name} {last_name}
and I am {age} years old.
""")

# MINICHALLENGE 1
"""
Create 4 variables: my_name, my_last_name, my_age, and my_favorite_technology.
Assign them your own information or mock data.

-Then, use an f-string to print a sentence like the following:
  "Hello my name is ___ ___, I am ___ years old and my favorite technology is ___."

- Personalize the values with your real data or fun mock data.
You can also add extra variables (like city or hobby) to make the sentence more creative.
"""

my_name = "Robert"
my_last_name = "Vinson"
my_age = 48
my_favorite_technology = "Python"
favorite_color = "blue"

print(f"Hello my name is {my_name} {my_last_name}, I am {my_age} years old and my favorite technology is {my_favorite_technology}. Favorite color is {favorite_color}. I also like french fries")

# ----- Input Function -----
user_name = input("Enter your name: ")
print(f"Hello {user_name}!")

user_age = int(input("Enter your age: "))
print(f"You are {user_age - 1} years old.")



