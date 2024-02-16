# Create somewhere to store all our names
names = []
# Repeat the input process 5 times
for i in range(5):
    # Take in name
    name = input("Please enter a name: ")
    # Add name to list
    names.append(name)
    
# Convert list to a tuple
names_tuple = tuple(names)

# For every slot in the list
for i in range(len(names_tuple)):
    # Print out the current slot number (position)
    # AND print out the data in the tuple at that positio
    print(f"{i}: {names_tuple[i]}")

# For every name in the tuple, get the name AND the position
# Enumerate gives us back the name and position in one go
for i, name in enumerate(names_tuple):
    # Print the current position and the current name
    print(f"{i}: {name}")
    
 
 
    
    
    
    
    