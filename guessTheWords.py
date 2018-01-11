# Created by Scott Kim
# The main Program


import time
import gameLogic
import wordGenerator

# Intial setup phase and welcome screen
def setup():
    guessWords = wordGenerator.generateWords() # Generate Words class object guessWords
    print("Welcome to Guess The Words game!!!")
    try:
        input("Press enter to play!")
    except SyntaxError:
        pass
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("LETS GO!")
    time.sleep(1)
    return guessWords

# Actual game play
def gamePlay(guessWords):
    defaultCharacters =[" ", "-", "\'", "\"", "!", ".", ","] # Add special characters as needed to be revealed by default
    guessedCharacters = [] # User-guessed characters will append onto the list
    turn = 0 # Number of turns to win the game

    while True:
        turn += 1
        print("\n[Turn " + str(turn) + "]")
        gameLogic.gameDisplay(guessWords, guessedCharacters, defaultCharacters)
        gameLogic.get_guessedCharacters(guessedCharacters)

        # Check if there are any blanks left. If all the characters have been guessed correctly, the player wins!
        blanks = gameLogic.get_blanks()
        if blanks == 0:
            print("Congratulations! You have won the game in " + str(turn-1) + " turns!!!")
            break

        # User input
        while True:
            guess = input("Guess a character: ").upper()
            if not guess.isalnum():
                print("Enter a number or a letter only please")
            elif len(guess) != 1:
                print("Enter one character only please")
            elif guess in str(guessedCharacters):
                print("You already have guessed " + guess)
            else:
                guessedCharacters.append(guess)
                break
        time.sleep(1)

def main():

    guessWords = setup()
    gamePlay(guessWords)

main()
