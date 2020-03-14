'''
Created on Oct 22, 2019

@author: astonyong
'''

def isVowel(ch):
    """
    Return True if ch is a vowel and False otherwise
    """
    return "aeiouAEIOU".count(ch) > 0

def isVowelY(ch):
    """
    Return True if ch is a vowel and False otherwise
    """
    return "aeiouyAEIOUY".count(ch) > 0

def isAllVowels(word):
    '''
    Return True if all characters in word are variables and False otherwise
    '''
    return "aeiouAEIOU".count(word) == len(word)

def isNoVowels(word):
    '''
    Return True if all characters are consonants and False otherwise
    '''
    for ch in word:
        if isVowelY(ch):
            return False
    return True

def firstVowelIndex(word):
    '''
    Returns the index of the first vowel in a word
    '''
    index =0
    for ch in word:
        if ch in ['a','e','i','o','u','A','E','I','O','U']:
            return index
        else:
            index+=1
    return index

def yFirstVowelIndex(word):
    '''
    Returns the index of the first vowel in a word
    '''
    index =0
    for ch in word:
        if ch in ['a','e','i','o','u','y','A','E','I','O','U','Y']:
            return index
        else:
            index+=1
    return index
            

def encrypt(word):
    '''
    Modifies words following the Pig Latin rules and 
    returns new string with modifications
    '''
    pgla=[]
    reflst=word.split()
    for word in reflst:
        if isVowel(word[0]) or isAllVowels(word):
            mod = word + '-way'
            pgla.append(mod)
        elif isNoVowels(word):
            mod = word + '-way'
            pgla.append(mod)
        elif word[0:2] == 'qu' or word[0:2] == 'Qu' or word[0:2] == 'qU' or word[0:2] == 'QU':
            num = firstVowelIndex(word[2:])+2
            mod = word[num:] + '-' + word[0:num] + 'ay'
            pgla.append(mod)
        else:
            num = yFirstVowelIndex(word)
            if num ==0:
                mod = word[1:] + '-' + word[0] + 'ay'
            else:
                mod = word[num:] + '-' + word[:num] + 'ay'
            pgla.append(mod)
    return ''.join(pgla)

def decrypt(word):
    '''
    Returns string with PigLatin reversed into a guess of the original string
    '''
    orig = []
    reflst = word.split()
    for word in reflst:
        ref = word[:-2]
        lstParts = ref.split('-')
        orig.append(lstParts[1]+lstParts[0])
#         lstParts=word.split('-')
#         if lstParts[1][0]=='w':
#             orig.append(lstParts[0])
#         elif lstParts[1][0:2] =='qu' or lstParts[1][0:2] =='qU' or lstParts[1][0:2] =='Qu' or lstParts[1][0:2] =='QU':
#             orig.append(lstParts[1][0:2]+lstParts[0])
#         else:
#             num = yFirstVowelIndex(lstParts[1])
#             orig.append(lstParts[1][:num]+lstParts[0])
    return ''.join(orig)
    
if __name__ == '__main__':
    print(encrypt('rhythm'))
    print(isNoVowels('computer'))
    print(decrypt('ENGTH-STRay'))