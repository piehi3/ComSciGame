# -*- coding: utf-8 -*-
import pygame, sys
import polyObject
import reference
import graphicsHelper

class Light(polyObject.PolyObject): 
    
    def __init__(self,xCoord,yCoord,size,xMotion, yMotion,red,green,blue,alfa,fade):
        super(Light, self).__init__(xCoord,yCoord,0,0,0,size,xMotion, yMotion, 0, 0)
        self.red = red
        self.green = green
        self.blue = blue
        self.alfa = alfa
        self.fade = fade
        self.canCollide = False

    def updateGraphics(self,window,player):
        return 
    
    def updateGraphicLighting(self,window,player):
        """
        special method for drawing alfa values 
        """
        graphicsHelper.drawLight(window,player,self.size,self.xCoord,self.yCoord,self.red,self.green,self.blue,self.alfa,self.fade)
        
            
    def getRenderBoundingBox(self,player):
        return super().getBoundingBox(player)
    
    def getBoundingBox(self,player):
         return reference.NONE_RECT