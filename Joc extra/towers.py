import pygame
import os
import math
from in_game_menu import Menu

class Towers():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0,0,0]
        self.price = [0,0,0]
        self.level = 1
        self.max_level = 3
        self.selected = False
        self.attack_speed = 1.0  # Velocidad de ataque en segundos
        self.attack_count = 0.0  # Contador para el tiempo de ataque
        self.image = None
        self.images = []
        self.animation_count = 0
        self.inRange = False
        self.range = 0
        self.damage = 0
        self.moving = False
        self.set_color = (0,0,255,100)



    def draw_placement (self,win):
        """
        Dibuja rango de colocacion alrededor de la torre
        :param win: surface
        :return: None
        """
        surface = pygame.Surface((self.range*4, self.range*4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.set_color, (45,45), 45, 0)

        win.blit(surface, (self.x - 50, self.y - 50))


    def click(self,x,y):
        """
        devuelve si la torre se clica y se selecciona
        :param x: int
        :param y: int
        :return: bool
        """
        if x - 50 <= self.x + self.width and x >= self.x:
            if y - 50 <= self.y + self.height and y >= self.y:
                return True
        return False

    def range(self, r):
        """
        cambia el rango de disparo de la torre
        :param r: int
        :return: None
        """
        self.range = r

    def draw(self, win,):
        """
        Dibuja la torre, el menu y el rango de disparo de la torre
        :param win: surface
        :return: None
        """
        # dibujar torre
        if self.inRange and not self.moving:
            self.animation_count += 1
            if self.animation_count >= len(self.images) * 5:
                self.animation_count = 0
        else:
            self.animation_count = 0

        tower = self.images[self.animation_count // 5]
        win.blit(tower, (self.x - 50, self.y - 50))

        #dibujar menu
        if self.selected:
            self.Menu.draw(win)

        # dibuja el rango de la torre cuando se esta colocando en el mapa o se clica
        if self.selected:
            sf = pygame.Surface((self.range*4, self.range*4), pygame.SRCALPHA, 32)
            pygame.draw.circle(sf, (255, 0, 0, 100), (self.range, self.range), self.range, 0)
            win.blit(sf, (self.x-self.range, self.y-self.range))

    def attack(self, enemies):
        """
        Ataca al enemigo de la lista de enemigos según la velocidad de ataque
        :param enemies: lista de enemigos
        :return: int
        """
        gems = 0
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            if distance < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        # Ordenar los enemigos por coordenada x
        enemy_closest.sort(key=lambda x: x.x)

        if len(enemy_closest) > 0:
            first_en = enemy_closest[0]
            self.attack_count += 1.0 / self.attack_speed  # Incrementar el contador de ataque

            # Realizar el ataque cuando el contador alcanza la velocidad de ataque
            if self.attack_count >= 1.0:
                if first_en.hit(self.damage):
                    gems = first_en.gems
                    enemies.remove(first_en)  # Eliminar el enemigo si se queda sin vida
                self.attack_count = 0.0  # Reiniciar el contador de ataque

        return gems

    def sell(self):
        """
        vender la torre, devuelve el precio
        :return: int
        """
        return self.sell_price[self.level - 1]





    def space_match (self, other_tower):
        """
        evita que se puedan poner dos torres en el mismo sitio generando un radio alrededor de la torre
        :return: bool
        """
        x2 = other_tower.x
        y2 = other_tower.y
        dis = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        if dis >= 50:
            return False
        else:
            return True

    def move(self, x, y):
        """
        mueve las torres
        :param x: int
        :param y: int
        :return: None
        """
        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update()
