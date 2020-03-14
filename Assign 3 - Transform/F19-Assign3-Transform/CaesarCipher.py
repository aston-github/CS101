'''
Created on Oct 24, 2019

@author: astonyong
'''
import os.path

shift = 3
lower_alph = "abcdefghijklmnopqrstuvwxyz"
upper_alph = lower_alph.upper()
shifted_lower = lower_alph[3:] + lower_alph[:3]
shifted_upper = upper_alph[3:] + upper_alph[:3]
# # shifted_upper is "DEFGHIJKLMNOPQRSTUVWXYZABC"

def setShift(number):
    '''
    Sets the global variables to shift and shifted alphabets according to input number
    '''
    global shift, shifted_lower, shifted_upper
    shift = number
    lower_alph = "abcdefghijklmnopqrstuvwxyz"
    upper_alph = lower_alph.upper()
    shifted_lower = lower_alph[shift:] + lower_alph[:shift]
    shifted_upper = upper_alph[shift:] + upper_alph[:shift]


def encrypt(word):
    '''
    Changes each letter into new shifted letter according to setShift
    '''
    shifted = []
    for ch in word:
        if ch in lower_alph:
            idx = lower_alph.index(ch)
            chNew = shifted_lower[idx]
            shifted.append(chNew)
        elif ch in upper_alph:
            idx = upper_alph.index(ch)
            chNew = shifted_upper[idx]
            shifted.append(chNew)
        else:
            shifted.append(ch)
    return ''.join(shifted)
 
def findShift(word):
    '''
    Finds the shift applied to make input string
    '''
    file = os.path.join("data","lowerwords.txt")
    f = open(file)
    wordsClean = [w.strip() for w in f.read().split()]
    shift = 0
    max_words = 0
    for i in range(26):
        setShift(i)
        ref_lst = encrypt(word).split()
        shift_words = 0
        for elm in ref_lst:
            if elm in wordsClean:
                shift_words +=1
        if shift_words>max_words:
            max_words = shift_words
            shift = i
    return 26-shift
                



if __name__ == '__main__':
    setShift(1)
    print(shifted_lower)
    
    word = 'Hat 7'
    print(encrypt(word))
    print(findShift("Zkdw grhv wkh ira vdb?"))