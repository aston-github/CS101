'''
@author: Aston Yong
'''

import SmallDukeEatsReader
import RecommenderEngine


def driver():
    '''
    Testing recommender assignment functions with Duke eateries
    '''
    (items,ratings) = SmallDukeEatsReader.getdata()
#     print("items = ",items)
#     print("ratings = ", ratings)

    
    avg = RecommenderEngine.averages(items,ratings)
#     print("average",avg)
    if avg == correctAvg:
        print('averages works')
    else:
        print('average fails') 
     
    for key in ratings:
        slist = RecommenderEngine.similarities(key,ratings)
#         print(key,slist)
        r3 = RecommenderEngine.recommendations(key,items,ratings,3)
#         print("top",r3)

        if key == 'Sung-Hoon' and slist == correctSim:
            print('similarities works')
        elif key == 'Sung-Hoon' and slist != correctSim:
            print('similarities fails')
        if key == 'Sarah Lee' and r3 == correctRec:
            print('recommendations works')
        elif key == 'Sarah Lee' and r3 != correctRec:
            print('recommendations fails')
    
       
        
if __name__ == '__main__':
    correctAvg = [('DivinityCafe', 4.0), ('TheCommons', 3.0), 
                  ('Tandoor', 2.4285714285714284), ('IlForno', 1.8),
                  ('FarmStead', 1.4), ('LoopPizzaGrill', 1.0), 
                  ('TheSkillet', 0.0), ('PandaExpress', -0.2), 
                  ('McDonalds', -0.3333333333333333)]
    correctSim = [('Wei', 1), ('Sly one', -1), ('Melanie', -2), ('Sarah Lee', -6), ('J J', -14), ('Harry', -24), ('Nana Grace', -29)]
    correctRec = [('Tandoor', 149.5), ('TheCommons', 128.0), 
                  ('DivinityCafe', 123.33333333333333), ('FarmStead', 69.5),
                  ('TheSkillet', 66.0), ('LoopPizzaGrill', 62.0), 
                  ('IlForno', 33.0), ('McDonalds', -69.5), 
                  ('PandaExpress', -165.0)]

    driver()