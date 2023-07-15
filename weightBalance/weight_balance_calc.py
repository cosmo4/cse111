import csv
import math


def main():
    pass

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

def calc_oil_weight(quantity):
    """
    Calculates the weight of the oil in the airplane

    Parameters:
        quantity: float - the quantity of oil in quartz

    Return: 
        Float - the weight of oil in pounds

    """
    pass

def calc_fuel_weight(quantity):
    """
    Calculates the weight of the fuel in the airplane

    Parameters:
        quantity: float - the quantity of fuel in gallons

    Return: 
        Float - the weight of fuel in pounds

    """
    pass

def calc_moment(weight, arm):
    """
    Calculates the moment

    Parameters:
        weight: float - the weight of part of the airplane in pounds
        arm: float - distance from the airplane's datum in inches

    Return: 
        Float - the moment of part of the airplane

    """
    pass

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
    



main()