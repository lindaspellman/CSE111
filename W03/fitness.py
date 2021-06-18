"""
PROJECT: Fitness
CLASS: Cse111-01
EDITED BY: Andrew Stamm and team members
"""
 
# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime
 
def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = str(input("Please enter your gender (M or F): "))
    birthdate = str(input("Please enter your birthdate (YYYY-MM-DD): "))
    weight = float(input("Enter your weight in US pounds: "))
    height = float(input("Enter your height in US inches: "))
 
 
 # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index,
 # and basal_metabolic_rate functions as needed.
age = compute_age(birthdate)
weight_kg = kg_from_lb(weight)
height_cm = cm_from_in(height)
bmi = body_mass_index(weight_kg, height_cm)
bmr = basal_metabolic_rate(gender, weight_kg, height_cm, age)
 
 # Print the results for the user to see.
print(f"Age (years): {age}")
print(f"Weight (kg): {weight_kg:.2f}")
print(f"Height (cm): {height_cm:.2f}")
print(f"Body mass index: {bmi:.1f}")
print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")
 
def compute_age(birth):
    """Compute and return a person's age in years.
 
    Parameter birth: a person's birthdate stored as
    a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()
 
    # Compute the difference between today and the birthday in years.
    years = today.year - birthday.year
 
    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
    (birthday.month == today.month and birthday.day > today.day):
        years -= 1
 
    return years
 
def kg_from_lb(lb):
    """Convert a mass in pounds to kilograms.
    Parameter lb: a mass in US pounds.
    Return: the mass in kilograms.
    """
    return lb * 0.45359237
 
def cm_from_in(inch):
    """Convert a length in inches to centimeters.
    Parameter inch: a length in inches.
    Return: the length in centimeters.
    """
    return inch * 2.54
 
def body_mass_index(weight, height):
    """Calculate and return a person's body mass index (bmi).
    Parameters:
    weight must be in kilograms.
    height must be in centimeters.
    Return: a person's body mass index.
    """
    bmi = 10000 * weight / height**2
    return bmi
 
def basal_metabolic_rate(gender, weight, height, age):
    """Calculate and return a person's basal metabolic rate (bmr).
    Parameters:
    weight must be in kilograms.
    height must be in centimeters.
    age must be in years.
    Return: a person's basal metabolic rate in kcal per day.
    """
    if gender.upper() == "F":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr
 
main()


 
# Call the main function so that
# this program will start executing.