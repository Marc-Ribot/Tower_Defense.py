import pygame
import math
import os

class Enemigos:
    def __init__(self):
        self.ancho = 64
        self.alto = 64
        self.velocidad = 1
        self.vida = 0
        self.vida_maxima = 0
        self.punto_inicial = 0
        self.camino = [(-10, 188), (4, 188), (290, 193), (336, 217), (355, 272), (359, 332), (359, 564), (443, 574), (554, 577), (668, 578), (958, 568), (990, 506), (964, 454), (895, 436), (711, 425), (679, 362), (670, 293), (669, 3), (669, -10)]
        self.x = self.camino[0][0]
        self.y = self.camino[0][1]
        self.imagen = None

    def dibujar(self, superficie):
        superficie.blit(self.imagen, (self.x - 30, self.y - 55))
        self.barra_vida(superficie)

    def barra_vida(self, superficie):
        longitud = 50
        movimiento = round(longitud / self.vida_maxima)
        barra_vida = movimiento * self.vida

        pygame.draw.rect(superficie, (255, 0, 0), (self.x - 30, self.y - 60, longitud, 10), 0)
        pygame.draw.rect(superficie, (0, 255, 0), (self.x - 30, self.y - 60, barra_vida, 10), 0)

    def colisionar(self, x, y):
        if x <= self.x + self.ancho and x >= self.x:
            if y <= self.y + self.alto and y >= self.y:
                return True
        return False

    def mover(self):
        x1, y1 = self.camino[self.punto_inicial]
        if self.punto_inicial + 1 >= len(self.camino):
            x2, y2 = (-10, 3)
        else:
            x2, y2 = self.camino[self.punto_inicial+1]

        dif = (x2-x1, y2-y1)
        longitud = math.sqrt((dif[0])**2 + (dif[1])**2)
        dif = (dif[0]/longitud, dif[1]/longitud)

        x_movimiento, y_movimiento = (self.x + dif[0], self.y + dif[1])

        self.x = x_movimiento
        self.y = y_movimiento

        if dif[0] >= 0:
            if dif[1] >= 0:
                if self.x >= x2 and self.y >= y2:
                    self.punto_inicial += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.punto_inicial += 1
        else:
            if dif[1] >= 0:
                if self.x <= x2 and self.y >= y2:
                    self.punto_inicial += 1
            else:
                if self.x <= x2 and self.y <= y2:
                    self.punto_inicial += 1

                if self.x >= x2 and self.y == y2:
                    self.distancia = 0
                    self.punto_inicial += 1

    def recibir_ataque(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            return True
        return False
