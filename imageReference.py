# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 10:50:10 2016

@author: S070726047
"""

import pygame
import os

def getImage(directory,filename):
    try:
        fn = os.path.join(os.path.dirname(__file__) + "/" + directory, filename)
        image = pygame.image.load(fn)
    except (pygame.error, message):
        print ("Cannot load image:", filename)
        raise (SystemExit, message)
    
    return image

livingObject = getImage("resources","BasicLivingEntity.png")