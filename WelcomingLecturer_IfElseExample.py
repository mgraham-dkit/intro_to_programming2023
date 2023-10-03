fName = input("Please enter your first name: ")
lName = input("Please enter your last name: ")
student_count = 0

if fName == "Michelle" and lName == "Graham":
    print("Welcome, lecturer")
    student_count = int(input("How many students came today?"))
else:
    print("Welcome")
    
print("Attendance count:", student_count)