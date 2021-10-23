# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
from string import ascii_lowercase

WORDLIST_FILENAME = "../words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    wordlist = []
    with open(WORDLIST_FILENAME) as f:
        for line in f:
            wordlist.append(line.strip())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guess = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            guess += letter
        else:
            guess += ' _ '
    return guess


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = ""
    for letter in ascii_lowercase:
        if letter not in lettersGuessed:
            available += letter
    return available


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guessesLeft = 8
    lettersGuessed = set()

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secretWord)} letters long.")

    while guessesLeft > 0 and not isWordGuessed(secretWord, lettersGuessed):
        print("------------")
        print(f"You have {guessesLeft} guesses left.")
        print(f"Available letters: {getAvailableLetters(lettersGuessed)}")
        guess = input("Please guess a letter: ")
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: ",
                  getGuessedWord(secretWord, lettersGuessed))
            continue

        lettersGuessed.add(guess)
        if guess in secretWord:
            print(f"Good guess: {getGuessedWord(secretWord, lettersGuessed)}")
        else:
            print("Oops! That letter is not in my word: ",
                  getGuessedWord(secretWord, lettersGuessed))
            guessesLeft -= 1

    print("------------")
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secretWord}")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
