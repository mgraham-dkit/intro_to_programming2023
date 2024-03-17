from screencast_module import validate_email


email = input("Please enter your email address: ")
valid = validate_email(email)
if valid:
    print(f"{email}: valid email found")
else:
    print(f"{email}: INVALID")
