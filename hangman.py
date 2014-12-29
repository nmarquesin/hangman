from __future__ import print_function
import random
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()


def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def init(words):
    print('H A N G M A N')
    return ('', '', getRandomWord(words), False)


def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    # replace blanks with correctly guessed letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    # show the secret word with spaces in between each letter
    for letter in blanks:
        print(letter, end=' ')
    print()


# Returns the letter the player entered. This function makes
# sure the player entered a single letter, and not something else.
def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def checkWin(secretWord, correctLetters):
    for i in range(len(secretWord)):
        if secretWord[i] not in correctLetters:
            return False
    print('Yes! The secret word is "' + secretWord + '"! You have won!')
    return True


def checkLost(HANGMANPICS, missedLetters, correctLetters, secretWord):
    if len(missedLetters) == len(HANGMANPICS) - 1:
        displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
        print('You have run out of guesses!')
        print('After ' + str(len(missedLetters)) + ' missed guesses and ' +
              str(len(correctLetters)) + ' correct guesses, the word was "' +
              secretWord + '"')
        return True


def playAgain():
    # This function returns True if the player wants to play again,
    # otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def main():
    missedLetters, correctLetters, secretWord, gameIsDone = init(words)

    while True:
        displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

        # Let the player type in a letter.
        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess

            # Check if the player has won
            foundAllLetters = gameIsDone = checkWin(secretWord, correctLetters)
        else:
            missedLetters = missedLetters + guess

            # Check if player has guessed too many times and lost
            gameIsDone = checkLost(HANGMANPICS, missedLetters,
                                   correctLetters, secretWord)

            # Ask the player if they want to play again
            # (but only if the game is done).
        if gameIsDone:
            if playAgain():
                (missedLetters, correctLetters,
                 secretWord, gameIsDone) = init(words)
            else:
                break

if __name__ == "__main__":
    main()
