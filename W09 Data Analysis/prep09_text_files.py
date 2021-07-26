"""2 types of files: text files and binary files
    text file: stores words and numbers as human readable text
    binary file: stores pictures, diagrams, sounds, 
      movies, and other media as numbers in a format 
      that is not directly readable by humans

Text Files
    - built-in open function
        - open(filename, mode="rt")
        - use file.close method to close file if
            not using a with block with the open func
            and nesting the for loop inside the with block
                - with open auto closes the file"""

# Example 1

def main():
    # Read the contents of a text file
    # named plants.txt into a list.
    text_list = read_list("plants.txt")

    # Print the entire list.
    print(text_list)


def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list named text_list.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)

    # Return the list that contains the lines of text.
    return text_list


# Call main to start this program.
if __name__ == "__main__":
    main()

"""CSV Files: 
    - a text file that contains tabular data
    with each row on a separate line and each cell 
    (column) separated by a comma
    - CSV module"""

# Example 2 - reads the contents of a CSV file and stores 
            # the contents in a dictionary.
            # Not always necessary

import csv


def main():
    # Indexes of some of the columns
    # in the dentists.csv file.
    COMPANY_NAME_INDEX = 0
    ADDRESS_INDEX = 1
    PHONE_NUMBER_INDEX = 2

    # Read the contents of a CSV file named dentists.csv
    # into a dictionary named dentists. Use the phone
    # numbers as the keys in the dictionary.
    dentists = read_dict("dentists.csv", PHONE_NUMBER_INDEX)

    # Print the dentists dictionary.
    print(dentists)


def read_dict(filename, key_column_index):
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
    dictionary = {}

    # Open a CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column
        # headings and not information, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row in reader:

            # From the current row, retrieve
            # the column that contains the key.
            key = row[key_column_index]

            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row

    # Return the dictionary.
    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()

"""Sometimes a program simply needs to use the values in 
the CSV file in calculations but doesn't need to store 
the contents of the CSV file. In such a situation, the 
program will still use a for loop but will not use a 
dictionary. The next code example processes each line in 
the dentists.csv file to determine which dental office 
has the most patients per employee, but it doesn't use a 
dictionary."""

# Example 3

import csv

# Indexes of some of the columns
# in the dentists.csv file.
COMPANY_NAME_INDEX = 0
NUM_EMPLOYEES_INDEX = 3
NUM_PATIENTS_INDEX = 4


def main():
    # Open a file named dentists.csv and store a reference
    # to the opened file in a variable named dentists_file.
    with open("dentists.csv", "rt") as dentists_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(dentists_file)

        # The first line of the CSV file contains column headings
        # and not information about a dental office, so this
        # statement skips the first line of the CSV file.
        next(reader)

        running_max = 0
        most_office = None

        # Read each row in the CSV file one at a time.
        # The reader object returns each row as a list.
        for row in reader:

            # For the current row, retrieve the
            # values in columns 0, 3, and 4.
            company = row[COMPANY_NAME_INDEX]
            num_employees = int(row[NUM_EMPLOYEES_INDEX])
            num_patients = int(row[NUM_PATIENTS_INDEX])

            # Compute the number of patients per
            # employee for the current dental office.
            patients_per_employee = num_patients / num_employees

            # If the current dental office has more patients per
            # employee than the running maximum, assign running_max
            # and most_office to be the current dental office.
            if patients_per_employee > running_max:
                running_max = patients_per_employee
                most_office = company

    # Print the results for the user to see.
    print(f"{most_office} has {running_max:.1f} patients per employee")


# Call main to start this program.
if __name__ == "__main__":
    main()