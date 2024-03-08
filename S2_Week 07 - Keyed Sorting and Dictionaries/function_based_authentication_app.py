def login(users, username, password):
    # If the username is a key in the dictionary
    if username in users:
        # Get the corresponding password from the dictionary
        correct_password = users[username]
        # If the stored password for this user
        # matches the entered password
        if correct_password == password:
            # Return true as user has been successfully credentialled
            return True
    # Where the username is not found as a key in the dictionary
    # OR the password doesn't match the one stored for the user
    # Return that they can't be logged in
    return False

def register(users, username, password):
    # Write the code for a registration function
    # Must confirm the username is not already in the dictionary
    # Must confirm the supplied password is valid
    #		- start with checking password has 8 characters
    #		- once the rest of the register logic works,
    #		- write your validate_password function and use that instead
    # If both of these checks pass, add the new user's information
    # to the dictionary of users and return True
    # Otherwise should return False (user info will not be added to dictionary)
    pass # Remove this line when you start writing your code!

def validate_password(password):
    # Write the code to validate (confirm) a password
    # contains a required set of characters
    # Passwords must be 8 characters or longer
    # Passwords must contain at least one lowercase letter
    # Passwords must contain at least one uppercase letter
    # Passwords must contain at least one special character
    # Passwords must contain at least one number
    
    # Function should return True if the password is valid,
    # and False otherwise
    pass # Remove this line when you start writing your code! 


# Create a dictionary to act as a database for user information
# Dictionary structure: key = username, value = password
users = {
    "username": "password",
    "Fred": "mischief",
    "George": "managed",
    "Ben" : "Kenobi"
}

# Take in username
username = input("Please enter username: ")
# Take in password
password = input("Please enter password: ")
        
# If the user has successfully logged in
logged_in = login(users, username, password)
if logged_in:
    # Display a welcome message
    print("Welcome to our super mysterious secret project code")
# Otherwise
else:
    # Display a failure message
    print("Sorry, you don't know the secret handshake")
    
