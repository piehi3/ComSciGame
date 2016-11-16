# -*- coding: utf-8 -*-
import random
import pygame
import reference
import math
import graphicsHelper

class Background(object): 
    
    def __init__(self):
        self.window = pygame.Surface((reference.WIDTH,reference.HEIGHT),pygame.SRCALPHA)
        self.genNum = random.randint(1000000000000000000000000000000,10000000000000000000000000000000000000000000000000000000000)

    def generateBackground(self,player):
        stars = []
        digitCount = len(str(self.genNum)) - 7
        shift = 0
        for i in range(digitCount):
            size = (self.getPlaceValue(i)//2) * 4 + 1
            degree = self.getPlaceValue(i+1) * ((2*math.pi)/9)
            shell1 = (self.getPlaceValue(i+2)+1) * (reference.CENTER_SCREEN_WIDTH / 8)
            shell2 = (self.getPlaceValue(i+2)+1) * (reference.CENTER_SCREEN_HEIGHT / 8)
            x = shell1*math.cos(degree+shift) #- reference.CENTER_SCREEN_WIDTH
            y = shell2*math.sin(degree+shift) #- reference.CENTER_SCREEN_HEIGHT
            starType = self.getPlaceValue(i+4)//3
            r = 200
            g = 200
            b = 200            
            if starType == 0:
                r += self.getPlaceValue(i+3) * 6
                g -= self.getPlaceValue(i+3) * 6
                b -= self.getPlaceValue(i+3) * 6
            if starType == 1:
                b += self.getPlaceValue(i+5) * 6
                r -= self.getPlaceValue(i+5) * 6
                g -= self.getPlaceValue(i+5) * 6
            if starType == 2:
                r = 255
                g = 255
                b = 255
            if starType == 3:
                r += self.getPlaceValue(i+3)
                b += self.getPlaceValue(i+5)
                
            a = 200 + self.getPlaceValue(i+6) * 6
            shift += self.getPlaceValue(i+7) * (math.pi/36)
            
            stars.append([size,x,y,r,g,b,a])
            
        for i in range(len(stars)):
            graphicsHelper.drawLight(self.window,player,stars[i][0],stars[i][1],stars[i][2],stars[i][3],stars[i][4],stars[i][5],stars[i][6],3)            
            
        
    def getPlaceValue(self,i):
        return int(str(self.genNum)[i])   
        
    def updateBackground(self,window2):
        self.window.blit(window2)
        
    def getWindow(self):
        return self.window.copy()
        
        
    