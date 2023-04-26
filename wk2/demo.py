# * in a parameter is an optional parameter, 
# it can hold as many as you give it
# it is call "spread arguments"
"""
def family(surname, *names):
    print(surname, names)

def family2(surname, *names):
    for name in names:
        print(f'{name} {surname}')
        
family2('Warner','Luke','Anna','Rebecca')
"""

# keyword arguments ** aka dictionary

# def person(surname, **names):
#     print(names)

# person('Warner', fname='Luke', mname='Aaron')

# this creates a dictionary!!
# how to extract from a dictionary
"""
def person(**names):
    print(f"{names['fname']} {names['mname']} {names['lname']}")

person(fname='Luke', mname='Aaron', lname='Warner')
"""

"""
from datetime import datetime as d1 # this is a type
import datetime as d2 # this is a module
# using "as" is just like SQL, it is an alias

print(type(d1))
today = d1.now()
print(today)
# this works!
"""

from datetime import datetime
timestamp = datetime.now()

# how to write to a file oldschool
"""
file = open("logs.txt", "w")
file.write(f"{timestamp}\n")
file.close()
"""

with open("logs.txt", "a") as file:
    file.write(f"{timestamp}\n")