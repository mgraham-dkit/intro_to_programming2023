# Ask the user to enter their age
print("Enter your age:")
# Take in the user's age and save it in a variable
age = int(input())
# Set up a variable to store the user's drink order and then this is just
# stream of consciousness writing
drink_order = None

# Check if the user's age is 21 or over
if age >= 21:
    # If it is, ask the user what they want to drink
    print("What's your order?")
    # Store their drink order in a variable
    drink_order = input()

# If the drink order exists (i.e. if the user entered something)
if(drink_order != None):
    # Display their drink order
    print("One", drink_order, "coming up!")
# Otherwise
else:
    # Print that they are getting a soda (default drink type for under 21)
    print("One soda, coming up!")