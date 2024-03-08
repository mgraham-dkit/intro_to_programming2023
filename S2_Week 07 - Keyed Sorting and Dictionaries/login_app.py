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

# Create flag to track if user is logged in
# Set to false as no successful login has occurred yet
logged_in = False
# If the username is a key in the dictionary
if username in users:
    # Get the corresponding password from the dictionary
    correct_password = users[username]
    # If the stored password for this user
    # matches the entered password
    if correct_password == password:
        # Display a succcess message
        print("Logged in successfully")
        # Update flag to indicate user has logged in
        logged_in = True
        
# If the user has successfully logged in
if logged_in:
    # Display a welcome message
    print("Welcome to our super mysterious secret project code")
# Otherwise
else:
    # Display a failure message
    print("Sorry, you don't know the secret handshake")
    