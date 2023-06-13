import pygame
import os
from .Bicho import Bicho

imagenes = []

# recorre las imagenes del enemigo para dar mobilidad
for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imagenes.append(pygame.transform.scale(
        pygame.image.load(os.path.join("Bichos/3", "1" + add_str + ".png")), (90, 90)))

class Bicho3(Bicho):
    def __init__(self):
        super().__init__()
        self.monedas = 20
        self.imagenes = imagenes[:]
        self.max_puntos_de_vida = 9
        self.puntos_de_vida = self.max_puntos_de_vida

