# Copyright 2023, Brigham Young University-Idaho. All rights reserved. (Keers)

"""
This is a demo of some of the most common methods of looping through a list.
Here I demo looping through 3 lists at the same time which should help you
with the Week 4 Team Activity.
"""

names = ['Daniel Brown',
         'Emily Davis',
         'James Wilson',
         'Olivia Lee',
         'Megan Martin', 
         'Adam Thompson']

ages = [19, 28, 45, 32, 24, 39]

genders = ['Male', 'Female', 'Male', 'Female', 'Female', 'Male']

"""
[BAD?]

Here we track the index ourselves and use a while() loop to pull out all the
date from the lists. We used the len() function in the while condition to keep
the loop going until we make it to the last index. We could have picked any
array since they are all the same length:
"""
print("\nwhile(i < len([list]))")
print(f"{'-' * 40}")
i = 0;
while(i < len(names)):
    name   = names[i]
    age    = ages[i]
    gender = genders[i] 
    print(f"Name: {name:<15} Age: {age:<5} Gender: {gender}")
    i += 1 # Don't forget to increment the iterator (index number).

"""
[GOOD]

Here we use the len() function inside the range() function to loop through
the indexes of the names array. We could have picked any array since they
are all the same length:
"""
print("\nfor i in range(len([list]))")
print(f"{'-' * 40}")
for i in range(len(names)):
    name   = names[i]
    age    = ages[i]
    gender = genders[i] 
    print(f"Name: {name:<15} Age: {age:<5} Gender: {gender}")

"""
[BETTER]

Here we use the enumerate() function to enumerate over the names array. Again we
could have picked any array since they are all the same length. This pulls out
the index number and value at the same time for us:
"""
print("\nfor i, [var] in enumerate([list]) *multiple lines*")
print(f"{'-' * 40}")
for i, name in enumerate(names):
    age    = ages[i]
    gender = genders[i] 
    print(f"Name: {name:<15} Age: {age:<5} Gender: {gender}")

"""
[BEST?]

Here we used enumerate again but did not bother pulling out the other variables
from their lists:
"""
print("\nfor i, [var] in enumerate([list]) *single line*")
print(f"{'-' * 40}")
for i, name in enumerate(names):
    print(f"Name: {name:<15} Age: {ages[i]:<5} Gender: {genders[i]}")

# Add a little more space.
print()