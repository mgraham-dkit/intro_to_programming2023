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
    
    dot_pos = domain.find(".")
    # At least one . AFTER the @ 
    if dot_pos == -1:
        return False
    
    # Make sure . isn't the start or end of the domain
    if domain[0] == "." or domain[len(domain)-1] == ".":
        return False

    after_prev_dot = dot_pos+1
    while dot_pos != -1:
        dot_pos = domain.find(".", after_prev_dot)
        # Must be text between the last . and the current .
        if dot_pos == after_prev_dot:
            return False
        after_prev_dot = dot_pos+1
        
    return True
    

if __name__ == "__main__":
    emails = [
        "michelle@dkit.ie",
        "michelledkit.ie",
        "michelle@@dkit.ie",
        "@michelle.dkit.ie",
        "michelle.dkit.ie@",
        "michelle@dkitie",
        "michelle@dkitie.",
        "michelle@.dkit.ie",
        "michelle@dkit.ie.",
        "michelle@zxc..dkit.ie",
        "michelle@abc.dkit.ie"
        ]
    
    for email in emails:
        if validate_email(email):
            print(f"{email}: valid email found")
        else:
            print(f"{email}: INVALID")
