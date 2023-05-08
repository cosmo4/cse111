# Author: Luke Warner

import math

def main(radius, height, name):
    volume = calc_volume(radius, height)
    area = calc_surface_area(radius, height)
    storage_efficiency = volume / area
    print(f"{name} {storage_efficiency:.2f}")

def calc_volume(r, h):
    """
    Calculates the volume of a can.

    Parameters:
        r (float): The radius of the can in cm
        h (int|float): The height of the can in cm.

    Returns:
        float: The volume of a can.
    """
    return math.pi * r ** 2 * h

def calc_surface_area(r, h):
    """
    Calculates the surface area of a can.

    Parameters:
        r (float): The radius of the can in cm
        h (int|float): The height of the can in cm.

    Returns:
        float: The surface area of a can.
    """
    return 2 * math.pi * r * (r + h)

cans = [
    {'radius': 6.83, 'height': 10.16, 'name': '#1 Picnic'},
    {'radius': 7.78, 'height': 11.91, 'name': '#1 Tall'},
    {'radius': 8.73, 'height': 11.59, 'name': '#2'},
    {'radius': 10.32, 'height': 11.91, 'name': '#2.5'},
    {'radius': 10.79, 'height': 17.78, 'name': '#3 Cylinder'},
    {'radius': 13.02, 'height': 14.29, 'name': '#5'},
    {'radius': 5.40, 'height': 8.89, 'name': '#6Z'},
    {'radius': 6.83, 'height': 12.38, 'name': '#8Z short'},
    {'radius': 15.72, 'height': 17.78, 'name': '#10'},
    {'radius': 6.83, 'height': 12.38, 'name': '#211'},
    {'radius': 7.62, 'height': 11.27, 'name': '#300'},
    {'radius': 8.10, 'height': 11.11, 'name': '#303'}
]


for can in cans:
    main(can['radius'], can['height'], can['name'])
