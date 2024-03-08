users = {
    "username": "password",
    "Fred": "mischief",
    "George": "managed",
    "Ben" : "Kenobi"
}

username = input("Please enter username: ")
password = input("Please enter password: ")

logged_in = False
if username in users:
    correct_password = users[username]
    if correct_password == password:
        print("Logged in successfully")
        logged_in = True
        
if logged_in:
    print("Welcome to our super mysterious secret project code")
    
else:
    print("Sorry, you don't know the secret handshake")
    