# All of the lines in this file that start with a # are NOT code
# and will not run. They are used to explain the actual code and how it works

# Step being carried out: Asking a user to enter their first name and saving it

# How it works:
# input() will print out the text in the quotes (text must be in quotes!)
# then it will wait until the user enters text

# Once the user enters text (and presses enter to submit it!)
# the program will take that text and put it into the thing (variable)
# on the left of the equals (in this case, fName) - this is storing in a variable
fName = input("Please enter your first name: ")

# Take in last name from user
# This does the same thing, but it puts what the user typed in
# in a separate variable called lName
lName = input("Please enter your last name: ")

# Create full name for user - this sticks (concatenates) the text stored
# in the variables together and stores that combined text in a new variable
full_name = fName +" " + lName

# Display full name to user
# print takes whatever text is within the brackets
# and prints it out to the screen
print("Your full name is: " + full_name)
