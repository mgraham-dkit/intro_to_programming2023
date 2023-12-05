# Create an empty list
text_list = []

# Take in name of file to read
filename= input("Please enter the filename to be read: ")
# Open link to file
file_handle = open(filename, "r")
# Loop through content of file
for line in file_handle:
    # Add current line from file to end of list
    text_list.append(line.strip())
        
file_handle.close()
print(f"The number of lines in the file was: {len(text_list)}")
print(text_list)