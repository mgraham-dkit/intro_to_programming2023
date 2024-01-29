input: 	List of floats (grades)
        Value to be counted (float)
        
Pseudocode:
Create a variable to track highest number of instances and set to 0
Create a variable to track the most frequent grade and set to None
for each value in grades list
    Create counter for value and set to 0
    for each grade in the grades list
        Check if current grade equals value being counted
            If so, add ONE to counter for value

    Display counter for this value
    
    Check if counter is higher than highest number of instances:
        Set highest number of instances equal to this counter
        Set most frequent grade to the current grade
 
Display most frequent grade found in list
Display how many times it was found