# -*- coding: utf-8 -*-
import reference
import polyObject
import light
import math
import random
import livingObject

def setUpObjects():
    """
    returns a list of basic objects
    """
    object1 = livingObject.LivingObject(0,0,100,0,50,0, 0,0)
    objects = [object1]
    s = 4
    g = (reference.HEIGHT*3)/(s*2)
    for i in range(s):
        for k in range(s):
            objects.append(polyObject.PolyObject(i*g-reference.CENTER_SCREEN_WIDTH-200,k*g-reference.CENTER_SCREEN_HEIGHT-200,0.15,4,math.pi/4,10,0,0,0,0,0))
    return objects

    
def generateObjects():
    """
    returns a list of random basic objects
    """
    pObjects = [0 for i in range(random.randint(4,20))]
    for i in range(len(pObjects)):
        pObjects[i] = getRandomObject()
    return pObjects
    
def getRandomObject():
    """
    return a single random basic object
    """
    return  polyObject.PolyObject(random.randint(20,reference.CENTER_SCREEN_WIDTH),random.randint(20,reference.CENTER_SCREEN_HEIGHT),random.randint(3,9),(math.pi*2)/random.randint(1,16),random.randint(10,40),random.randint(1,10)/1000,random.randint(1,10)/1000,random.randint(1,10)/1000,random.randint(1,10)/1000)