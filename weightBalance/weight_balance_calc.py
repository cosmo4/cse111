import csv

def main():
    
    print('Welcome to Idaho Flight Academy!')

    try:
        plane_data = read_aircraft_data('plane_info.csv')
    
        while True:
            plane_selection = input('Which plane will you be flying today? (please enter the tail number): ')
                
            # verify that the plane_selection exists
            chosen_plane = None
            for planes in plane_data:
                if planes['Tail number'] == plane_selection.upper():
                    chosen_plane = planes
                    break
            
            if chosen_plane:
                plane = {key: float(value) if key != list(chosen_plane.keys())[0] else value for key, value in chosen_plane.items()}
                # Plane weight
                empty_weight = plane['Empty Weight']
                # call functions for user input
                oil_quantity = get_valid_oil()
                front_seat_weight = get_valid_front_seat()
                fuel_quantity = get_valid_fuel()
                rear_seat_weight = get_valid_rear_seat()
                baggage_weight = get_valid_baggage()

                # begin calculations

                # liquid calculations
                oil_weight = calc_oil_weight(oil_quantity)
                fuel_weight = calc_fuel_weight(fuel_quantity)

                # moment calculations
                empty_moment = plane['EW Moment']
                oil_moment = calc_moment(oil_weight, plane['Oil Arm'])
                front_seat_moment = calc_moment(front_seat_weight, plane['Front Seat Arm'])
                fuel_moment = calc_moment(fuel_weight, plane['Fuel Arm'])
                rear_seat_moment = calc_moment(rear_seat_weight, plane['Rear Seat Arm'])
                baggage_moment = calc_moment(baggage_weight, plane['Baggage Arm'])

                # total values
                total_weight = calc_totals(empty_weight, oil_weight, front_seat_weight, fuel_weight, rear_seat_weight, baggage_weight)
                total_moment = calc_totals(empty_moment, oil_moment, front_seat_moment, fuel_moment, rear_seat_moment, baggage_moment)

                # Center of Gravity calculation
                center_of_gravity = calc_center_of_gravity(total_weight, total_moment)

                print('Plane Information: ')
                print(f"Tail Number: {plane['Tail number']}")
                print(f"Total Weight: {total_weight}")
                print(f"The plane's center of gravity is {center_of_gravity:.1f}")
                print(f"Please double check the limitations on the weight and balance sheet and have a safe flight!")
                break
                
            else:
                print("Oops, that isn't a plane in our hanger. Please enter the tail number of one of our planes.")

    except FileNotFoundError:
        print("ERROR! File not found.")

# Get user input functions below here

def get_valid_oil():
    try:
        oil_quantity = float(input("How many quarts of oil are in the engine? "))
        if oil_quantity >= 0:
            return oil_quantity
        else:
            print("Invalid input. Please enter a non-negative number.")
            return get_valid_oil()
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_valid_oil()

def get_valid_front_seat():
    try:
        front_passengers = float(input("What is the total weight of the front-seat passengers in pounds? "))
        if front_passengers >= 0:
            return front_passengers
        else:
            print("Invalid input. Please enter a non-negative number.")
            return get_valid_front_seat()
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_valid_front_seat()

def get_valid_fuel():
    try:
        fuel_quantity = float(input("How many total gallons of fuel are in the fuel tanks? "))
        if fuel_quantity >= 0:
            return fuel_quantity
        else:
            print("Invalid input. Please enter a non-negative number.")
            return get_valid_fuel()
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_valid_fuel()

def get_valid_rear_seat():
    try:
        rear_passengers = float(input("What is the total weight of the rear-seat passengers in pounds? "))
        if rear_passengers >= 0:
            return rear_passengers
        else:
            print("Invalid input. Please enter a non-negative number.")
            return get_valid_rear_seat()
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_valid_rear_seat()

def get_valid_baggage():
    try:
        baggage = float(input("How much total baggage will be loaded in pounds? "))
        if baggage >= 0:
            return baggage
        else:
            print("Invalid input. Please enter a non-negative number.")
            return get_valid_baggage()
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_valid_baggage()

# Function to get the csv file that will be used

def read_aircraft_data(filename):
    """
    Get the csv file. Convert it's contents to a dictionary. Return the dictionary
    """
    aircraft_data = []
    with open(filename, 'rt') as file:
        reader = csv.DictReader(file)
        for row in reader:
            aircraft_data.append(row)
    return aircraft_data

# Calculation functions below

def calc_oil_weight(quantity):
    """
    Calculates the weight of the oil in the airplane

    Parameters:
        quantity: float - the quantity of oil in quartz

    Return: 
        Float - the weight of oil in pounds

    """
    return quantity * 1.8

def calc_fuel_weight(quantity):
    """
    Calculates the weight of the fuel in the airplane

    Parameters:
        quantity: float - the quantity of fuel in gallons

    Return: 
        Float - the weight of fuel in pounds

    """
    return quantity * 6

def calc_moment(weight, arm):
    """
    Calculates the moment

    Parameters:
        weight: float - the weight of part of the airplane in pounds
        arm: float - distance from the airplane's datum in inches

    Return: 
        Float - the moment of part of the airplane

    """
    return weight * arm

def calc_totals(*values):
    """
    Calculates the total values of the airplane

    Parameters:
        all are floats of the values of the different parts of the airplane and are collected into a tuple

    Return:
        Float - the total values of the airplane
    """
    total_value = 0
    for num in values:
        total_value += num
    return total_value

def calc_center_of_gravity(total_weight, total_moment):
    """
    Calculates the center of gravity

    Parameters:
        total_weight: float - total weight of the airplane in pounds
        total_moment: float - total moment of the airplane
    Return:
        Float - the center of gravity in inches from the datum
    """
    cg = total_moment / total_weight
    return cg
    
if __name__ == "__main__":
    main()