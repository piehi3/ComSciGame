# -*- coding: utf-8 -*-
from enum import Enum
import material

class MaterialEnum(Enum):
    iron = material.Material(1,1,1)
    steel = material.Material(1.5,1.5,1.5)