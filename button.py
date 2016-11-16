# -*- coding: utf-8 -*-

import pygame

class UIButton(object):
    
    def __init__(self, rect):
        self.rect = rect
        self.isClicked = False
        
    def getRect(self):
        return self.rect
        
    def unClickButton(self,window):
        self.isClicked = False
        self.draw(window)
    
    def onButtonClicked(self,window):
        self.isClicked = not self.isClicked
        if(self.isClicked):
            pygame.draw.rect(window,(34,190,88,100),self.rect,0)
        else:
            self.draw(window)
        return
        
    def draw(self,window):
        pygame.draw.rect(window,(34,220,100,100),self.rect,0)