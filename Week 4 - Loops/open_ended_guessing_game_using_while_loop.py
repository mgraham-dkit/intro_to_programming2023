# Import the random module so we can use the functions from there
import random


# Generate a random whole number (because we're asking for a random INT)
# between 1 and 20 and store it in a variable called random_num
random_num = random.randint(1, 20)
# Take in a guess from the user, cast it to an int and store it
# in a variable called guess
guess = int(input("Please enter your guess for the random number between 1 and 20"))
# While the guess the user entered does not match the generated random number,
# repeat the next section of code
# (This will keep the loop repeating until the value in the guess variable
# equals the value in the random_num variable)
while guess != random_num:
    # Print a message to the user telling them they're wrong
    print("Incorrect, sorry!. Try again...")
    # Ask the user for a new guess, cast it to an int and save it in the guess variable
    guess = int(input("Please enter your guess for the random number between 1 and 20"))

# Print a message congratulating the user on guessing correctly
# We know they must have guessed correctly because the loop will not stop until they do
print("Congratulations, you got it right!")