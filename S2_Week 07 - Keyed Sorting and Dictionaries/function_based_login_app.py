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
    
