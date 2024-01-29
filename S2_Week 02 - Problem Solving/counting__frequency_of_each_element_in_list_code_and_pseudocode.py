# input: 	List of floats (grades)
grades = [1, 4, 1, 2, 3, 6, 1, 9, 19, 2, 23, 3, 6, 12, 9]

# for each value in the grades list
for value in grades:
    # Create counter for value and set to 0
    counter = 0
    # for each grade in the grades list
    for grade in grades:
        # Check if current grade equals value being counted
        if grade == value:
            # If so, add ONE to counter for value
            counter = counter + 1

    # Display counter for this value
    print(f"{value} appeared {counter} times in the list")
