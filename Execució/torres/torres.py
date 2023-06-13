import pygame
import os
import math
from menus.in_game_menu import Menu

mejora_menu = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/menumillora.png")), (125, 60))
mejora_button = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/millora.png")), (50, 50))


class Torres():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 0
        self.altura = 0
        self.price = [0,0,0]
        self.level = 1
        self.max_level = 3
        self.selected = False
        self.menu = Menu(self, self.x - 63, self.y + 45, mejora_menu, [1000, 3000, "MAX"])
        self.menu.add_buttons_mejora(mejora_button, "mejora")
        self.image = None
        self.imagenes = []
        self.animation_count = 0
        self.inrango = False
        self.rango = 0
        self.daño = 0
        self.moving = False
        self.set_color = (0,0,255,100)



    def draw_placement (self,win):
        """
        Dibuja rango de colocacion alrededor de la torre
        :param win: surface
        :return: None
        """
        surface = pygame.Surface((self.rango*4, self.rango*4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.set_color, (45,45), 45, 0)

        win.blit(surface, (self.x - 50, self.y - 50))

    def click(self, x, y):

        #Devuelve un booleano si se selecciona la torre mediante un click

        if x >= self.x - 50 and x <= self.x + self.ancho:
            if y >= self.y - 50 and y <= self.y + self.altura:
                return True
        return False

    def rango(self, r):

        #función utilizada para cambiar el rango de la torre como un integer

        self.rango = r

    def draw(self, win):
        """
        Dibuja la torre, el menú y el rango de disparo de la torre
        :param win: surface
        :return: None
        """
        # Dibujar torre
        if self.inrango and not self.moving:
            self.animation_count += 1
            if self.animation_count >= len(self.imagenes) * 5:
                self.animation_count = 0
        else:
            self.animation_count = 0

        torre = self.imagenes[self.animation_count // 5]
        win.blit(torre, (self.x - 50, self.y - 50))

        # Dibujar menú
        if self.selected:
            self.menu.draw(win)

        # Dibujar el rango de la torre cuando se está colocando en el mapa o se hace clic
        if self.selected:
            rango_surface = pygame.Surface((self.rango * 2, self.rango * 2), pygame.SRCALPHA)
            pygame.draw.circle(rango_surface, (255, 0, 0, 100), (self.rango, self.rango), self.rango, 0)
            win.blit(rango_surface, (self.x - self.rango, self.y - self.rango))

    def attack(self, bichos):

        #Esta función ataca a los enemigos en rango, los ataca a medida que aparecen.
        #Lo ideal sería que atacase al que estuviese más cerca de la base. Si un enemigo
        #pasa de largo, no será atacado a menos que se el último en pie.

        monedas = 0
        self.inrango = False
        bichos_en_rango = []

        for bicho in bichos:
            x = bicho.x
            y = bicho.y
            distancia = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if distancia < self.rango:
                self.inrango = True
                bichos_en_rango.append(bicho)

        # Atacar al enemigo más cercano a la torre
        bichos_en_rango.sort(key=lambda x: x.x)

        if len(bichos_en_rango) > 0:
            bicho_mas_cercano = bichos_en_rango[0]
            if self.animation_count == 25:  # Golpear al enemigo después de 25 imágenes de la torre
                if bicho_mas_cercano.atacar(self.daño):
                    monedas = bicho_mas_cercano.monedas
                    bichos.remove(bicho_mas_cercano)  # Eliminar el enemigo si se queda sin vida

        return monedas

    def mejora(self):
        """
        subir de nivel la torre
        :return: None
        """
        if self.level < self.max_level:
            self.level += 1
            self.daño += 1
            self.rango += 50

    def get_mejora_precio(self):

        #Este getter devuelve el precio de mejorar una torre, este es un integer que será 0
        #en caso de que no se pueda mejorar más 

        return self.menu.get_object_precio()

    def space_match(self, other_torre):

        #Esta función retorna un booleano cuando se intenta colocar una nueva torre, para evitar
        #que se coloquen una encima de la otra.

        x2, y2 = other_torre.x, other_torre.y
        distance = math.sqrt((x2 - self.x) ** 2 + (y2 - self.y) ** 2)
        return distance < 50

    def mover(self, x, y):

        #Función utilizada para mover las torres

        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update()
