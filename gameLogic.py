import wordGenerator

global blanks# Number of characters that user has to guess

def gameDisplay(words, guessedCharacters ,defaultCharacters):
    global blanks
    blanks = 0
    guessedCharacters = guessedCharacters + defaultCharacters
    board = "" # Initial board to display


    # Compares the guessedCharacters list to the words to guess.
    #   If they match, board should display that character.
    #   otherwise, display the character space holder "_" instead
    for ch in str(words):
        cGuessed = False
        for gC in guessedCharacters:
            if gC in ch:
                board+=gC
                cGuessed = True
                 # If there is a character match, display the character
                                # Otherwise, display "_" instead
        if cGuessed == False:
            board+="_"
            blanks +=1

    print(board)

def get_guessedCharacters(guessedCharacters):
    guessedCharacters.sort()
    gC = ""
    for ch in guessedCharacters:
        gC += ch

    if gC == "":
        print("There are no guesses yet")
    else:
        print("Guessed: " + gC)

def get_blanks():
    return blanks
