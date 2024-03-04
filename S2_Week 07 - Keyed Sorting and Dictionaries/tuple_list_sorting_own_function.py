# Import operator module so we can do flexible sorting
from operator import itemgetter

def calc_value(item_tuple):
    return item_tuple[1] * item_tuple[2]


# Read in file
# Take in a filename & store in variable
filename = input("Please enter the name of the file: ")
# Create a list to store product tuples
items = []
# Open the file
# file = open(filename, "r") is simpler version of:
with open(filename, "r") as file:
    # for each line in the file:
    for line in file:
        # Strip excess padding off line and split
        # based on the %% delimiter
        name, price_str, quantity_str = line.strip().split("%%")
        # Cast price to number
        price = float(price_str)
        # Cast quantity to number
        quantity = int(quantity_str)
        # Build tuple from name, price and quantity
        item = (name, price, quantity)
        # Add new item tuple to the list
        items.append(item)

# Display the list before we sort it, so we can see the impact
print(f"Before sorting: {items}")
# Sort the list of tuples in reverse order of quantity
# (because we are using itemgetter to get the value at position 2 in the tuple)
# Reverse parameter will switch it to descending order of data
# Doesn't need to be included if we don't want to reverse it!
items.sort(key=itemgetter(2), reverse=True)
# Display the end result
print(f"After sorting: {items}")

# Find tuple with maximum price in list
print("Tuple with max price:", max(items, key=itemgetter(1)))
# Find tuple with minimum quantity in list
print("Tuple with min quantity:", min(items, key=itemgetter(2)))

# Using own function
# Find tuple with maximum value in list
print("Tuple with max value:", max(items, key=calc_value))
