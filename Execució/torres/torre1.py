import pygame
import os
from .torres import Torres
import math

imagenes = []

# Ensenya imatges de torres
for im in range(8):
    add_str = "0" + str(im)
    imagenes.append(
        pygame.transform.scale(pygame.image.load(os.path.join("torres/1", "2" + add_str + ".png")),
                               (100, 100)))

class Torre1(Torres):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.imagenes = imagenes[:]
        self.rango = 190
        self.daño = 1
        self.name = "Torre1"



