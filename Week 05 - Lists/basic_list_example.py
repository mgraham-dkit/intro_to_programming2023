# Create a list (the [] indicates it's an empty list)
rollcall = []
for i in range(3):
    name = input("Please enter your name: ")
    # Add each new name to the list using append()
    rollcall.append(name)

# Loop through the slots in the list
# (len(rollcall) will give the length of the list, so you can count through it
for i in range(len(rollcall)):
    # Access each slot in the list using the [] notation
    # the number in the [] indicates which slot to access
    # Writing it using the i variable from your for loop
    # will let you access each slot in the list one after the other
    print("Name:", rollcall[i])