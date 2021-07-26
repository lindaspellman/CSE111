# 02 Prove: Calling Functions
# File Name: tire.volume
# By Linda Spellman 5/1/21

# import math in order to access math.pi
import math

# Import the datatime module so that
# it can be used in this program.
from datetime import datetime

# Call the now() method to get the current date and
# time as a datetime object from the computer's clock.
today = datetime.now(tz=None)
start = ""

# Description of program's purpose
print("File Name: tire_volume")
print("This program computes and outputs the volume of a tire")
print("based on its width, aspect ratio, and the diameter")
print("of the wheel it is meant to fit.")
print()

while start.capitalize() != "No":
    # Ask for data
    width_tire = int(input("Enter the width of the tire in mm: "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire: "))
    diameter_wheel = int(input("Enter the diameter of the wheel in inches: "))
    print()
    # formula through which the data will be computed
    volume = math.pi * width_tire**2 * aspect_ratio * (width_tire * aspect_ratio + 2540 * diameter_wheel) / 10000000

    # description of end product of computation
    print(f"The approximate volume is {volume:.1f} cubic cm.")
    print()
    purchase = input("Do you want to buy tires with the dimensions that you entered? ")
    
    if purchase.capitalize() == "Yes":
        phone = input("What is your phone number? ")
        print()
    
        with open("volumes.txt","at") as volumes:
            print(file=volumes)
            print(f"{today}, {width_tire}, {aspect_ratio}, {diameter_wheel}, {volume}, {phone}", file=volumes)
            print("Today is " + str(today.day))

    elif purchase.capitalize() == "No":
        print()
        
        with open("volumes.txt","at") as volumes:
            print(file=volumes)
            print(f"{today}, {width_tire}, {aspect_ratio}, {diameter_wheel}, {volume}", file=volumes)
    
    print("Today is " + str(today))
    start = input("Do you want to start again? (Yes/No) ")
    print()

# input function put at end, so that the program will not exit immediately
input("")