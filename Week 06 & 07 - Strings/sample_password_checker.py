valid = False
while not valid:
    name = input("Please enter your password: ")
    if len(name) >=  8:
        upper = False
        lower = False
        digit = False
        special = False

        for letter in name:
            if letter.isupper():
                upper = True
            elif letter.islower():
                lower = True
            elif letter.isdigit():
                digit = True
            elif letter in "?!&@~":
                special = True
                
        if upper == True and lower == True and digit == True and special == True:
            print("Password accepted")
            valid = True
        else:
            print("Password does not meet minimum requirements")
            if not upper:
                print("You did not have an uppercase letter")
            if not lower:
                print("You did not have a lowercase letter")
            if not digit:
                print("You did not have a digit")
            if not special:
                print("You did not have a special character! (Must be one of '!?&@~')")       
    else:
        print("Password was too short!")
