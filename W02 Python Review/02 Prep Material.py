# Calling Functions in Python

# very large comp programs = divide programs into parts
# can be divided into modules, classes, and functions

# Function: a group of statements (comp commands) that together
# perform one task
    # 4 broad types of functions in Python:
        # Built-in functions, standard library functions,
        # Third-party functions, user defined functions

# Build-in functions: input, int, float, str, len, range, abs
    # round, list, dict, open, print

# To call or invoke a func means to write code that causes
# the comp to execute the code that is inside that func
    # all types of functions called with its name and ()

# Example
name = input("Please enter your name: ") # parameter is (prompt)
print(f"Hello {name}")

# To correctly call a function you must know the following:
    # The name of the func
    # The parameters that the function takes
    # What the function does
        # all are normally available in online documentation

# Parameter: A piece of data that a function needs in order
# to complete its task

# Argument: The value that is passed through a parameter into
# a function
    # parameters are listed in a func's documentation, while
    # arguments are listed in a call to a func

# To write code that calls a function:
    # Type a new variable name and use the assignment operator
        # (=) to assign a value to the variable
    # Type a name of the function followed by a set of 
        # parantheses
    # B/w the parentheses, type arguments that the comp will
        # pass into the function through its paramenters

# More than one parameter to a function usually means
# writing the arguments in the same order as the parameters
# Example:
    # round(number, ndigits)
        # Return number rounded to ndigits precision after 
        # the decimal point. If ndigits is omitted or is None,
        # round returns the nearest integer to number
n = float(input("Please enter a number: "))
r = round(n, 2) # passes two arguments into the two parameters
print(r)

# when calling a func or method, some arguments are optional
# for some opt. arguments -> pass a named argument
    # Named Argument: An argument preceded by the name of
        # its matching parameter
# print(*objects, sep="", end="\n", file=sys.stdout, flush=False)
    # Print objects to the text stream file, separated by sep
    # and followed by end. sep, end, file and flush, if 
    # present, MUST be given as named arguments.
    # Example:
x = "sun"
y = "moon"
z = "stars"
print(x, y, z, sep="|", flush=True)

# Module: A collection of related functions
# Python standard library includes many modules which have more functions
# such as the math module - floor, ceil, squrt funcs, and random module
# which includes randint, choice, and shuffle functions
    # math.squrt(x)
        # Return the square root of x.
            # name of module is math
            # name of func is squrt
            # the func takes one parameter named x
            # the func computes & returns square root of a num
    # To use any code that is in a module, you MUST import
    # the module into your program & precede the func name
    # with the module name ---> module.func()
import math
r = math.sqrt(71)
print(r)

# Python is an object oriented lang---includes many classes & objects
    # Method: a func that belongs to a class or object - easy and common to call
        # similar to calling a func
        # except: to call a method we must type the name of 
        # the object & a period in front of the method name
# Get a string of text from the user.
text1 = input("Enter a motivational quote: ")

# Call the built-in len function to get
# the number of characters in the text.
length = len(text1)

# Call the string upper method to convert
# the quote to upper case characters.
text2 = text1.upper()

# Call the built-in print function to print
# the length of the text and the text in all
# upper case for the user to see.
print(length, text2)

# a method can receive arguments just like a func can, 
# but none are passed to the upper method in the example

# Template: To call a built-in func:
variable_name = function_name(arg1, arg2, ...argN)

# Template: To call a func from a module, import the module and write code
import module_name

variable_name = module_name.function_name(arg1, arg2, ...argN)

# Template: To call a method:
variable_name = object_name.method_name(arg1, arg2, ...argN)