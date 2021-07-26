"""Assertion statements - causes the computer to check if a comparison is true. 
When the computer checks the comparison, if the comparison is true, the computer 
will continue to execute the code in the program. However, if the comparison is false, 
the computer will raise an AssertionError, which will likely cause the program to terminate"""

"""Assert - inform the computer of comparisons that must be true in order for the program to run 
successfully"""

# EXAMPLE
def deposit(amount):
    # In order for this program to work correctly and
    # for the bank records to be correct, we must not
    # allow someone to deposit a zero or negative amount.
    assert amount >= 0
    # ect code...

"""If amount is less than or equal to zero -> AssertionError -> probable termination of program"""

"""A programmer can write any valid Python comparison in an assert statement. Here are a few examples from various unrelated programs:"""
    assert temperature < 0

    assert len(given_name) > 0

    assert balance == 0

    assert school_year != "senior"

# pytest - allows a programmer to write simple test functions that use the Python assert statement to verify that a function 
# returns a correct result. For example, if we want to verify that the built-in min function works correctly, 
# we could write an assert statement like this:

# For example, if we want to verify that the built-in min function works correctly, 
# we could write an assert statement like this:
    assert min(7, -3, 0, 2) == -3
# If the returned minimum value is not -3, the assert statement will raise an exception 
# which will cause pytest to print an error message.

# pytest - approx function: help compare floating numbers
    # EXAMPLE
    assert math.sqrt(5) == approx(2.24, 0.01)
    # The previous assert statement verifies that the value 
    # returned from math.sqrt(5) is within 1% (0.01) of 2.24

"""To test a function you should do the following:
 1. Write a function that is part of your normal Python program.
 2. Think about different parameter values that will cause the 
   computer to execute all the code in your function and 
   will possibly cause your function to fail or return 
   an incorrect result.
 3. In a separate Python file, write a test function that 
   calls your program function and uses an assert statement 
   to automatically verify that the value returned from your 
   program function is correct.
 4. Use pytest to run the test function.
 5. Read the output of pytest and use that output to 
   help you find and fix mistakes in both your program 
   function and test function."""