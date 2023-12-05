student_names = []
student_ids = []
filename = input("Please enter the student filename: ")
with open(filename) as file_handle:
    for line in file_handle:
        line = line.strip()
        components = line.split("%%")
        if len(components) == 2:
            print(f"Student number: {components[0]}")
            student_names.append(components[0])
            print(f"Student name: {components[1]}")
            student_ids.append(components[1])

# Locate student with longest name
# Print out their name and their ID
# Where two students have the same length as longest,
# Print the info of the first one