import csv 

def main():
    # Call read_dictionary function and store the compound dictionary in products_dict
    products_dict = read_dictionary("products.csv", 0)
    
    # Print the products_dict
    print(products_dict)
    
    # Open the request.csv file for reading
    with open("request.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        # Loop over each row in the request.csv file
        for row in reader:
            product_number = row[0]
            quantity = int(row[1])
            
            # Find the corresponding item in products_dict using the product number
            if product_number in products_dict:
                product = products_dict[product_number]
                product_name = product[1]
                product_price = product[2]
                
                # Print the product name, requested quantity, and product price
                print(f"Product: {product_name}, Quantity: {quantity}, Price: {product_price}")
            else:
                print(f"Product number {product_number} not found in the product dictionary.")


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
    dictionary = {}

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
                values = [row_list[0], row_list[1], float(row_list[2])]
                dictionary[key] = values

        return dictionary
    
if __name__ == "__main__":
    main()
