# input: List of grades
grades = [1, 4, 1, 2, 3, 6, 1, 9, 19, 2, 23, 3, 6, 12, 9]
# Create highest grade variable and set it to -1
highest_grade = -1
# for each grade in list of grades
for grade in grades:
    # if the current grade is greater than the highest grade:
    if grade > highest_grade:
        # Set current grade to highest grade
        highest_grade = grade
        
# print the highest grade
print(f"The highest grade within your list is {highest_grade}")