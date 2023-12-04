# Create a list with some hard-coded values
veg = ["Spinach", "Broccoli", "Carrots", "Potatoes", "Mushrooms"]

# Standard version
# For each position in the list
# (this will generate from 0 to the length of the list)
for i in range(len(veg)):
    # str(i) will get the position of the vegetable in the list
    # as a piece of text
    # veg[i] will get the text stored in the current position
    # in the veg list
    print(str(i) + ")", veg[i])

# Enhanced version
# For each element in the veg list, take that element
# and store it in the vegetable variable
# The content of this variable (vegetable) will be swapped out after 
# every iteration and the next element in the list will be put into it
for vegetable in veg:
    print("Vegetable:", vegetable)

# Overwriting the 4th position (remember, index starts at 0)
# with "Sweet potato"
veg[3] = "Sweet potato"
# Display the updated list (this will print the WHOLE list)
print(veg)