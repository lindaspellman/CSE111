# 01 Prove Milestone: Review Python
# By Linda Spellman 4/22/21
# import math in order to access math.pi
import math

# Description of program's purpose
print("File Name: tire_volume")
print("This program computes and outputs the volume of a tire")
print("based on its width, aspect ratio, and the diameter")
print("of the wheel it is meant to fit.")
print()
# start = input("Do you want to start? (Yes/No) ")
start = ""
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
    start = input("Do you want to start again? (Yes/No) ")

# input function put at end, so that the program will not exit immediately
input("")