# Author: Luke Warner <-- You must include your name in all files!

# Import statements should do before other code.
from datetime import datetime as date # <-- You can alias imports
import math

# DONT: Pull out import attributes unnecessary or incorrectly.
pi = math.pi

# DO: Pull out import attributes necessarily and correctly.
PI = math.pi # <-- Using all caps indicates a constant variable.

# DO: Use imports efficiently.
print(f'π is noy just 3.14 it actually is more like: {math.pi}')

"""
Make sure to use the correct variable casing.

True is what you should do in python, False is to be avoided in python.
"""
snake_case   = True  # aka. Underscore Case
camelCase    = False #
# kebab-case = False # Not possible in python
PascalCase   = False # aka. Title Case
Pascal_Case  = False # aka. Pascal with Underscores
UPPERCASE    = True  # Indicates a variable that should stay constant

# Private variables.
_do_not_touch = True

# Numbers in variable names are allowed but not at the start.
pi_314 = 3.14

# Be specific/intentional with your naming conventions: What is this!?
u  = 92
pu = 94
ra = 88
am = 95
po = 84
be = 4
th = 90
cu = 96
np = 93

# This makes a lot more sense! Good thing too because these could all kill you.
uranium   = 92  # U: uranium
plutonium = 94  # Pu: plutonium
radium    = 88  # Ra: radium
americium = 95  # Am: americium
polonium  = 84  # Po: polonium
beryllium = 4   # Be: beryllium
thorium   = 90  # Th: thorium
curium    = 96  # Cm: curium
neptunium = 93  # Np: neptunium

def get_max_hr(a):
    """
    Calculates the maximum heart rate using the age-based formula (220 - age).

    Parameters:
        a (int): The persons age.

    Returns:
        int: The persons maximum heart rate based on their age.
    """
    return 220 - a

def get_target_hr(max_r, r):
    """
    Calculate target heart rate zone using the Karvonen method.

    Parameters:
        max_r (int|float): The persons max heart rate.
        r (int|float): The persons resting heart rate.

    Returns:
        float: The persons target (max) heart rate for healthy exercise.
    """
    return ((max_r - r) * 0.6) + r

def calc_target_hr_zone(age, resting):
    """
    Calculate a persons target (max) heart rate for healthy exercise.

    Parameters:
        age (int): The persons age.
        resting  (int): The persons resting heart rate.

    Returns:
        dict: The users `min` and `max` heart rates for healthy exercise.
    """
    max_hr = get_max_hr(age)
    target_hr = get_target_hr(max_hr, resting)
    return {
        'min': round(target_hr * 0.7, 2),
        'max': round(target_hr * 0.85, 2)
    }

def write_to_file(filename, content, mode="a"):
    """
    Write data to a file.

    Parameters:
        filename (str): The name (including path if needed) of the file to write to.
        content (str): The content (data) to write to the file.
        mode [str]: What mode to open the file in, default is a (append).
    """
    content  = content.strip()
    content += '\n'
    with open(filename, mode) as file:
        file.write(content)

def main():
    """
    A simple demo script that highlights proper coding practices for the
    CSE 111 course.
    """

    # Get user input.
    age = int(input('Enter your age: '))
    resting_hr = int(input('Enter your resting heart rate: '))
    zone = calc_target_hr_zone(age, resting_hr)

    # Show user their target heart rate for healthy exercise.
    print('Your target heart rate zone for vigorous exercise is')
    print(f"{zone['min']} and {zone['max']} beats per minute.")

    # Write this users results to a file.
    data = f"""
Age: {age:<8} RHR: {resting_hr:<8} => MIN: {zone['min']:<8} MAX: {zone['max']}
    """
    write_to_file('hr-zone.txt', data)

main()