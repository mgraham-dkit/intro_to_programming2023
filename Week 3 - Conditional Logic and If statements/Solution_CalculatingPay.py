'''
A company pays regular time for the first 40 hours
worked in a week by each employee.
They then pay time and a half for the next 10 hours
worked over 40 hours, and double time for any hours
worked beyond that.

Ask the user to enter the number of hours an employee
worked in a particular week and the worker’s
hourly rate of pay.

The program should calculate and output the employee’s
gross pay.
'''
# Ask the user to enter how many hours were worked
# and store the answer as an INT in a varible called hours_worked
# Remember that everything taken in using input() comes in as text
# The int() is what turns the user's data from text into a number
hours_worked = int(input("Please enter the number of hours worked: "))
# Ask the user to enter the hourly rate of pay
# and then store it as an INT in a variable called rate
rate = int(input("Please enter the hourly rate of pay: "))

# Create a variable called takehome that will hold
# the overall calculated wages
# (we will fill it with an actual value using our if statement sequence)
takehome = 0
# Define what to do if they have worked 40 hours or fewer
if hours_worked <= 40:
    # Calculate the regular pay by multiplying
    # the number of hours worked by how much they are paid per hour
    # Store this as our takehome variable as that's the only income they are getting
    takehome = hours_worked * rate
# Now define what to do if the number of hours worked is between 40 and 50
# elif links this condition to the first one.
# If the first if statement branch runs, then this won't be run
elif hours_worked > 40 and hours_worked <= 50:
    # We know they have worked for more than 40 hours
    # (if it was 40 or fewer, the first if statement would have run)
    # so we can work out the basic pay as 40 * hourly rate
    regular_pay = 40 * rate
    # We can then work out the amount of overtime worked by subtracting
    # 40 from the hours worked (the 40 hours were used for the regular pay)
    overtime = (hours_worked-40) * (1.5*rate)
    # Set our takehome value to be the regular pay plus the overtime
    takehome = regular_pay + overtime
# Define what should happen if the user worked more than 50 hours
# Since we have covered all numbers up to 50, we can use an else to
# deal with this. else will run if the other if conditions are not true,
# it's a default. If a number is not less than or equal to 50,
# it must be more than 50, so else will cover that
else:
    # Calculate the default pay and store it in the regular_pay variable
    regular_pay = 40 * rate
    # Calculate the overtime and store it in the overtime variable
    overtime = 10 * (1.5*rate)
    # Calculate the double time pay and store it in the double variable
    double = (hours_worked-50) * (2*rate)
    # Add the regular pay, overtime and double time pay together
    # and store it in the takehome variable
    takehome = regular_pay + overtime + double

# Display the takehome value calculated in the if statement
# Only one of the above branches will have run,
# so the takehome variable will only have been filled once
print("Take home pay:", takehome)