import pygame
import os
from enemies import Enemigos

# Ruta de la imagen del enemigo
image_path = "Imatges\Enemic1.jpg"

# Carga la imagen del enemigo
image = pygame.transform.scale(pygame.image.load(image_path), (64, 64))

class Enemy1(Enemigos):
    def __init__(self):
        super().__init__()
        self.gems = 4
        self.image = image
        self.rect = self.image.get_rect()
        self.max_health = 3
        self.health = self.max_health




