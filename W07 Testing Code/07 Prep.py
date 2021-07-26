# Lists - mutable (can be changes after creation)
# element - each item in a list, stored at a unique index (always an integer, starts at 0)
# [] = new empty list

# Example 1

def main():
    # Create a list that contains five words.
    colors = ["yellow", "red", "green", "yellow", "blue"]

    # Print the length of the list.
    length = len(colors)
    print(length)

    # Print the element that is stored
    # at index 2 in the colors list.
    print(colors[2])

    # Change the element that is stored at
    # index 3 from "yellow" to "purple".
    colors[3] = "purple"

    # Print the entire colors list.
    print(colors)


# Call main to start this program.
if __name__ == "__main__":
    main()

### Add item to list using INSERT and APPEND methods
# can determine if element is in a list using the Python
    # membership operator ---> IN
# can find the index of item within list using INDEX method
# remove item from list by using DEL, POP, and REMOVE

# Example 2

def main()
    # Create an empty list that will hold fabric names.
    fabrics = []

    # Add three elements at the end of the fabrics list.
    fabrics.append("velvet")
    fabrics.append("denim")
    fabrics.append("gingham")

    # Insert an element at the beginning of the fabrics list.
    fabrics.insert(0, "chiffon")

    # Determine if gingham is in the fabrics list.
    if "gingham" in fabrics:
        print("gingham is in the list.")
    else:
        print("gingham is NOT in the list.")

    # Get the index where velvet is stored in the fabrics list.
    i = fabrics.index("velvet")

    # Replace velvet with taffeta.
    fabrics[i] = "taffeta"

    # Remove the last element from the fabrics list.
    fabrics.pop()

    # Remove denim from the fabrics list.
    fabrics.remove("denim")

    # Get the length of the fabrics list and print it.
    n = len(fabrics)
    print(f"The fabrics list contains {n} elements.")


# Call main to start this program.
if __name__ == "__main__":
    main()

### Compound Lists - a list that contain other lists
    # used to store lots of related data

# How to create a compound list, retrieve an inner list
    # from the compound list, and retrieve an individual
    # number from the inner list

# Example 3

def main():
    # Create a compound list that stores smaller lists.
    apple_tree_data = [
        # [year_planted, height, girth, fruit_amount]
        [2012, 2.7, 3.6, 70.5],
        [2012, 2.4, 3.7, 81.3],
        [2015, 2.3, 3.6, 62.7],
        [2016, 2.1, 2.7, 42.1]
    ]

    # These are the indexes of each
    # element in the inner lists.
    YEAR_PLANTED_INDEX = 0
    HEIGHT_INDEX = 1
    GIRTH_INDEX = 2
    FRUIT_AMOUNT_INDEX = 3

    # Retrieve one inner list from the compound list.
    one_tree = apple_tree_data[2]

    # Retrieve one value from the inner list.
    height = one_tree[HEIGHT_INDEX]

    # Print the tree's height.
    print(height)


# Call main to start this program.
if __name__ == "__main__":
    main()

### Repetition
# for loop - iterates over a range of numbers, such as
    # range(3, 10) or a sequence, such as a list
# while loop - repeats while some condition is true

# Example 4

def main():
    # Count from zero to nine by ones.
    for i in range(10):
        print(i)

    # Count from zero to eight by twos.
    for i in range(0, 10, 2):
        print(i)

    # Count from 100 down to 70 by three.
    for i in range(100, 69, -3):
        print(i)


# Call main to start this program.
if __name__ == "__main__":
    main()

# BREAK statement - causes a loop to end early

# Example 5 - break statement causes for loop to
    # terminate early before summing

def main():
    sum = 0

    # Get ten or fewer numbers from the user and add them
    # together. Notice that this loop uses underscore (_) as
    # the counting variable, which is a valid variable name.
    # Many programmers use underscore to indicate that the
    # variable will not be used within the body of the loop.
    for _ in range(10):
        n = float(input("Please enter a number: "))
        if n == 0:
            break
        sum += n
    print(sum)


# Call main to start this program.
if __name__ == "__main__":
    main()

# Example 6
    # there is a for loop that processes all the elements 
    # in a list. The code in the body of the for loop is 
    # very small and simply prints an element from the 
    # list. However, we can write as much code as we need 
    # in the body of a loop to repeatedly perform all sorts 
    # of computations for each element in the list.

def main():
    # Create a list.
    colors = ["red", "orange", "yellow", "green", "blue", "indigo"]

    # Use a for loop to print each element in the list.
    # Of course, the code in the body of a loop can do
    # much more with each element than simply print it.
    for color in colors:
        print(color)


# Call main to start this program.
if __name__ == "__main__":
    main()

### Values and References - values are assigned to variables
    # differently based on their data type

# Example 7

def main():
    x = 17
    y = x
    print(f"Before changing x: x {x}  y {y}")
    x += 1
    print(f"After changing x:  x {x}  y {y}")

# Call main to start this program.
if __name__ == "__main__":
    main()

# > python example_7.py
# Before changing x: x 17  y 17
# After changing x:  x 18  y 17

# Example 8: contains two variables named lx and ly that 
    # each refer to a list. This program is similar to the 
    # previous program, but it has two lists instead of two 
    # integers.

def main():
    lx = [7, -2]
    ly = lx
    print(f"Before changing lx: lx {lx}  ly {ly}")
    lx.append(5)
    print(f"After changing lx:  lx {lx}  ly {ly}")

# Call main to start this program.
if __name__ == "__main__":
    main()

# > python example_8.py
# Before changing lx: lx [7, -2]  ly [7, -2]
# After changing lx:  lx [7, -2, 5]  ly [7, -2, 5]

"""From examples 7 and 8, we learn that when a computer 
executes a Python statement to assign the value of a 
boolean, integer, or float variable to another variable 
(y = x), the computer copies the value of one variable 
into the other. However, when a computer executes a 
Python statement to assign the value of a list variable 
to another variable (ly = lx), the computer does not 
copy the value but instead copies the reference so that 
both variables refer to the same value in memory.

The fact that the computer copies the value of some data 
types (boolean, integer, float) and copies the reference 
for other data types (list and others) has important 
implications for passing arguments into functions. 
Consider the Python program in example 9 with two functions
 named main and modify_args."""

# Example 9

def main():
    print("main()")
    x = 5
    lx = [7, -2]
    print(f"Before calling modify_args(): x {x}  lx {lx}")

    # Pass one integer and one list
    # to the modify_args function.
    modify_args(x, lx)

    print(f"After calling modify_args():  x {x}  lx {lx}")


def modify_args(n, alist):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters:
        n - A number
        alist - A list
    Return: nothing
    """
    print("   modify_args(n, alist)")
    print(f"   Before changing n and alist: n {n}  alist {alist}")

    # Change the values of both parameters.
    n += 1
    alist.append(4)

    print(f"   After changing n and alist:  n {n}  alist {alist}")


# Call main to start this program.
if __name__ == "__main__":
    main()

# > python example_9.py
# main()
# Before calling modify_args(): x 5  lx [7, -2]
    # modify_args(n, alist)
    # Before changing n and alist: n 5  alist [7, -2]
    # After changing n and alist:  n 6  alist [7, -2, 4]
# After calling modify_args():  x 5  lx [7, -2, 4]"""

"""Modifying an integer parameter changes the integer 
within the called function only. However, modifying a 
list parameter changes the list within the called function 
and within the calling function. Why? Because when a 
computer passes a boolean, integer, or float variable to 
a function, the computer copies the value of that variable 
into the parameter of the called function. However, when 
a computer passes a list variable to a function, the 
computer copies the reference so that the original variable 
and the parameter both refer to the same value in memory."""

# lists are passed into functions by reference in order
    # to save space/avoid making unneccessary copies