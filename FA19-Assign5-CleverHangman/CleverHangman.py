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
    print("How many misses do you want? Hard has 8 and Easy has 12")
    misses = input("(h)ard or (e)asy> ")
    while misses != "h" and misses != "e":
        print("You must pick h or e.")
        print("How many misses do you want? Hard has 8 and Easy has 12")
        misses = input("(h)ard or (e)asy> ")
    if misses == "h":
        return 8
    if misses == "e":
        return 12

def createDisplayString(lettersGuessed, missesLeft, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''
    notGuessed = ''.join(sorted(['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']))
    for letter in lettersGuessed:
        notGuessed = notGuessed.replace(letter, " ")
    hword = " ".join(hangmanWord)
    return "letters not yet guessed: " + notGuessed + '\n' + "misses remaining = " + str(missesLeft) + '\n' + hword

def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''
    print(displayString)
    letter = input("letter> ")
    while letter in lettersGuessed:
        print("you already guessed that")
        letter = input("letter> ")
    return letter

def handleUserInputDebugMode():
    '''
    Asks user for input whether they want to play
    in debug mode or not
    '''
    print("Do you want to play in DEBUG mode?")
    choice = input("(d)ebug or (p)lay: ")
    if choice == 'd':
        return True
    else:
        return False

def handleUserInputWordLength():
    '''
    Asks user how long they want secret word to be
    '''
    length = input("How many letters in the word you'll guess: ")
    return int(length)

def createTemplate(currTemplate, letterGuess, word):
    '''
    Makes new template 
    '''
    ret = currTemplate
    if letterGuess in word:
        for idx in range(len(word)):
            if word[idx] == letterGuess:
                ret = ret[:idx] + letterGuess + ret[idx+1:]
    return ret

def getNewWordList(currTemplate, letterGuess, wordList, DEBUG):
    '''
    Returns list with elements as template with most words and its word list,
    prioritizes underscores in ties
    '''
    dic = {}
#     print(wordList)
    for word in wordList:
        wordTemplate = createTemplate(currTemplate, letterGuess, word)
        if wordTemplate not in dic:
            dic[wordTemplate] = []
        dic[wordTemplate].append(word)
        
    ref = [template for template in dic.keys() if len(dic[template]) == max([len(dic[template2]) for template2 in dic.keys()])]
#     for k,v in dic:
#         if len(v) == maxLen:
#             ref.append(k)
    ref = sorted(ref, key= lambda x:x.count('_'), reverse=True)
#     if len(ref) > 1:
#         ref = [k for k in ref if '_' in k]   
    if DEBUG == True:
        for k,v in sorted(dic.items()):
            print(k + " : " + str(len(v)))
        print("# keys = " + str(len(dic)))     
    return (ref[0], dic[ref[0]])

def processUserGuessClever(guessedLetter, hangmanWord, missesLeft):
    '''
    updates the misses left and the hangman word with the guessed letter
    '''
    if guessedLetter not in hangmanWord:
        missesLeft-=1
        elm1 = False
    else:
        elm1 = True
    return [missesLeft, elm1]

def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''
    f = open(filename)
    data = []
    for line in f:
        data.append(line.strip())
    f.close()

    wordLength = handleUserInputWordLength()
    wordList = [i for i in data if len(i) == wordLength]
#     wordLength = random.randint(5, 10)
    print("you'll get 12 misses unless you enter 'h' for 'hard to guess'")
#     secretWord = getWord(words, wordLength)
    missesStart = handleUserInputDifficulty()
    DEBUG = handleUserInputDebugMode()
    lettersGuessed = []
#     currTemplate = ["_" for i in range(wordLength)]
    currTemplate = "_"*wordLength
    count = 0
    missesLeft = missesStart
    word = random.choice(wordList)

    while missesLeft != 0:
        displayString = createDisplayString(lettersGuessed, missesLeft, currTemplate)
        if DEBUG == True:
            print("(word is " + word + ")")
            print("# possible words: " + str(len(wordList)))
#         print(lettersGuessed)
#         print(word)
#         print(currTemplate)
        letterGuess = handleUserInputLetterGuess(lettersGuessed, displayString)
        lettersGuessed.append(letterGuess)
#         currTemplate = createTemplate(currTemplate, letterGuess, word)
#         print(DEBUG)
        tup = getNewWordList(currTemplate, letterGuess, wordList, DEBUG)
        #wordList = getNewWordList(currTemplate, letterGuess, wordList, DEBUG)[1]
        currTemplate = tup[0]
        wordList = tup[1]
        
#         print(wordList)
        
        if currTemplate.count("_") == 0:
            print(displayString)
            print("you guessed the word: " + word)
            if missesStart - missesLeft == 1:
                print("you made " + str(count) + " guesses with " + str(missesStart - missesLeft) + " miss")
            else:
                print("you made " + str(count) + " guesses with " + str(missesStart - missesLeft) + " misses")
            return True
        count += 1
        (missesLeft, userGuessed) = processUserGuessClever(letterGuess, word, missesLeft)
#         print(userGuessed)
        if not userGuessed:
            print("you missed: " + letterGuess + " not in word")
        
        word = random.choice(wordList)

    print("you're hung!!")
    print("word was " + word)
    print("you made " + str(count) + " guesses with " + str(missesStart - missesLeft) + " misses")
    return False
        

if __name__ == "__main__":
    '''
    Running Hangman.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
    '''
    sessionLog = []
    play = True
    while play:
        result = runGame('lowerwords.txt')
        sessionLog.append(result)
        again = input("\nDo you want to play again? y or n> ")
        if again != 'y':
            play = False
    print("You won " + str(sessionLog.count(True)) + " game(s) and lost " + str(sessionLog.count(False)))