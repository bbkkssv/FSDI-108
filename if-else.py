"""

if-else statement

An if-else statement in Python is a conditional control structure that lets you decide which block of code to run depending on whether a condition is True or False.

The if block runs only if the condition evaluates to True.
If the condition is False, the else block runs instead.
You can also add elif (else if) blocks to check multiple conditions in sequence.

if condition:
    - Code block runs if condition is True
elif another_condition:
    - Code block runs if the first conditions is False and this condition is True
else:
    - Code block runs if none of the above conditions are True
"""

x = -7

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

    # nested if statements
if x > 0:
    if x < 20:
        print("x is a positive number less than 20")


# combining conditions
age = 18

if age >=18 and age<=21:
    print("You are between 18 and 21 years old")

"""
Mini-challenge

1. Ask the user to enter a number from 0-100 and store in a variable called "score"
2. If the score is under 90 or above, print "Grade: A"
3. If the score is between 80-89, print "Grade: B"
4. If the score is between 70-79, print "Grade: C"
5. Otherwise, print "Grade F"

"""


print("-------- Mini-Challenge: If-Else --------")

score = int(input("Enter score from 0-100: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")   
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")



"""
Mini-challenge

1. Ask the user to enter today's temperature in fahrenheit and store it in a variable called temperature
2. Use if-elif-else statements to classify the temperature:
    If temperature >= 86, print "It's hot outside!"
    If temperature >=68 and temperature < 86, print "The weather is nice"
    If temperature is >=50 and temperature <68, print "It's a bit chilly"
    Otherwise, print "It's cold!"

"""

temperature = int(input("Enter today's temperature in Fahrenheit: "))
if temperature >= 86:
    print("It's hot outside!")
elif temperature >= 68:
    print("The weather is nice")
elif temperature >= 50:
    print("It's a bit chilly")  
else:
    print("It's cold!")

    