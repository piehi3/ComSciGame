import pygame
import random
import reference
import graphicsHelper
import math

def getMomentum(mass1,mass2,v1,v2):
    f = mass1*v1 + mass2*v2
        
    g = mass1*v1*v1 + mass2*v2*v2
        
    a = (mass1*mass1)/mass2 + mass1
    b = -((2*f*mass1)/mass2)
    c = (f*f)/mass2 - g
        
    h = quad(a,b,c)
    if(h[2]):
        if(h[0]==v1):
            return h[1]
        return h[0]
    return h[0]

def quad(a,b,c):
    dis = b*b - (4*a*c)
    if(dis>=0):
        a1 = (-b + math.sqrt(dis))/(2*a)
        a2 = (-b - math.sqrt(dis))/(2*a)
        return [a1,a2,True]
    return[None,None,False]

def FindCollitions(objects,pObject):
    objectPos = []
    for i in range(len(objects)):
        if(objects[i]!=pObject):
            if(isInFirstRange(pObject.xCoord,pObject.yCoord,objects[i].xCoord,objects[i].yCoord,objects[i].size+pObject.size)):
                if(isInSecondRange(pObject.xCoord,pObject.yCoord,objects[i].xCoord,objects[i].yCoord,objects[i].size+pObject.size)):
                    objectPos.append(i)
    return objectPos
        
def isInFirstRange(x1,y1,x2,y2,dis):
    return dis > (abs(x1-x2) + abs(y1-y2))

def isInSecondRange(x1,y1,x2,y2,dis):
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

class PolyObject(object):    
    
    def __init__(self,xCoord,yCoord,mass,numSides,rotation,size,xMotion, yMotion, rotaionRate, zoomRate,ID):
            self.xCoord = xCoord
            self.yCoord = yCoord
            self.numSides = numSides
            self.rotation = rotation
            self.size = size  
            self.mass = mass
            self.newXMotion = None
            self.newYMotion = None
            self.pCollide = None    
            self.counter = 10
            
            self.red = 50
            self.green = 128
            self.blue = 128    
            self.ID=ID
            
            self.xMotion = xMotion
            self.yMotion = yMotion
            self.rotatioRate = rotaionRate
            self.zoomRate = zoomRate
            
            self.canCollide = True
            self.canMove = True
    
    def disableMotion(self):
        """
        disables all motion of the object
        """
        self.canMove = False
    
    def enableMotion(self):
        """
        enables motion of the object
        """
        self.canMove = True    
    
    def checkCollided(self,player1,objects):
        if self.canCollide:
            
            collitionList =  FindCollitions(objects,self)  
            
            if len(collitionList) > 0: 
                for i in range(len(collitionList)):
                    self.onCollide(player1,objects[collitionList[i]])
    
    def updateLogic(self,player1):
        """
        updates the postion of the object
        """
        if(self.newXMotion != None):
            self.xMotion = self.newXMotion
            self.newXMotion = None
            player1.updatePlayer()
        if(self.newYMotion != None):
            self.yMotion = self.newYMotion
            self.newYMotion = None
            player1.updatePlayer()
        
        self.updatePosition(player1,1)
        self.rotation += self.rotatioRate
        self.size += self.zoomRate
        if (self.pCollide!=None):
            self.countDown()
       
    def countDown(self):
        if(self.counter>0):        
            self.counter-=1
        else:
            self.pCollide = None
        
    def onCollide(self,player,cObject):
        self.pCollide = cObject
        self.counter = 10
        self.newXMotion = getMomentum(self.mass,cObject.mass,self.xMotion,cObject.xMotion)
        self.newYMotion = getMomentum(self.mass,cObject.mass,self.yMotion,cObject.yMotion)

    def updatePosition(self,player1,i):
        if(self.canMove):
            self.xCoord += i*(self.xMotion - player1.xMotion)
            self.yCoord += i*(self.yMotion - player1.yMotion)
    
    def updateGraphics(self,window,player):
        """
        updates the graphics of the object
        """
        #self.colorChange()
        if((self.xCoord-self.size<reference.WIDTH) or (self.xCoord+self.size>0)):
            if((self.yCoord-self.size<reference.HEIGHT) or (self.yCoord+self.size>0)):
                graphicsHelper.drawRegualrPolygon(player,window,(self.red,self.green,self.blue),self.numSides,self.size+player.zoom,self.rotation,self.xCoord,self.yCoord)    
    
    def getRenderBoundingBox(self,player):
        """
        returns a rect render box of the polygon
        """
        buffer = 1.2
        distance = int((self.size*buffer)*player.zoom)
        x = player.getTranslatedXCoord(self.xCoord)
        if x < (reference.WIDTH+distance) and x > (-distance):
            y = player.getTranslatedYCoord(self.yCoord)
            if y < (reference.HEIGHT+distance) and y > (-distance):
                return pygame.Rect(x-distance, y-distance, distance*2, distance*2)
        return reference.NONE_RECT
    
    def getBoundingBox(self,player):
        return self.size
    
    def accelerateUp(self):
        """
        removes y acceleration
        """
        self.yMotion -= 0.001#02
        
    def accelerateDown(self):
        """
        adds y acceleration
        """
        self.yMotion += 0.001#02
    
    def accelerateLeft(self):
        """
        removes x acceleration
        """
        self.xMotion -= 0.001#02
    
    def accelerateRight(self):
        """
        adds x acceleration
        """
        self.xMotion += 0.001#02
        
    def accelerateRotation(self):
        """
        adds clockwise rotation
        """
        self.rotatioRate += 0.00002
        
    def deccelerateRotation(self):
        """
        adds counterclockwise rotation
        """
        self.rotatioRate -= 0.00002
        
    def zoomIn(self):
        """
        increases the radius of the polygon
        """
        self.size += 0.1
        
    def zoomOut(self):
        """
        decreases the radius of the polygon
        """
        self.size -= 0.1
        
    def colorChange(self):
        """
        sets random color
        """
        self.red = self.getRandomColorInBounds(self.red)
        self.green = self.getRandomColorInBounds(self.green)
        self.blue = self.getRandomColorInBounds(self.blue)
        
    def getRandomColorInBounds(self,color):
        """
        randomly ajusts the given color (r,g or b) and returns it
        """
        rand = random.randint(-2,2)        
        return (color+rand if color+rand <= 255 else 255) if color+rand>=0 else 0