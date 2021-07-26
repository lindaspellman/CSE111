# Video: Introducing Functions

# If you're running the same code over and over again
# don't copy and paste, put it into a function
# By moving the code to a function, you reduce rework
# and the chance of introducing bugs when you change the 
# code you had copied

# Import the datetime class from datetime library
from datetime import datetime
# print the current time
def print_time():
    print("task completed")
    # Now I don't need the extra datetime prefix
    print(datetime.now())
    print()

first_name = "Susan"
print_time()

for x in range(0,10):
    print(x)
print_time()

# What if I want a different message displayed?

first_name = "Linda"
print("first name assigned")
print(datetime.now())
print()

for x in range(0,10):
    print(x)
    print("loop completed")
    print(datetime.now())
    print()

# Pass the task name as a parameter

def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = "Linda"
print_time("first name assigned")

for x in range(0,10):
    print(x)
print_time("loop completed")

# Here's another example where the code looks different
# but we are doing the same logic over and over

first_name = input("Enter your first name ")
first_name_initial = first_name[0:1]
last_name = input("Enter your last name ")
last_name_initial = last_name[0:1]

print("Your initials are " + first_name_initial \
    + last_name_initial)

# I can still use a function, but this time my function
# returns a value

def get_initial(name):
    initial = name[0:1].upper() # If you need to change 
    # something you only have to change it in one place
    return initial # return always passes back a value

first_name = input("Enter your first name: ")
first_name_initial = get_initial(first_name)

last_name = input("Enter your last name: ")
last_name_initial = get_initial(last_name)

print("Your initials are: " + first_name_initial /
    + last_name_initial)

# Functions that return values allow clever code,
# but you might trade readability for less code

def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("Your initials are: " + get_initial(first_name) /
    + get_initial(last_name))

# Functions make your code more readable and easier to
# maintain
# Alwaygs add comments to explain the purpose of your
# functions
# Functions must be declared before the line of code
# where the function is called


# Video: Parameterized Functions

def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

# Ask for someone's name and return initials
first_name = input("Enter your first name: ")
first_name_initial = get_initial(first_name, False)
# pass arguments in same order parameters are declared in

print("Your initial is: " + first_name_initial)

# You can specify a default value for a parameter

def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input("Enter your first name: ")
first_name_initial = get_initial(first_name)

print("Your initial is: " + first_name_initial)

# Named notation in parameters - can specify in any order

def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input("Enter your first name: ")
first_name_initial = get_initial(force_uppercase=True,\
    name=first_name)
    # high readability

print("Your initial is: " + first_name_initial)

# example of named notation readability

def error_logger(error_code, error_severity, log_to_db, \
    effor_message, source_module):
    print("Oh no error: " + error_message)
    # Imagine code here that logs our error to a database
    # or file

first_number = 10
second_number = 5
if first_number > second_number:
    error_logger(error_code=45, error_severity=1, 
    log_to_db=True, error_message="Second number greater than first",
    source_module="my_math_method")


# MORE NOTES

# body of a function: statements inside
    # body begins with docstring: triple quoted string that describes the func's purpose parameters and return value
    # may contain as many statements as you want, but a good idea is to limit funcs to less than 20 lines of code

# Example 3

# import math

# Define a func named print_cylinder_volume.
def print_cylinder_volume():
    """Compute and print the volume of a cylinder."""

    # Get the radius and height from the user.
    radius = float(input("Please enter the radius of a cylinder: "))
    height = float(input("Please enter the height of a cylinder: "))

    # Compute teh volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Print the volume of the cylinder.
    print(volume) 

print_cylinder_volume() # can be called this this b/c no parameters

# Example 4 - doesn't get radius and height from user, instead accepts two parameters

# import math

# Define a function named print_cylinder_volume.
def print_cylinder_volume(radius, height):
    """Compute and print the volume of a cylinder.

    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    """
    # Compute the volume of the cylinder 
    volume = math.pi * radius**2 * height 

    # Print the volume of the cylinder.
    print(volume) 

print_cylinder_volume(2.5, 4.1) # must be called like this

# When a func returns a result, we usually write code to
# store that returned result in a variable to use later

# Example 5

# import math

# Define a function named computer_cylinder_volume.
def compute_cylinder_volume(radius, height):
    """Compute and return the volume of a cylinder.

    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the volume of the cylinder
    """
    # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Return the volume of the cylinder so that the
    # volume can be used somewhere else in the program.
    return volume 

volume = compute_cylinder_volume(2.5, 4.1)

# Example 6

# import math

# Define a function that accepts two parameters.
def compute_cylinder_volume(radius, height):
    """Compute and print the volume of a cylinder.

    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the volume of the cylinder
    """
    # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Return the volume of the cylinder so that the
    # volume can be used somewhere else in the program.
    # The returned result will be available wherever
    # this function was called.
    return volume

# Define the main function.
def main():
    # Create two variables to hold the radius and height.
    radius = float(input("Enter the radius in centimeters: "))
    height = float(input("Enter the height in centimeters: "))

    # Call the compute_cylinder_volume function and store
    # its return value in a variable to use later.
    volume = compute_cylinder_volume(radius, height)

    if volume < 1000:
        print(f"That cylinder holds {volume} cubic")
        print("centimeters, which is less than a liter.")
    elif volume > 1000:
        print(f"That cylinder holds {volume} cubic")
        print("centimeters, which is more than a liter.")
    else:
        print(f"That cylinder holds {volume} cubic")
        print("centimeters, which is exactly one liter.")

# Start this program by
# calling the main function.
main()

# Example 7

# Define the main function.
def main():
    # Create two variables to hold the radius and height.
    radius = float(input("Enter the radius in centimeters: "))
    height = float(input("Enter the height in centimeters: "))

    # Call the compute_cylinder_volume function
    # and immediately print its return value.
    print( compute_cylinder_volume(radius, height) )

    # Call the compute_cylinder_volume function again
    # and use its return value in an if statement.
    if compute_cylinder_volume(radius, height) < 1000:
        print("That cylinder holds less than a liter.")
    elif compute_cylinder_volume(radius, height) > 1000:
        print("That cylinder holds more than a liter.")
    else:
        print("That cylinder holds exactly one liter.")


# Start this program by
# calling the main function.
main()

# Example 8

# Define the main function.
def main():
    # Create two variables to hold the radius and height.
    radius = float(input("Enter the radius in centimeters: "))
    height = float(input("Enter the height in centimeters: "))

    # Call the compute_cylinder_volume function and store
    # its return value in a variable to use later.
    volume = compute_cylinder_volume(radius, height)

    print(f"The volume is: {volume} cubic centimeters.")

    if volume < 1000:
        print("That cylinder holds less than a liter.")
    elif volume > 1000:
        print("That cylinder holds more than a liter.")
    else:
        print("That cylinder holds exactly one liter.")


# Start this program by
# calling the main function.
main()

# The most reusable functions are ones that take parameters, 
# perform calculations, and return a value but do not 
# perform user input and output.
# If a func performs user input/output it is not
# reusable in other programs