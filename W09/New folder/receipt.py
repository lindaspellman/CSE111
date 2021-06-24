"""This file reads the products.csv file and the 
request.csv file in order to create dictionaries. ???"""

import csv

def main():

    # dictionary = read_products(r"C:\Users\Linda\OneDrive\Desktop\Python Programming\CSE111 2021 Programming with Functions\W09\New folder\products.csv")
    dictionary = read_products("products.csv")

    # process_request(r"C:\Users\Linda\OneDrive\Desktop\Python Programming\CSE111 2021 Programming with Functions\W09\New folder\request.csv", dictionary)
    process_request("request.csv", dictionary)

def read_products(filename):

    dictionary = {}

    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)

        next(reader)

        for rows in reader:
            dictionary[rows[0]] = [rows[1], rows[2]]

    print("\nProducts")

    for key in dictionary:
        print(key + " " + str(dictionary[key]))

    # Return the dictionary.
    return dictionary

def process_request(filename, dictionary):

    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)

        next(reader)

        print("\nRequested Items")

        for rows in reader:
            key = rows[0]
            keyList = dictionary[key]
            amountOrdered = rows[1]
            productName = keyList[0]
            productPrice = keyList[1]
            print(f"{productName}: {amountOrdered} @ {productPrice}")

main()