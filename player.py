# -*- coding: utf-8 -*-
import pygame, sys
import reference



class Player(object):
    
    def __init__(self,pObject):
        self.pObject = pObject

        self.pObject.disableMotion()        
        
        self.xMotion = 0
        self.yMotion = 0

        self.xView = 0
        self.yView = 0        
        
        self.zoom = 1
        
        self.keyUp = pygame.K_w
        self.keyDown = pygame.K_s
        self.keyLeft = pygame.K_a
        self.KeyRight = pygame.K_d
        self.keyRotateRight = pygame.K_q
        self.keyRotateLeft = pygame.K_e
        self.keyZoomIn = pygame.K_x
        self.keyZoomOut =  pygame.K_c
        self.keySwitchObject = pygame.K_TAB
        
    def bindKeys(self,keyUp,keyDown,keyLeft,KeyRight,keyRotateRight,keyRotateLeft,keyZoomIn,keyZoomOut,keySwitchObject):
        """
        binds keys in parameters to player
        """
        self.keyUp = keyUp
        self.keyDown = keyDown
        self.keyLeft = keyLeft
        self.KeyRight = KeyRight
        self.keyRotateRight = keyRotateRight
        self.keyRotateLeft = keyRotateLeft
        self.keyZoomIn = keyZoomIn
        self.keyZoomOut =  keyZoomOut
        self.keySwitchObject = keySwitchObject

    def playerInput(self,keyPress):
        """
        process input from the user
        """
        if keyPress[self.keyUp]:
            self.pObject.accelerateUp()
        if keyPress[self.keyDown]:
            self.pObject.accelerateDown()
        if keyPress[self.keyLeft]:
            self.pObject.accelerateLeft()
        if keyPress[self.KeyRight]:
            self.pObject.accelerateRight()
        if keyPress[self.keyRotateRight]:
            self.pObject.accelerateRotation()
        if keyPress[self.keyRotateLeft]:
            self.pObject.deccelerateRotation()
        if keyPress[self.keyZoomIn]:
            self.zoom += 0.001
        if keyPress[self.keyZoomOut]:
            self.zoom -= 0.001
            
    def keyUpPress(self,keyPress,pObjects):
        if keyPress == self.keySwitchObject:
            pObject2 = self.getNextObject(pObjects)
            self.setFrameOfRefernce(self.pObject,pObject2)
            self.pObject = pObject2
            self.pObject.disableMotion()
            pygame.display.update()
    
    def getTranslatedXCoord(self,xCoord):
        """
        returns the x coord of the relitive to the player
        """
        return int((xCoord*self.zoom)+reference.CENTER_SCREEN_WIDTH+self.xView)
    
    def getTranslatedYCoord(self,yCoord):
        """
        returns the y coord of the relitive to the player
        """
        return int((yCoord*self.zoom)+reference.CENTER_SCREEN_HEIGHT+self.yView)
    
    def setFrameOfRefernce(self,pObject1,pObject2):
        """
        shifts the frame of reference to the second object
        """
        self.xView += pObject1.xCoord - pObject2.xCoord
        self.yView += pObject1.yCoord - pObject2.yCoord
     
    def updatePlayer(self):
        """
        updates the relative motion all object
        """
        self.xMotion = self.pObject.xMotion
        self.yMotion = self.pObject.yMotion
        
    def getNextObject(self,pObjects):
        """
        returns the next object from the object list
        """
        self.pObject.enableMotion()
        i = 0
        while (pObjects[i] != self.pObject):
            i+=1
        return pObjects[i+1 if i+1<len(pObjects) else 0]
        