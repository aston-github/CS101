'''
@author: Aston Yong
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    file = open('data/books.txt','r')
    ratings = {}
    for line in file:
        info = line.split(',')
        ratings[info[0]] = []
        for i in range(len(info)):
            if i%2 == 0 and i > 0:
                ratings[info[0]].append(int(info[i]))

    file = open('filename.txt', 'r')
    firstLine = file.readline().split(',')
    items = [firstLine[i] for i in range(len(firstLine)) if i%2 ==1]
    tup = (items, ratings)
    file.close() 
    return tup