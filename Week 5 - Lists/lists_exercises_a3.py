# Create a list with some hard-coded values
# This will be used as a look-up table to convert
# from month position to month name
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Prompt the user to enter the number of a month, convert it to a number
# and store it in the choice variable
choice = int(input("Please enter the number of the month you want to see: "))
# Display the number of the month they chose, followed by the corresponding month name
# This is an example of an fString - a formatted piece of text
# Text within {} will be treated as a variable name, and the value of that
# variable will be inserted into the text
# Here choice and months[choice-1] are variables, and their values will be
# slotted in before printing the overall information

# Note: We use months[choice-1] because our months index starts at 0
# (i.e. the first position is 0)
# Since users start their count at 1, we need to offset this
# (For example, 1-1 gives 0, which would point the user to January)
print(f"Month #{choice}: {months[choice-1]}")

# This is a standard print - no fString is used.
# You need to cast the number before printing it
#print("Month #", str(choice),":", months[choice-1])