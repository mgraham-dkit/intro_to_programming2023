import random


keep_running = True

while keep_running == True:
    print("Please enter one of the following: ")
    print("1) Guessing game")
    print("2) Tax calculator")
    print("quit) Quit the program")
    choice = input().lower()
    
    match choice:
        case "1":
            number = random.randint(1, 10)
            attempts = 0
            max_attempts = 5
            while attempts < max_attempts:
                guess = int(input("Please guess a number between 1 and 10"))
                
                if guess == number:
                    print("You have guessed the right number!")
                    print(f"It took {attempts+1} attempts to guess correctly")
                    break
                else:
                    attempts+=1
                    if attempts == max_attempts:
                        print(f"You have no guesses left - the number was {number}")
                    else:
                        print(f"Incorrect. You have {max_attempts - attempts} attempts left")
        case "2":
            salary = float(input("Please enter your salary: "))
            tax_rate = int(input("Please enter your tax_rate"))
            
            if salary > 0 and 0 <= tax_rate <= 100:
                yearly_tax = salary * (tax_rate/100)
                net_pay = salary - yearly_tax
                print(f"Yearly tax = {yearly_tax}")
                print(f"Net salary = {net_pay}")
            else:
                print("Salary or tax_rate info invalid. Please try again later.")
        case "quit":
            keep_running = False
            print("Thanks for using our program. Program now terminating...")
        case _:
            print("Invalid menu selection. Please try again")
