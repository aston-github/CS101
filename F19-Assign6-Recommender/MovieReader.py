'''
@author: Aston Yong
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    file = open('data/movies.txt','r')
    items = []
    ratings = {}
    for line in file:
        info = line.split(',')
        items.append(info[1])
#         items = list(set(items))
#         items = sorted(items, key=None, reverse=False)
        if info[0] not in ratings:
            ratings[info[0]] = []
#         for k,v in ratings.items():
#             if k == info[0]:
#                 ratings[info[0]].insert(items.index(info[1]),int(info[2]))
#             else:
#                 
    items = list(set(items))
    items = sorted(items, key=None, reverse=False)
    for k in ratings:
        ratings[k] = [0 for i in range(len(items))]
    file = open('data/movies.txt','r')
    for line in file:
        info = line.split(',')
        for k,v in ratings.items():
            if k == info[0]:
                ratings[k][items.index(info[1])] = int(info[2])

    tup = (items, ratings)
    file.close() 
    return tup