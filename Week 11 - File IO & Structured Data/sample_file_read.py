count = 0
filename= input("Please enter the filename to be read: ")
file_handle = open(filename, "r")
for line in file_handle:
    print(line.strip())
    count+=1
        
file_handle.close()
print(f"The number of lines in the file was: {count}")
    