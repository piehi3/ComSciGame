# -*- coding: utf-8 -*-
import pygame
import reference
import button
import graphicsHelper
import math

class UIOverlay(object):
    
    def __init__(self):
        self.window = pygame.Surface((reference.WIDTH,reference.HEIGHT),pygame.SRCALPHA)
        self.buttons = []
        self.isOverlayed = False
        
    def generateBackground(self,player):
        pygame.draw.rect(self.window,(0,191,255,100),(0,reference.HEIGHT-reference.CENTER_SCREEN_HEIGHT/4,reference.WIDTH,reference.CENTER_SCREEN_HEIGHT/4),0)        

        buttonSize = ((reference.CENTER_SCREEN_HEIGHT)/5)
        buttonHSpace = (reference.CENTER_SCREEN_HEIGHT/4-buttonSize)/2
        buttonWSpace = (reference.WIDTH-(buttonSize*9))/11
        for i in range(9):
            box = pygame.Rect((buttonSize*i+buttonWSpace*(i+1),(reference.HEIGHT-reference.CENTER_SCREEN_HEIGHT/4)+buttonHSpace,buttonSize,buttonSize))
            self.buttons.append(button.UIButton(box))
            self.buttons[i].draw(self.window)
            self.drawButtonOverlay(i,(buttonSize*i+buttonWSpace*(i+1)+buttonSize/2),(reference.HEIGHT-reference.CENTER_SCREEN_HEIGHT/4)+buttonHSpace+buttonSize/2,buttonSize)
    
    
    def drawButtonOverlay(self,buttonID,x,y,size):
        graphicsHelper.drawPlayerlessPolygon(self.window,(255,255,255),3,size/2,math.pi,x,y)
    
    def updateButtons(self,x,y):
        for i in range(len(self.buttons)):
            if(self.buttons[i].getRect().collidepoint(x,y)):
                self.unClickButtons(self.window)
                self.buttons[i].onuBttonClicked(self.window)
                self.uiButtonClicked(i)

    def unClickButtons(self,window):
        for i in range(len(self.buttons)):
            self.buttons[i].unClickButton(window)
    
    def uiButtonClicked(self,buttonID):
        if (buttonID==0):
            return
    
    def toggleOverlay(self,keyPress):
        if keyPress == pygame.K_ESCAPE:
            self.isOverlayed = not self.isOverlayed
    
            
    def getWindow(self):
        return self.window.copy()