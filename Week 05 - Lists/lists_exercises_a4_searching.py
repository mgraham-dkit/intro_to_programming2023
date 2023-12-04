# Create a hard-coded list of values
nums = [1, 4, 45, 12, 6, -4, 35, 10000, 7, 99]

# Set up a flag to track if we found 43 in our list
# We start by assuming the value is not there (hence found = False)
# and then if we DO find it, we can set our flag to True
found = False
# Loop through the numbers in our list
for i in range(len(nums)):
    # If the current number equals 43
    # (nums[i] is always the current number in the list)
    # set our flag to True as we've found a match
    # Break out of the loop because we don't need to keep looking for a match
    if nums[i] == 43:
        found = True
        break

# If a match was found, inform the user it was found
if found == True:
    print("43 was found in the list")
# Otherwise inform them it couldn't be found
else:
    print("43 could not be found in this list")