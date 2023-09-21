# All of the lines in this file that start with a # are NOT code
# and will not run. They are used to explain the actual code and how it works

# - Working with numbers:
# Take in a number from the user and save it in a variable called temp1
# Remember, input() always "takes in" (gets from the user) information as TEXT
# So even if the user types in a number, it's like the number is in quotes
temp1 = input("Please enter your first number")

# If the info entered was a number, we can convert it from the text version
# into an actual number (e.g. turn "3" into 3). This is done through CASTING

# Casting for whole numbers (no decimal point) is done using int()
# int("3") would produce the value 3
# We then need to save that result (the actual number) in a variable of its own

# So here we're casting the value the user entered from text into a number,
# then saving that actual number in a new variable of its own
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
