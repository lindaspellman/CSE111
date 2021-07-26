# 03 Prep: Checkpoint
# File Name: fuel_usage.py
# By: Linda J. Spellman - 5/4/21

def main():
    # Get an odometer value in U.S. miles from the user.
    first_odometer_miles = int(input("Enter the first odometer reading (in miles): "))

    # Get another odometer value in U.S. miles from the user.
    second_odometer_miles = int(input("Enter the second odometer reading(in miles): "))

    # Get a fuel amount in U.S. gallons from the user.
    fuel_gallons = float(input("Enter the amount of fuel used (in gallons): "))

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(first_odometer_miles, second_odometer_miles, fuel_gallons)

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)

    # Round the miles per gallon to one digit after the decimal.
    mpg = round(mpg, 1)

    # Round the liters per 100 km to two digits after the decimal.
    lp100k = round(lp100k, 2)

    # Display the results for the user to see.
    print(f"{mpg} miles per gallon")
    print(f"{lp100k} liters per 100 kilometers")

    # OR ACCORDING TO THE SAMPLE SOLUTION
    # print(f"{mpg:.1f} miles per gallon")
    # print(f"{lp100k:.2f} liters per 100 kilometers")


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    # SAMPLE SOLUTION used absolute value here with math
    # mpg = abs(end_miles - start_miles) / amount_gallons
    mpg = (end_miles - start_miles) / amount_gallons 
    return mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lp100k = 235.215 / mpg 
    return lp100k 


# Call the main function so that
# this program will start executing.
main()