'''
Created on Sep 13, 2019

@author: astonyong
Name: Aston Yong
'''
import random
'''head part functions 
- 12 head part functions 
- 3 face parts
- 3 versions for each face part
- selfie band function'''

def part_hair_flat():
    """
    Returns a string that is flat hair
    """   
    s=r"012345678901234567"
    s=r" IIIIIIIIIIIIIIII " + "\n"
    s+=r" |              | "
    return s
def part_hair_spike():
    """   
    Returns a string that is spiky hair
    """   
    s=r"012345678901234567"
    s=r" /\/\/\/\/\/\/\/\ " + "\n"
    s+=r" |              | "
    return s
def part_hair_curl():
    """   
    Returns a string that is curly hair
    """   
    s=r"012345678901234567"
    s=r" OOOOOOOOOOOOOOOO " + "\n"
    s+=r" |              | "
    return s

def part_eyes_surprised():
    """   
    Returns strings that are surprised eyes
    """   
    s=r"012345678901234567"
    s=r" | /--\   /--\  | " + "\n"
    s+=r" | |O |   |O |  | "
    return s
def part_eyes_glasses():
    """   
    Returns strings that are eyes with glasses
    """   
    s=r"012345678901234567"
    s=r" | ----    ---- | " + "\n"
    s+=r" | | o |--| o | | " + "\n"
    s+=r" | ----    ---- | " 
    return s
def part_eyes_silly():
    """   
    Returns strings that are silly eyes
    """   
    s=r"012345678901234567"
    s=r" | ~~~~~  ~~~~~ | " + "\n"
    s+=r" | | ~ |  | ~ | | " + "\n"
    s+=r" | -----  ----- | " 
    return s

def part_nose_left():
    """   
    Returns strings that are the nose pointed left
    """   
    s=r"012345678901234567"
    s=r" |      /       | " + "\n"
    s+=r" |     /        | " + "\n"
    s+=r" |    |___      | " + "\n"
    s+=r" |              | "
    return s
def part_nose_right():
    """   
    Returns strings that are the nose pointed right
    """   
    s=r"012345678901234567"
    s=r" |       \      | " + "\n"
    s+=r" |        \     | " + "\n"
    s+=r" |      ___|    | "+ "\n"
    s+=r" |              | "
    return s
def part_nose_front():
    """
    Returns strings that are the nose facing frontward
    """
    s=r"012345678901234567"
    s=r" |      /\      | " + "\n"
    s+=r" |     /  \     | " + "\n"
    s+=r" |    |____|    | " + "\n"
    s+=r" |              | "
    return s

def part_mouth_open():
    """
    Returns strings that is an open mouth
    """
    s=r"012345678901234567"
    s=r" |     ____     | " + "\n"
    s+=r" |    \____/    | "
    return s
def part_mouth_smile():
    """
    Returns strings that is a smiling mouth
    """
    s=r"012345678901234567"
    s=r" |    \____/    | "
    return s

def part_chin_flat():
    """
    Returns strings that is a flat chin
    """
    s=r"012345678901234567"
    s=r" |______________| "
    return s

def selfie_band():
    """
    Returns strings that make the selfie band
    """
    s=r"012345678901234567"
    s=r" |--------------| " + "\n"
    s+=r" |aty9      aty9| " + "\n"
    s+=r" |--------------| "
    return s

"""head functions 
- 3 heads no parameter
- 3 heads with parameter
"""
def head_with_hair(hairfunc):
    """
    Print a head that looks surprised with a left
    pointing nose and hair that can change.
    """
    print(hairfunc())
    print(part_eyes_surprised())
    print(part_nose_left())
    print(part_mouth_open())
    print(part_chin_flat())
def head_with_nose(nosefunc):
    """
    Print a head that looks silly,
    with spiky hair and an input nose
    """
    print(part_hair_spike())
    print(part_eyes_silly())
    print(nosefunc())
    print(part_mouth_smile())
    print(part_chin_flat())
def head_with_eyes(eyefunc):
    """
    Print a head that is talking with 
    variable eyes.
    """
    print(part_hair_flat())
    print(eyefunc())
    print(part_nose_front())
    print(part_mouth_open())
    print(part_chin_flat())
def silly_head():
    """
    Print a head that looks funny,
    with open mouth
    """
    print(part_hair_spike())
    print(part_eyes_silly())
    print(part_nose_front())
    print(part_mouth_open())
    print(part_chin_flat())
def happy_head():
    """
    Print a head that looks happy,
    With smile and glasses
    """
    print(part_hair_curl())
    print(part_eyes_glasses())
    print(part_nose_left())
    print(part_mouth_smile())
    print(part_chin_flat())
def surprised_head():
    """
    Print a head that looks surprised,
    with open mouth.
    """
    print(part_hair_flat())
    print(part_eyes_surprised())
    print(part_nose_right())
    print(part_mouth_open())
    print(part_chin_flat())
def head_with_two(hairfunc,nosefunc):
    """
    Print a head with hair and nose parts 
    given by user, with open mouth and 
    surprised eyes
    """
    print(hairfunc)
    print(part_eyes_surprised())
    print(nosefunc)
    print(part_mouth_open())
    print(part_chin_flat())
    
'''totem functions - 3 Totems (fixed, selfie function, 
selfie totem, random function, random totem)
'''
    
def totem_fixed():
    """
    Print the same totem pole with three
    heads, one with curly hair, one with glasses,
    and one with nose pointed right.
    """
    head_with_hair(part_hair_curl)
    head_with_eyes(part_eyes_glasses)
    head_with_nose(part_nose_right)
    

def totem_selfie():
    """
    Print a totem pole with selfie band under each head.
    """
    head_with_hair(part_hair_spike)
    print(selfie_band())
    head_with_eyes(part_eyes_surprised)
    print(selfie_band())
    head_with_nose(part_nose_front)
    print(selfie_band())
    
def head_random():
    """
    Print a head with randomly chosen
    hair and nose.
    """
    nosefunc = part_nose_left()
    hairfunc= part_hair_flat()
    x = random.randint(1,4)
    if x == 1:
        nosefunc = part_nose_front()
        hairfunc = part_hair_spike()
    elif x == 2:
        hairfunc = part_hair_curl()
        nosefunc = part_nose_left()
    elif x==3:
        hairfunc = part_hair_flat()
        nosefunc = part_nose_right()
    else:
        hairfunc = part_hair_spike()
    # now call the function
    head_with_two(hairfunc,nosefunc)
    

def totem_random():
    """
    Print three random heads
    using head_random()
    """
    head_random()
    head_random()
    head_random()

if __name__ == '__main__':
    print("\nfixed totem\n")
    totem_fixed()    
      
    print("\nself totem\n")
    totem_selfie()
      
    print("\nrandom totem\n")
    totem_random()
