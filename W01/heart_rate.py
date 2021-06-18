# heart_rate.py
# 01 Checkpoint: Review Python
# By: Linda Spellman 4/21/21

max_beats = 0

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""

# Get the user's age as a string.
age = int(input("Please enter your age: "))

# Compute the slowest and fastest beneficial
# heart rates from the user's age.
max_range = 220 - age
fastest = max_range * 0.85
slowest = max_range * 0.65

# Use an f-string to create and print a message for the user to see.
print(f"When you exercise to strengthen your heart, you should keep your heart rate between {slowest:.0f} and {fastest:.0f} beats per minute.")
input("END")