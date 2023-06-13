import pygame
import os
from .Bicho import Bicho

imagenes = []

# recorre las imagenes del enemigo para dar mobilidad
for x in range(19):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imagenes.append(pygame.transform.scale(
        pygame.image.load(os.path.join("Bichos/1/", "0" + add_str + ".png")), (64, 64)))

class Bicho1(Bicho):
    def __init__(self):
        super().__init__()
        self.monedas = 4
        self.imagenes = imagenes[:]
        self.max_puntos_de_vida = 3
        self.puntos_de_vida = self.max_puntos_de_vida



