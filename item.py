# -*- coding: utf-8 -*-
class Item(object):
    
    def __init__(self,nameID,maxStackSize,mass):
        self.nameID = nameID
        self.maxStackSize = maxStackSize
        self.mass = mass