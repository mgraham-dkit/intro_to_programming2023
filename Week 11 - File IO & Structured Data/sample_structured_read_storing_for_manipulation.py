student_names = []
student_ids = []
filename = input("Please enter the student filename: ")
with open(filename) as file_handle:
    for line in file_handle:
        line = line.strip()
        components = line.split("%%")
        if len(components) == 2:

            student_ids.append(components[0])
            student_names.append(components[1])

longest_pos = 0
# Locate student with longest name
for i in range(len(student_names)):
    if len(student_names[i]) > len(student_names[longest_pos]):
        longest_pos = i
        
print(f"Longest name: {student_names[longest_pos]}")
print(f"Student ID: {student_ids[longest_pos]}")
    
# Print out their name and their ID
# Where two students have the same length as longest,
# Print the info of the first one
