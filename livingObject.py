# -*- coding: utf-8 -*-
import polyObject
import pygame
import imageReference
import math
import itemStack

def pythagoran(x,y):
    return math.sqrt(x*x+y*y)

class LivingObject(polyObject.PolyObject):
    
    def __init__(self,xCoord,yCoord,mass,rotation,size,xMotion, yMotion,ID):
         super(LivingObject, self).__init__(xCoord,yCoord,mass,0,0,size,xMotion, yMotion, 0, 0,ID)
         self.inventory = []
         for i in range(0,9*3):
             self.inventory.append(itemStack.ItemStack(None,None,0,[]))
         
    def updateLogic(self,player1):
        """
        updates the postion of the object
        """

        x,y = pygame.mouse.get_pos()
        o = (player1.getTranslatedYCoord(self.yCoord)-y)
        a = (player1.getTranslatedXCoord(self.xCoord)-x)
        h = pythagoran(a,o)
        if (h!=0):
            if(a <= 0):
                self.rotation = math.asin(o/h)
            else:
                self.rotation = (math.pi)-math.asin(o/h)
        super(LivingObject, self).updateLogic(player1)
         
    def updateGraphics(self,window,player):
        """
        updates the graphics of the object
        """
        img = imageReference.livingObject
        img = pygame.transform.scale(img, (int(1*player.zoom*self.size), int(1*player.zoom*self.size)))
        img = pygame.transform.rotate(img,(self.rotation)*(180/math.pi)-90) 
        window.blit(img,(int(player.getTranslatedXCoord(self.xCoord)-self.size/2),int(player.getTranslatedYCoord(self.yCoord)-self.size/2)))
    