import random

def guessing_game(difficulty):
    match difficulty.lower():
        case "easy":
            print("*"*5+"Now playing on easy mode" + "*"*5)
            top = 10
            max_attempts = 5
        case "medium":
            print("*"*5+"Now playing on medium mode" + "*"*5)
            top = 20
            max_attempts = 4
        case "hard":
            print("*"*5+"Now playing on hard mode" + "*"*5)
            top = 100
            max_attempts = 2
        case _:
            top = 10
            max_attempts = 5
            
    number = random.randint(1, top)
    attempts = 0
    max_attempts = 5
    while attempts < max_attempts:
        guess = int(input(f"Please guess a number between 1 and {top}: "))
        
        if guess == number:
            print("You have guessed the right number!")
            print(f"It took {attempts+1} attempts to guess correctly")
            return True
        else:
            attempts+=1
            if attempts == max_attempts:
                print(f"You have no guesses left - the number was {number}.")
            else:
                print(f"Incorrect. You have {max_attempts - attempts} attempts left.")

    return False

keep_running = True
game_count = 0
win_count = 0
while keep_running:
    print("Please choose one of the following options: ")
    print("1) Guessing game")
    print("quit) Quit the program")
    choice = input()
    
    match choice.lower():
        case "1":
            game_count += 1
            print("Please select one of the following difficulty levels:")
            print("1) easy: 10 guesses at a number between 1 and 10")
            print("2) medium: 4 guesses at a number between 1 and 20")
            print("3) hard: 2 guesses at a number between 1 and 100")
            choice = input()
            match choice.lower():
                case "1":
                    level = "easy"
                case "2":
                    level = "medium"
                case "3":
                    level = "hard"
                case _:
                    print("You didn't select a valid option. Since menus are a bit tough for you, I'll default you to easy mode...")
                    level = "easy"
            result = guessing_game(level)
            print(difficulty)
            if result:
                win_count+=1
        case "quit":
            print("Aww, ok. See you next time!")
            keep_running = False
        case _:
            print("Please select one of the options offered.")
            
print(f"You won {win_count} of {game_count} attempts")