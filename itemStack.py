# -*- coding: utf-8 -*-
import item

class ItemStack(object):
    
    def __init__(self,item2,material,stackNum,data):
        self.item2 = item2
        self.stackNum = stackNum
        self.data = data