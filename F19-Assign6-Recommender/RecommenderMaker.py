'''
@author: Aston Yong
'''
from RecommenderEngine import recommendations

def makerecs(name, items, ratings, numUsers, top):
    '''
    This function calculates the top recommendations and returns a two-tuple consisting of two lists. 
    The first list is the top items rated by the rater called name (string).
    The second list is the top items not seen/rated by name (string)
    '''
    newRatings = recommendations(name, items, ratings, numUsers)
    
    seen = []
    notSeen = []
    for i in range(len(ratings[name])):
        if ratings[name][i] == 0:
            notSeen.append(items[i])
        else:
            seen.append(items[i])

    topSeen = []
    topNotSeen = []
    for tup in newRatings:
        if tup[0] in seen:
            topSeen.append(tup)
        elif tup[0] in notSeen:
            topNotSeen.append(tup)
    topSeen = topSeen[:top]
    topNotSeen = topNotSeen[:top]
    return (topSeen,topNotSeen)
    


if __name__ == '__main__':
    name = 'student1367'
    items = ['127 Hours', 'The Godfather', '50 First Dates', 'A Beautiful Mind', 'A Nightmare on Elm Street', 'Alice in Wonderland', 'Anchorman: The Legend of Ron Burgundy', 'Austin Powers in Goldmember', 'Avatar', 'Black Swan']

    ratings = {'student1367': [ 0, 3,-5, 0, 0, 1, 5, 1, 3, 0], 
               'student1046': [ 0, 0, 0, 3, 0, 0, 0, 0, 3, 5], 
               'student1206': [-5, 0, 1, 0, 3, 0, 5, 3, 3, 0], 
               'student1103': [-3, 3,-3, 5, 0, 0, 5, 3, 5, 5]}

    numUsers = 2
    top = 1
    print(makerecs(name, items, ratings, numUsers, top))
             



