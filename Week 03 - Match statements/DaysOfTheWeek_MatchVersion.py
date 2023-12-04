day = input("Please enter the day of the week: ")
day = day.lower()
match day:
    case "monday":
        print("Monday's child is fair of face")
    case "tuesday":
        print("Tuesday's child is full of grace")
    case "wednesday":
        print("Wednesday's child is full of woe")
    case "thursday":
        print("Thursday's child has far to go")
    case "friday":
        print("Friday's child is loving and giving")
    case "saturday":
        print("Saturday's child works hard for a living")
    case "sunday":
        print("and the child that is born on the Sabbath day is bonnie and blyth and good and gay")
    case _:
        print("Not a recognised English-language day")
