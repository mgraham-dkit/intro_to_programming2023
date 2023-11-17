def email_generator(fName, lName, college):
    email = fName[0] + "." + lName + "@" + college + ".ie"
    email = email.lower()
    print(f"Email address is {email}")
    

first = input("Please enter your first name: ")
last = input("Please enter  your last name: ")
institution = input("Please enter your institution's name: ")
email_generator(first, last, institution)