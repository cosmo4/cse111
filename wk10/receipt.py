import csv
from datetime import datetime

def main():
    store_name = 'Johnson Grocery Outlet'
    print(store_name)
    print()

    try:
        # Call read_dictionary function and store the compound dictionary in products_dict
        products_dict = read_dictionary("products.csv", 0)

        # Open the request.csv file for reading
        with open("request.csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            total_quantity = 0
            cost = 0
            subtotal = 0

            # Loop over each row in the request.csv file
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])

                try:
                    # Find the corresponding item in products_dict using the product number
                    product = products_dict[product_number]
                    product_name = product[1]
                    product_price = product[2]

                    # Print the product name, requested quantity, and product price
                    print(f"Product: {product_name}, Quantity: {quantity}, Price: {product_price}")
                    total_quantity += quantity
                    cost = quantity * float(product_price)
                    subtotal += cost
                except KeyError:
                    print(f"Product number {product_number} not found in the product dictionary.")

        print()

        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax
        print(f"Number of Items: {total_quantity}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sale Tax: ${sales_tax:.2f}")
        print(f"Total: ${total:.2f}")

        print()
        print(f"Thank you for shopping at {store_name}!")
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%A %I:%M %p}")

    except FileNotFoundError:
        print("File not found. Please check the file path and name.")
    except PermissionError:
        print("Permission denied. Please ensure you have the necessary permissions to access the file.")

def read_dictionary(filename, key_column_index):
    dictionary = {}

    try:
        with open(filename, 'rt') as file:
            reader = csv.reader(file)
            next(reader)

            for row_list in reader:
                if len(row_list) != 0:
                    key = row_list[key_column_index]
                    values = [row_list[0], row_list[1], float(row_list[2])]
                    dictionary[key] = values

        return dictionary

    except FileNotFoundError:
        print("File not found. Please check the file path and name.")
    except PermissionError:
        print("Permission denied. Please ensure you have the necessary permissions to access the file.")

if __name__ == "__main__":
    main()
