import pygame
import math
import os

class Bicho():
    def __init__(self):
        self.ancho = 64
        self.altura = 64
        self.velocidad = 1
        self.puntos_de_vida = 0
        self.max_puntos_de_vida = 0
        self.init_camino = 0
        self.camino = [(-10, 188), (4, 188), (295, 193), (345, 217), (365, 272), (370, 332), (370, 550), (443, 555), (554, 555), (668, 555), (920, 555), (925, 506), (928, 454), (920, 380), (890, 340), (750, 330), (700, 293), (700, 3), (700, -10)]
        self.x = self.camino[0][0]
        self.y = self.camino[0][1]
        self.contador_movimientos = 0
        self.animation_count = 0
        self.image = None
        self.distancia = 0
        self.mover_distancia = 0
        self.flipped = False
        self.imagenes = []

    def draw(self, win):
        """
        Dibuja al enemigo
        :param win: surface
        :return: None
        """
        self.image = self.imagenes[self.animation_count]
        enemy_rect = self.image.get_rect(center=(self.x, self.y))

        win.blit(self.image, enemy_rect)
        self.puntos_de_vida_barra(win)

    def puntos_de_vida_barra(self, win):
        """
        Dibuja la barra de salud del enemigo
        :param win: surface
        :return: None
        """
        length = 50
        mover = round(length / self.max_puntos_de_vida)
        puntos_de_vida_barra = mover * self.puntos_de_vida

        barra_rect = pygame.Rect(self.x - 30, self.y - 60, length, 10)
        puntos_rect = pygame.Rect(self.x - 30, self.y - 60, puntos_de_vida_barra, 10)

        pygame.draw.rect(win, (255, 0, 0), barra_rect, 0)
        pygame.draw.rect(win, (0, 255, 0), puntos_rect, 0)

    def colisionar(self, x, y):
        """
        Devuelve si la posición toca al enemigo
        :param x: int
        :param y: int
        :return: bool
        """
        return self.x <= x <= self.x + self.ancho and self.y <= y <= self.y + self.altura

    def mover(self):
        """
        Mover los enemigospor el camino definido con los puntos
        :return: None
        """
        self.animation_count += 1
        if self.animation_count >= len(self.imagenes):
            self.animation_count = 0


        x1,y1 = self.camino[self.init_camino]
        if self.init_camino +1 >= len(self.camino):
            x2, y2 = (-10, 3)
        else:
            x2, y2 = self.camino[self.init_camino+1]

        dif = (x2-x1, y2-y1)
        length = math.sqrt((dif[0])**2 + (dif[1])**2)
        dif = (dif[0]/length, dif[1]/length)

        if dif[0] < 0 and not (self.flipped):
            self.flipped = True
            for x, img in enumerate(self.imagenes):
                self.imagenes[x] = pygame.transform.flip(img, True, False)


        x_mover, y_mover = (self.x + dif[0], self.y + dif[1])

        self.x = x_mover
        self.y = y_mover

        #Ir al siguiente punto
        if dif[0] >= 0: # a la derecha
            if dif[1] >= 0: #a bajo
                if self.x >= x2 and self.y >= y2:
                    self.init_camino += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.init_camino += 1
        else:
            if dif[1] >= 0:  # a bajo
                if self.x <= x2 and self.y >= y2:
                    self.init_camino += 1
            else:
                if self.x <= x2 and self.y <= y2:
                    self.init_camino += 1

                if self.x >= x2 and self.y == y2:
                    self.distancia = 0
                    self.init_camino += 1

    def atacar(self, daño):
        """
        Esta función permite quitarle vida al enemigo y hacerle desaparecer en caso de
        que su vida sea menor o igual que 0. Devuelve un booleano.
        """
        self.puntos_de_vida -= daño
        return self.puntos_de_vida <= 0

