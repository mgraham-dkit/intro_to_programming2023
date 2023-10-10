# Import the random module
# Needed to generate random numbers
import random


# Generate a random number between 1 and 3 (making it easy!)
random_num = random.randint(1,3)

# Run the code in the next section 5 times (because the range is set to 5) 
for i in range(5):
    # Take in a guess from the user and store in a variable
    guess = int(input("Please enter a guess: "))
    # If the guess matches the value to be guessed (i.e. if it's correct)
    if guess == random_num:
        # Inform the user that they got it right
        print("Congratulations!!! You guessed right!")
        # Stop the loop so the user isn't given any more guesses
        # break will halt the loop and drop the flow of execution to after it ends
        break
    # Otherwise the guess was wrong, so inform the user of this
    else:
        print("Sorry, that's wrong..")
        
# Once the game is over, tell the user what the number was
# (this way even if they got it wrong, they know)
print("Game over. The number was", random_num)
        
