# - Working with numbers:
# Take in a number from the user and save it in a variable called temp1
temp1 = input("Please enter your first number")

# Cast (turn) the value the user entered from text into a number,
# then save that actual number in a new variable of its own
num1 = int(temp1)

# We then do the same thing again to get the second number from the user
temp2 = input("Please enter your second number")
num2 = int(temp2)

# Add the two numbers together
total = num1 + num2

# Display the result - print out the information in the brackets
# When you have a few things you want to print out,
# you can include them all, just separate them with commas
print("Your total is: ", total)
