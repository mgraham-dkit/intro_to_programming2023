# Create a list to store the grades
grades = []
# Ask user how many grades they want to enter
num_grades = int(input("How many grades do you want to enter?"))

# for each grade to be entered:
for i in range(num_grades):
    # Take in the grade and store it in a variable
    grade = int(input("Please enter the next grade: "))
    # Add the grade to the list
    grades.append(grade)
    
print(f"Grades entered: {grades}")