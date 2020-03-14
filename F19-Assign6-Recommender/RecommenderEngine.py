'''
@author: Aston Yong
'''

def averages(items, ratings):
    '''
    This function calculates the average ratings for items. 
    A two-tuple is returned, where the first element is a string and the second element is a float.
    '''
    ret = []
    for i in range(len(items)):
        numerator = 0
        denominator = 0
        for lst in ratings.values():
            if lst[i] != 0:
                numerator += lst[i]
                denominator += 1
        if denominator == 0:
            avg = 0
        else:
            avg = numerator/denominator
        tup = (items[i],float(avg))
        ret.append(tup)
    ret = sorted(ret, key= lambda x:x[0], reverse=False)
    ret = sorted(ret, key= lambda x:x[1], reverse=True)
    return ret

def dotProduct(lst1,lst2):
    '''
    Calculates the dot product of the two parameter lists
    '''
    ret = 0
    for i in range(len(lst1)):
        product = lst1[i]*lst2[i]
        ret += product
    return ret

def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''
    ret = []
    lst1 = ratings[name]
    for k,v in ratings.items():
        if k != name:
            lst2 = v
            score = dotProduct(lst1, lst2)
            tup = (k,int(score))
            ret.append(tup)
    ret = sorted(ret, key= lambda x:x[0], reverse=False)
    ret = sorted(ret, key= lambda x:x[1], reverse=True)
    return ret
 
def recommendations(name, items, ratings, numUsers):
    '''
    This function calculates the weighted average ratings and makes recommendations 
    based on the parameters and weighted average. A two-tuple is returned, where 
    the first element is a string and the second element is a float.
    '''
    weights = similarities(name, ratings)[:numUsers]
    newRatings = {}
    for k,v in ratings.items():
        for i in range(len(weights)):
            if k != name and k == weights[i][0]:
                vNew = [num*weights[i][1] for num in v]
                newRatings[k] = vNew
    ret = averages(items, newRatings)
    return ret

if __name__ == '__main__':
    name = 'Jeanice'
    items = ['lions', 'tigers', 'bears']
    ratings = dict([('Nohemi', [1, -2, 1]), ('Ines', [-2, 2, 0]), ('Evelynn', [-1, -2, -1]), ('Jeanice', [1, -2, 1])])
    size = 2
    sim = similarities(name, ratings)
    print('sim =', sim) # Printing for your convenience

    ret = recommendations(name, items, ratings, size)
    print(ret)