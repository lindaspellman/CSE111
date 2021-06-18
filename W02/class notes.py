# if you compare two variables in print() ---> boolean variable

x = 5
y = 6

number_list = [1,2,3,4,5]

print(x < y or x == 5) # True

x = x + 1
# is the same as
x += 1
# x varaible is reassigned
# -=, *=, /=, %= are also valid short-cuts, in addition to any other short cuts

# Repeating Commands/Traversing Data
# loops for any time you need to repeat something
    # happy path: user did the correct thing

# i is an example of something inside a list, creating a new variable in a for loop
x = 10
x += 1
for i in range(0, x):
    print(i)

x = 10
i = 0
while i < x:
    print(i)
    i += 2 # increments the numbers as are listed

course = "CSE111 " # 7 total spaces to loop through
x = 0 # The variable that we are adding to
for i in range(0, len(course)):
    if course[i].isalpha(): # .isalpha() returns True or False if course[i] is an alphabetical letter or not
        x += 2
    else:
        x += 1
print(x)

# Storage Data Sets
    # Tuples are immutable (cannot change after creation)
    # Lists mutable
    # add item to list using insert() and append()
    # replace item in list and retrieve using index operators([ ])
    # remove item from list using del(), pop(), remove() funcs
    # find item in list using an index ([ ])
    # find num of items in list using len() func

# How to use and define a list
Classes = ["CSE111", "CSE130", "CSE280"]
Classes.append("MATH316")
print(Classes[0])
Classes.insert(0, "CS124")
print(Classes[0])
print(Classes)
Engineers = ["Software", "Computer", "Electrical"]
Engineers += Classes
print(Engineers)
Engineers = Classes # interchanged with other lists
print(Engineers)