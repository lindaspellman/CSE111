"""This file reads the products.csv file and the 
request.csv file in order to create dictionaries. ???"""

import csv

def main():
    read_products("products.csv")

def read_products(filename):
    products = {}

    # Open the text file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:
        products_reader = csv.reader(csv_file, delimiter=" ", quotechar="|")
        
        # Read the contents of the text
        # file one line at a time.
        for line in products_reader:
            print(line)
            # Identify variables from each line
            product_num = products_reader[0]
            product_name = products_reader[1]
            product_price = products_reader[2]

    # Return the list that contains the lines of text.
    ### print(products)

main()