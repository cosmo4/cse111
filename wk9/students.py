import csv
import re

def main():
    I_NUMBER_INDEX = 0
    STUDENT_INDEX = 1

    students_dict = read_dictionary("students.csv", I_NUMBER_INDEX)

    print(students_dict)

    valid_student_number = get_valid_id()


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create empty dictionary that can be filled from reading csv file
    student_dictionary = {}

    # open csv file and store it as variable 'file'
    with open(filename, 'rt') as file:
        
        # csv module that creates a reader object that will read from the file
        reader = csv.reader(file)

        # ignore first row
        next(reader)

        # read rows one row at a time from csv file
        for row_list in reader:
            
            # if current row is not blank add data to dictionary
            if len(row_list) != 0:

                # from current row retrieve the data from the column that contains the key
                key = row_list[key_column_index]

                student_dictionary[key] = row_list

        return student_dictionary

# Stretch 2
def get_valid_id():
    # re.match("^[0-9]{1,9}$", "I NUMBER"): 
    # re.match("^[\d]{1,9}$", "I NUMBER"): same result as above
    #re.sub("[-]", "", "I NUMBER")
    while True:
        student_id = input('What is your I-Number? ')
        # Remove any dashes from the number
        student_id = re.sub("[-]", "", student_id)
        # Ensure only numbers are left
        if not re.match("^[0-9]{1,9}$", ""):
            print("Invalid I-Number")
            continue
        # Catch if I Number is too short
        if len(student_id) < 9:
            print("Invalid I-Number: too few digits")
            continue
        # Catch if I Number is too long
        if len(student_id) > 9:
            print("Invalid I-Number: too many digits")
            continue
        # All conditions met, return valid student I Number
        return student_id
    
if __name__ == "__main__":
    main()