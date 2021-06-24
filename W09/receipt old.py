"""This file reads the products.csv file and the 
request.csv file in order to create dictionaries. ???"""

import pandas as pd 

def main():
    read_products("products.csv")


def read_products(filename):
    """Read the contens of a CSV file into a dictionary
    and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    products = {}

    # Open the text file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:
        products_reader = pd.read_csv(csv_file)

        # Read the rows in the CSV file one row at a time.
    # The reader object returns each row as a list.
    for product in products_reader:

        # From the current row, retrieve
        # the column that contains the key.
        key_column_index = 0
        key = product[key_column_index]

        # Store the data from the current row
        # into the dictionary.
        products[key] = product

    # Return the dictionary named products.
    return products


# Call main to start this program.
if __name__ == "__main__":
    main()