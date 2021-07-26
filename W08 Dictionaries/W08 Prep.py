bad_guys = {
    "daredevil": "kingpin",
    "x-men": "apocalypse",
    "batman": "bane"
}
print(bad_guys["batman"])
print(bad_guys["x-men"])

bad_guys["deadpool"] = "evil deadpool"
print(bad_guys["deadpool"]) 

bad_guys["x-men"] = "juggernaut"

print(bad_guys["x-men"])
del(bad_guys["x-men"])
print(bad_guys)

# can't access dictionaries with an index number
# python expects a key. You can use integers as keys!

d = {
    0: "plane",
    1: "train"
}
print(d[0]) # 0 is a key, not an index
# Output: "plane"

# No key can appear more than once in a dictionary. 
#   Values within a dictionary do not have to be unique.

### Question: Can you use variables as keys? 
#       Sort of?

# Example 1

def main():
    # Create a dictionary with student IDs as
    # the keys and student names as the values.
    students = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Michelle Davis",
        "10-450-1203": "Jorge Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Michelle Davis"
    }

    # Add an item to the dictionary. 
    # Follow this template: dictionary_name[key] = value
    students["81-298-9238"] = "Sama Patel"

    # Remove an item from the dictionary.
    students.pop("61-315-0160")

    # Get the number of items in the dictionary and print it.
    length = len(students)
    print(length)

    # Print the entire dictionary.
    print(students)

    # Get a student ID from the user.
    id = input("Enter a student ID: ")

    # Check if the student ID is in the dictionary.
    if id in students:

        # Find the student ID in the dictionary and
        # retrieve the corresponding student name.
        # Follow template: value (/variable?) = dictionary_name[key]
        name = students[id]

        # Print the student's name.
        print(name)
    else:
        print("No such student")


# Call main to start this program.
if __name__ == "__main__":
    main()

# simple value: doesn't contain parts, such as an integer
# Compoud Value: a value that has parts, such as a list
    # Example 2 shows a students dictionary where each 
    # value is a Python list. Because each list contains 
    # multiple parts, we say that the dictionary stores 
    # compound values

# Example 2

def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students = {
        # student_ID: [given_name, surname, email_address, credits]
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Michelle", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Jorge", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Michelle", "Davis" "dav19008@byui.edu", 0]
    }

### Processing All Items

# Example 5

def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students = {
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Michelle", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Jorge", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Michelle", "Davis", "dav19008@byui.edu", 0],
        "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
    }

    # These are the indexes of the elements in the value lists.
    GIVEN_NAME_INDEX = 0
    SURNAME_INDEX = 1
    EMAIL_INDEX = 2
    CREDITS_INDEX = 3

    total = 0

    # For each item in the list add the number
    # of credits that the student has earned.
    for item in students.items():
        key = item[0]
        value = item[1]
    # OR write the for loop more simply this way to combine the three lines of code:
    for key, value in students.items():

        # Retrieve the number of credits from the value list.
        credits = value[CREDITS_INDEX]

        # Add the number of credits to the total.
        total += credits

    print(f"Total credits earned by all students: {total}")


# Call main to start this program.
if __name__ == "__main__":
    main()

### Converting b/w Lists and Dictionaries
    # convert two lists into a dictionary by using the 
        # built-in zip and dict functions
        ## first list ---> the keys
        ## second list ---> the values
    # convert a dictionary into two lists by using the 
        # keys and values methods and the built-in list
        # function

# Example 6

def main():
    # Create a list that contains five student numbers.
    numbers = ["42-039-4736", "61-315-0160",
            "10-450-1203", "75-421-2310", "07-103-5621"]

    # Create a list that contains five student names.
    names = ["Clint Huish", "Michelle Davis",
            "Jorge Soares", "Abdul Ali", "Michelle Davis"]

    # Convert the numbers list and names list into a dictionary.
    student_dict = dict(zip(numbers, names))

    # Print the entire student dictionary.
    print(student_dict)

    # Convert the student dictionary into
    # two lists named keys and values.
    keys = list(student_dict.keys())
    values = list(student_dict.values())

    # Print both lists.
    print(keys)
    print(values)


# Call main to start this program.
if __name__ == "__main__":
    main()