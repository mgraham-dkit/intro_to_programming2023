count = 0
filename= input("Please enter the filename to be read: ")
with open(filename, "r") as file_handle:
    for line in file_handle:
        print(line.strip())
        count+=1
        
print(f"The number of lines in the file was: {count}")

