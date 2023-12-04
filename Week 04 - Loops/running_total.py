# Create a variable to hold the total of all numbers entered
total = 0

# Repeat the next section of code 5 times
for i in range(5):
    # Take in a number from the user and add it to the current total.
    # Save this value in the total variable
    total = total + int(input("Please enter #: "))

# Once the loop has finished and all the numbers have been entered, display the total
print("The total is:", total)
