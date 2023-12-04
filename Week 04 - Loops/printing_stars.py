# Run the inner loop 10 times
for i in range(10):
    # Run the print statement 5 times (i.e. print the * 5 times)
    for j in range(5):
        # Print out an *.
        # The end="" in this is setting what the print will end with.
        # A standard print call sets the end of the line to \n (a new line)
        # This specifies to set it to "", which means a new line is not started.
        # The effect of this is that it stops the print moving to a new line, so everything is printed on the same line
        print("*", end="")
    # Do a standard print after the inner (nested) loop finishes,
    # so that it moves to a new line
    # That way the next 5 *s will be printed on the line after this one
    print()
# Both loops are finished, a rectangle of *s has now been printed