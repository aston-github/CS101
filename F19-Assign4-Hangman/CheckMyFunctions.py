'''
This module is for you to use to test your implemention of the functions in Hangman.py
 
@author: ksm
'''
import random
import Hangman
 
 
if __name__ == '__main__':
    print('Testing createDisplayString')
    lettersGuessed = ['a', 'e', 'i', 'o', 's', 'u']
    misses = 4
    hangmanWord = list('s___oo_')
    s = Hangman.createDisplayString(lettersGuessed, misses, hangmanWord)
    print(s)
    print()
 
    print('Testing updateHangmanWord')
    guessedLetter = 'a'
    secretWord = 'cat'
    hangmanWord = ['c', '_', '_']
    expected = ['c', 'a', '_']
    print('Next line should be: ' + str(expected))
    print(Hangman.updateHangmanWord(guessedLetter, secretWord, hangmanWord))
    print()
     
    print('Testing createDisplayString')
    lettersGuessed = ['a', 'e', 'i', 'o', 's', 'u']
    missesLeft = 4
    hangmanWord = ['s','_','_','_','o','o','_']
    print(Hangman.createDisplayString(lettersGuessed, missesLeft, hangmanWord))
    print()
 
    def getWord(words, length):
        chosen_words = [word for word in words if len(word) == length]
        return random.choice(chosen_words)
    length = random.randint(5,10)
    file = open('lowerwords.txt', 'r')
    words = [line.strip() for line in file.readlines()]
    secretWord = getWord(words, length)
    print(words)
    print(length)
    print(secretWord)