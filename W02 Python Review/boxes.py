# 02 Prep: Checkpoint
# File Name: boxes.py
"""
A manufacturing company needs a program that will help its employees
pack manufactured items into boxes for shipping. Write a Python program
named boxes.py that asks the user for two integers:  1) the number of
manufactured items and 2) the number of items that the user will pack
per box. Your program must compute and print the number of boxes
necessary to hold the items. This must be a whole number. Note that the
last box may be packed with fewer items than the other boxes.
"""

import math

manu_items = int(input("How many manufactured items are there? "))
items_per_box = int(input("How many items will you pack per box? "))

box_need = math.ceil(manu_items / items_per_box)

remainder = manu_items % items_per_box

print(f"For {manu_items} items, packing {items_per_box} items in each box,"
f" you will need {box_need:.0f} boxes.")

print(f"The last box will be packed with {remainder} items.")