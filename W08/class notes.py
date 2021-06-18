student = {"first_name": "Jennifer",
        "last_name": "smith",
        "phone": 2387598223,
        "i-number": 2398578294,
        "address": "w first e"}

print(student)

print(type(student))

print(student["first_name"])

for item in student:
    # print(student[item]) # print student at index/value of item # Output: the values of the keys
    # print(item) # prints keys

    print(f"{item}: {student[item]}")

# dictionary methods that are different from the list methods - look up on w3schools.com
x = ["key1", "key2", "key3"]
y = 0

thisdict = dict.fromkeys(x,y)
print(thisdict)
# returns a dictionary with the specified keys and the 
# specified value

