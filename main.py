# Call for modules:
import random
from art import logo

#--------------------------------------------------------------------
# Logo printing and welcome message:
print(logo)
print("Welcome to the Number Guessing Game!")
#--------------------------------------------------------------------
# Global variables:

game_modes = ('zen', 'hard',  'easy', 'crusher')
game_mode = input("Which difficulty you want to play on? (Zen, Easy, Hard)\nDescription:\nZen --> Unlimited lives\n"
                  "Easy --> 10 lives\nHard --> 5 lives\nCRUSHER --> ONLY ONE SHOT!\n").lower()

#---------------------------------------------------------------------

# Defining the game number:
number = random.randint(1,100) # The number of the game
#---------------------------------------------------------------------

# Define the game modes:

def zen_mode():
    """This function creates the game mode that has unlimited lives"""
    is_game_over = False
    guess = int(input("Guess a number: "))
    while not is_game_over:
        if number == guess:
            print("Congratulations!🎆🎆🎉🎊\nYou guessed my number!")
            is_game_over = True
        elif number > guess:
            print("Your guess is too low! Think bigger!")
            guess = int(input("Guess again: "))
        elif number < guess:
            print("Your guess is too high!")
            guess = int(input("Guess again: "))

def easy_mode():
    """This function creates the game mode that has 10 lives"""
    is_game_over = False
    lives = 10
    guess = int(input("Guess a number: "))
    while not is_game_over:
        if number == guess:
            print("Congratulations!🎆🎆🎉🎊\nYou guessed my number!")
            is_game_over = True
        else:
            if lives > 1:
                if number > guess:
                    lives -= 1
                    print(f"You have {lives} lives left!")
                    print("Your guess is too low! Think bigger!")
                    guess = int(input("Guess again: "))
                elif number < guess:
                    lives -= 1
                    print(f"You have {lives} lives left!")
                    print("Your guess is too high!")
                    guess = int(input("Guess again: "))
            elif lives == 1:
                print("You ran out of lives! Game is over!")
                is_game_over = True



def hard_mode():
    """This function creates the game mode that has 5 lives"""
    is_game_over = False
    lives = 5
    guess = int(input("Guess a number: "))
    while not is_game_over:
        if number == guess:
            print("Congratulations!🎆🎆🎉🎊\nYou guessed my number!")
            is_game_over = True
        else:
            if lives > 1:
                if number > guess:
                    lives -= 1
                    print(f"You have {lives} lives left!")
                    print("Your guess is too low! Think bigger!")
                    guess = int(input("Guess again: "))
                elif number < guess:
                    lives -= 1
                    print(f"You have {lives} lives left!")
                    print("Your guess is too high!")
                    guess = int(input("Guess again: "))
            elif lives == 1:
                print("You ran out of lives! Game is over!")
                is_game_over = True

def crusher_mode():
    """This function creates the game mode that has 1 lives"""
    is_game_over = False
    lives = 1
    guess = int(input("Guess a number: "))
    while not is_game_over:
        if number == guess:
            print("Congratulations!🎆🎆🎉🎊\nYou guessed my number!")
            is_game_over = True
        else:
            if lives > 1:
                if number > guess:
                    lives -= 1
                    print(f"You have {lives} lives left!")
                    print("Your guess is too low! Think bigger!")
                    guess = int(input("Guess again: "))
                elif number < guess:
                    lives -= 1
                    print(f"You have {lives} lives left!")
                    print("Your guess is too high!")
                    guess = int(input("Guess again: "))
            elif lives == 1:
                print("YOU MISSED YOUR ONLY SHOT! GAME IS OVER!")
                is_game_over = True


# --------------------------------------------------------------------
# Checking if the player did choose a valid game mode:

valid_game_mode = False
while not valid_game_mode:
    if not game_mode in game_modes:
        print("Not valid difficulty! Choose another one from the list!")
        game_mode = input("Description:\nZen --> Unlimited lives\n"
                          "Easy --> 10 lives\nHard --> 5 lives\nCRUSHER --> ONLY ONE SHOT!\n").lower()
        valid_game_mode = False
    else:
        valid_game_mode = True

#--------------------------------------------------------------------
# Calling the game mode chosen by the player:
if valid_game_mode:
    #print(f"Pssstttt... My number is: {number}")
    if game_mode == "zen":
        print("Difficulty: ZEN")
        zen_mode()
    elif game_mode == "easy":
        print("Difficulty: EASY")
        easy_mode()
    elif game_mode == "hard":
        print("Difficulty: HARD")
        hard_mode()
    elif game_mode == "crusher":
        print("Difficulty: CRUSHER! 1 BAD GUESS AND YOU ARE OUT!")
        crusher_mode()
#--------------------------------------------------------------------