def display_file(filename):
    file_handle = open(filename, "r")
    
    line = file_handle.readline().strip()
    while line:
        print(line)
        line = file_handle.readline().strip()
        
    file_handle.close()
    
    
def save_to_file(data, filename):
    file_handle = open(filename, "a")
    
    #for i in range(len(data)):
    for elem in data:
        file_handle.write(str(elem)+"\n")
        
    file_handle.close()
 
def dump_to_file(data, filename):
    file_handle = open(filename, "w")
    file_handle.writelines(data)
    file_handle.close()
 

file_path = input("Please enter the name of the file to be read: ")
display_file(file_path)

data = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
save_to_file(data, "numbers.txt")
dump_to_file(data, "numbers.txt")