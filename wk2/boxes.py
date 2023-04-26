import math
def num_boxes(item, space):
    return math.ceil(item / space)

num_items = int(input("Enter the number of items: "))
num_items_box = int(input("Enter the number of items per box: "))

calculate = num_boxes(num_items, num_items_box)

print(f'For {num_items} items, packing {num_items_box} items in each box, you will need {calculate} boxes.')