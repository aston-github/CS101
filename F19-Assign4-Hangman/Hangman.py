'''
Description:
        You must create a Hangman game that allows the user to play and guess a secret word.  
        See the assignment description for details.
    
@author: Aston Yong    aty9
'''
import random




def handleUserInputDifficulty():
    '''
    This function asks the user if they would like to play the game in (h)ard or (e)asy mode, then returns the 
    corresponding number of misses allowed for the game. 
    '''
    
    #Your Code Here
    print('How many misses do you want? Hard has 8 and Easy has 12.') 
    mode = input('(h)ard or (e)asy> ')
    if mode == 'e':
        return 12
    elif mode == 'h':
        return 8




def getWord(words, length):
    '''
    Selects the secret word that the user must guess. 
    This is done by randomly selecting a word from words that is of length length.
    '''
    
    #Your Code Here
#     secret = random.choice(words)
#     while len(secret) != length:
#         secret = random.choice(words)
#     return secret
    chosen_words = [word for word in words if len(word) == length]
    return random.choice(chosen_words)




def createDisplayString(lettersGuessed, missesLeft, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''
    
    #Your Code Here
    guessStr = ''
    for letter in sorted(lettersGuessed):
        guessStr = guessStr + letter + ' '
    line1 = "letters you've guessed: " + guessStr + "\n"
    line2 = 'misses remaining = ' + str(missesLeft) + "\n"
    
    wordStr = ''
    for elm in hangmanWord:
        wordStr = wordStr + elm + ' '
    line3 = wordStr
    ret = line1 + line2 + line3
    return ret




def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''
    
    #Your Code Here
    print(displayString)
    guess = input('letter> ')
    while guess in lettersGuessed:
        print('you already guessed that')
        guess = input('letter> ')
    lettersGuessed.append(guess)
    return guess




def updateHangmanWord(guessedLetter, secretWord, hangmanWord):
    '''
    Updates hangmanWord according to whether guessedLetter is in secretWord and where in secretWord guessedLetter is in.
    '''
    
    #Your Code Here
    if guessedLetter in secretWord:
        for idx in range(len(secretWord)):
            if guessedLetter == secretWord[idx]:
                idxletter = idx
                hangmanWord[idxletter] = guessedLetter
        return hangmanWord
    else:
        return hangmanWord 




def processUserGuess(guessedLetter, secretWord, hangmanWord, missesLeft):
    '''
    Uses the information in the parameters to update the user's progress in the hangman game.
    '''
    
    #Your Code Here
    ret = []
    elm0 = updateHangmanWord(guessedLetter, secretWord, hangmanWord) 
    if guessedLetter not in secretWord:
        missesLeft -= 1
    elm1 = missesLeft
    elm2 = guessedLetter in secretWord
    ret.append(elm0)
    ret.append(elm1)
    ret.append(elm2)
    return ret



def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''
    
    #Your Code Here
    length = random.randint(5,10)
    file = open('lowerwords.txt', 'r')
    words = [line.strip() for line in file.readlines()]
    secretWord = getWord(words, length)
    missesLeft = handleUserInputDifficulty()
    hangmanWord = ['_' for letter in secretWord]
    lettersGuessed = []
    numMiss = 0
    numGuess = 0
    while missesLeft >0:
        displayString = createDisplayString(lettersGuessed, missesLeft, hangmanWord)
        guessedLetter = handleUserInputLetterGuess(lettersGuessed, displayString)
        print(guessedLetter)
        numGuess +=1
        missesLeft -=1
        if guessedLetter not in secretWord:
            print("you missed: " + guessedLetter+ " not in word")
            numMiss +=1
        processUserGuess(guessedLetter, secretWord, hangmanWord, missesLeft)
        if "_" not in hangmanWord:
            print("you guessed the word: " + secretWord)
            print("you made " + str(numGuess) + " guesses with "+ str(numMiss) + " misses")
            return True

    print("you're hung!!")
    print("you made " + str(numGuess) + " guesses with "+ str(numMiss) + " misses")
    print("word is " + secretWord)
    return False
        
        



if __name__ == "__main__":
    '''
    Running Hangman.py should start theh game, which is done by calling runGame, therefore, we have provided you this code below.
    '''
    win = 0
    loss = 0
    play = 'y'
    while play == 'y':
        if runGame('lowerwords.txt') == True:
            win += 1
        else:
            loss += 1
        play = input('Want to play another game? (y)es or (n)o > ')
    print('Wins: ' + str(win) + ', Losses: ' + str(loss))
    