import math
def max_heart(age):
    return 220 - age


user_age = float(input("What is your age: "))

heart = max_heart(user_age)

sixty = math.floor(heart * .65)
eighty = math.floor(heart * .85)
print(f'When you exercise to strengthen your heart, you should keep your heart rate between {sixty} and 167 beats per minute.')