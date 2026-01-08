"""
Loops

A for loop in Python is a control structure that lets you repeat a block of code for each item in sequence such as (list, string, tuple, dictionary or a range of numbers)

for variable in sequence:
    - Code block runs for each item in the sequence


"""

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


print("------------------------")

for letter in "Robert":
    print(letter)   

print("------------------------")

for number in range(2,6):  # 2-5
    print(number)   

print("------------------------")

for number in range(0,10,2):  # 0-8
    print(number)

print("------------------------")

"""
Mini-challenge

1. Ask the user to enter a number and store it in a variable called num
2. Use a for loop with range(1,11) to repeat 10 times (from 1 to 10)
3. Inside the loop, multiply num by the current loop value

"""

num = int(input("Enter a number: "))
for i in range(1,11):
    result = num * i
    print(f"{num} x {i} = {result}")



"""
While loops

A while loop repeats a block of code as long as a condition is True.

while condition:
    - Code block runs as long as condition is True

"""
print("----------------")

count = 1

while count <=5:
    print("Count is: ", count)
    count += 1
    