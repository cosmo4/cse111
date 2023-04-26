"""


v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.

"""

import math

w = int(input('Enter the width of the tire in mm (ex 205): ')) #205
ratio = int(input('Enter the aspect ratio of the tire (ex 60): ')) #60
dia = int(input('Enter the diameter of the wheel in inches (ex 15): ')) #15

volume = (math.pi * w**2 * ratio * (w * ratio + 2540 * dia)) / 10000000000

print(f'The approximate volume is {volume:.2f} liters')