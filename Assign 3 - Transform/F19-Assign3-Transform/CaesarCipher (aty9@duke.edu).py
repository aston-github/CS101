'''
Created on Oct 24, 2019

@author: astonyong
'''
from Transform import setShift

shift = 3
lower_alph = "abcdefghijklmnopqrstuvwxyz"
upper_alph = lower_alph.upper()
shifted_lower = lower_alph[3:] + lower_alph[:3]
shifted_upper = upper_alph[3:] + upper_alph[:3]
# shifted_upper is "DEFGHIJKLMNOPQRSTUVWXYZABC"
setShift(1):



def encrypt(word):
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


if __name__ == '__main__':
    setShift(1)
    print(shifted_lower)
    word = 'Hat 7'
    print(encrypt(word))