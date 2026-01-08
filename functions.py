"""
Functions

A function is a block of code that only runs when it is called.
We can pass data to functions(parameters). and they can return data as a result

def function_name(parameters):
    - code block
    return result
"""

def my_function():
    print("This is a function") # this line runs when the funciton is called

# calling the function
my_function()


def other_function():
    print("This is another function")

other_function()



def hello():
    cohort = 63
    print("Hello Cohort#", cohort)


hello()
hello()
hello()


def get_full_name(first_name, last_name):
    return f"Hello {first_name} {last_name}" # sends back the full name as text

full_name = get_full_name("Leo", "Miranda")
print(full_name)


# default parameter
def greet(name="Student"):
    print(f"Hello, {name}, welcome to class.")

greet()
greet("Pam")
greet("Angela")


