import random


def generate_password():
    # Set up the sources of the password components
    special_char = "£$%@!?#"
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = alpha_lower.upper()
    
    # Set up the quantities required for each component
    req_lower = 3
    req_upper = 1
    req_num = 2
    req_special = 2
    
    # Create the string to store the password (blank to start)
    password = ""
    
    # Loop to create and add required quantity of lowercase letters
    # to the password
    for i in range(req_lower):
        # Gererate random number between 0 and 25
        # this range corresponds to the available letters in the string
        # (i.e. their positions in the string)
        index = random.randint(0, 25)
        # Get the letter at the generated position
        rand_letter = alpha_lower[index]
        # Add the new letter to the password
        password += rand_letter
    
    # Return the final version of the password
    return password
    

# This is the line calling the function
# therefore it is the line that the function will "return" (hand) its
# result back to
password = generate_password()
# Display the password
print(f"Generated password is: {password}")

