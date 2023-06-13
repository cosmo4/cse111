# Open the file for reading
with open("provinces.txt", "r") as file:
    # Read the contents of the provinces file into a list
    provinces_list = file.read().splitlines()

# Print the list
print(provinces_list)

# Remove the first and last elements from the list
provinces_list.pop(0)
provinces_list.pop(-1)

# Replace all "AB" with "Alberta"
provinces_list = [province.replace("AB", "Alberta") for province in provinces_list]

# Count the number of items that are "Alberta"
count_alberta = provinces_list.count("Alberta")

# Print the count
print("Number of elements that are 'Alberta':", count_alberta)
