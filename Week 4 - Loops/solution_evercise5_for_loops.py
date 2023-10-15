# Display all of the even numbers between 10 and 50 INCLUSIVE
# The program should display 5 numbers per line

# Create a counter to track how many numbers we have printed out to the line
count = 0
# Loop from 10 to 50 (remember, when you specify an end point, it will stop
# one before that! Therefore we say 51 to include 50 as well)
# Instead of increasing by 1 every time (which is the default way range() works),
# we specify to increase by TWO every time. This will only give us even numbers
for i in range(10, 51, 2):
    # Print a number to the line, then a space
    # end=' ' will specify that the number is followed by a space
    # instead of moving to the next line
    # (The standard way print() works is to end the data with a \n, or a new
    # line character. This specifies not to do that)
    print(i, end=' ')
    # Add one on to the counter tracking how many numbers we have printed
    # onto the current line
    count+=1
    # If we have printed 5 numbers, we need to start a new line!
    if count == 5:
        # Move to the next line by getting print() to send a new line to the shell
        print()
        # Reset our counter to 0 so we can count how many numbers have been
        # put onto THIS line
        # (We are on a brand new line now, and no numbers have been printed to
        # it yet. Our counter should reflect that!)
        count = 0