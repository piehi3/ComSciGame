
import pygame
import math
import reference
# -*- coding: utf-8 -*-
def getPoint(player,i,size,partSide,rotation,xCoord,yCoord):
    """
    gets a point on a circle with radius size and at the angle partSides*i
    """
    return [int((size*math.sin((partSide*i)+rotation)+xCoord)*player.zoom)+reference.CENTER_SCREEN_WIDTH+player.xView,int((size*math.cos((partSide*i)+rotation)+yCoord)*player.zoom)+reference.CENTER_SCREEN_HEIGHT+player.yView]
    
def drawRegualrPolygon(player,window,color,numSides,size,rotation,xCoord,yCoord):
    """
    draws a regular polygon within the given parameters
    """
    points = [i for i in range(numSides)]
    partSide = (2*math.pi)/numSides
    for i in range(len(points)):
            points[i] = getPoint(player,i,size,partSide,rotation,xCoord,yCoord)
    pygame.draw.polygon(window, color ,points)

def drawPlayerlessPolygon(window,color,numSides,size,rotation,xCoord,yCoord):
    """
    draws a regular polygon within the given parameters not bound to a player
    """
    points = [i for i in range(numSides)]
    partSide = (2*math.pi)/numSides
    for i in range(len(points)):
            points[i] = getNonBoundPoint(i,size,partSide,rotation,xCoord,yCoord)
    pygame.draw.polygon(window, color ,points)

def getNonBoundPoint(i,size,partSide,rotation,xCoord,yCoord):
    """
    gets a point on a circle with radius size and at the angle partSides*i
    """
    return [int((size*math.sin((partSide*i)+rotation)+xCoord)*1)+0+0,int((size*math.cos((partSide*i)+rotation)+yCoord)*1)+0+0]

def drawLight(window,player,size,xCoord,yCoord,red,green,blue,alfa,fade):
    i = int(size*player.zoom)
    while i > 0:
        pygame.draw.circle(window, (int(red),int(green),int(blue),int(alfa)-int((alfa/(size*player.zoom))*i)),(player.getTranslatedXCoord(xCoord),player.getTranslatedYCoord(yCoord)),i,0)
        i -= int(fade*player.zoom)