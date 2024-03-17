def validate_email(email):
    # Can only be one @ symbol
    if email.count("@") != 1:
        return False
    
    at_pos = email.index("@")
    # Must be text before the @
    # Must be text after the @
    if at_pos == 0 or at_pos == len(email)-1:
        return False
    
    username, domain = email.split("@")
    # michelle@dkit.ie
    # At least one . AFTER the @
    if "." not in domain:
        return False
    
    dot_pos = domain.index(".")
    # Must be text between the @ and the .
    # Must be text AFTER the .
    if dot_pos == 0 or dot_pos == len(domain)-1:
        return False
    
    return True
    

if __name__ == "__main__":
    emails = ["michelle@dkit.ie", "michelledkit.ie", "michelle@@dkit.ie", "@michelle.dkit.ie", "michelle.dkit.ie@", "michelle@dkitie", "michelle@dkitie.", "michelle@.dkit.ie", "michelle@dkit.ie."]
    for email in emails:
        if validate_email(email):
            print(f"{email}: valid email found")
        else:
            print(f"{email}: INVALID")
