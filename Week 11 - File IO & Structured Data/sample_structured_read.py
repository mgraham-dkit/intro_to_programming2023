students = []
filename = input("Please enter the student filename: ")
with open(filename) as file_handle:
    for line in file_handle:
        line = line.strip()
        components = line.split("%%")
        if len(components) == 2:
            print(f"Student number: {components[0]}")
            print(f"Student name: {components[1]}")
    