import pygame
from pygame.locals import *
import os
import sys
from enemy1 import Enemy1
from tower1 import Tower1
from in_game_menu import *
import time
import random

pygame.init()
lifes_image = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/cor.jpg")), (40,40))
gems_image = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/gemas.png")), (40,40))
background_menu = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/bg.png")), (150, 270))
upper_menu = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/bg.png")), (550, 80))
buy_tower1 = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/Torres/1/shoot_000.png")), (70, 70))
buy_tower2 = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/Torres/Torre cost 2.jpg")), (70, 70))
buy_tower3 = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/Torres/Torre cost 5.jpg")), (70, 70))
play_button = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/play.jpg")), (70, 70))
pause_button = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/Pause.jpg")), (70, 70))
close_button = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/tancar.jpg")), (70, 70))
music_on_button = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/Musica.jpg")), (70, 70))
music_off_button= pygame.transform.scale(pygame.image.load(os.path.join("Imatges/Musicaoff.jpg")), (70, 70))

# definir colocación de torres en el mapa
towers_names = ["Tower1"]
areas_permitidas = [(27, 259), (266, 498), (446, 403), (670, 518), (653, 465), (911, 525), (35, 68), (606, 153), (414, 130), (588, 267), (740, 21), (783, 84), (745, 286), (1169, 390), (1027, 348), (1169, 603)]

# oleadas de enemigos definidas por numero de enemigos [Enemy1(), Enemy2(), Enemy3()]
waves = [[25], [12]]


class Juego:
    def __init__(self, speed, difficulty):
        print(speed, difficulty)
        self.width = 1200
        self.height = 650
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.background = pygame.image.load(os.path.join("maps/mapa1.jpg"))
        self.menu = BuyMenu(1050, 0, background_menu)
        self.menu.add_buttons_towers(buy_tower1, "buy_tower1", 500)
        self.menu.add_buttons_towers(buy_tower2, "buy_tower2", 600)
        self.menu.add_buttons_towers(buy_tower3, "buy_tower3", 800)
        self.timer = time.time()
        self.text_font = pygame.font.Font("freesansbold.ttf", 32)
        self.selected_tower = None
        self.object_moving = None
        self.wave = 0
        self.current_wave = waves[self.wave][:]
        self.pause = True
        self.muted = False

        #        self.close_button = Button ()

        # Cambiar modo de juego segun la velocidad y dificultad del menu ajustes
        if speed == "Media":
            self.clock_speed = 100
        else:
            self.clock_speed = 1000

        if difficulty == "Media":
            self.lifes = 50
            self.gems = 1600
        elif difficulty == "Alta":
            self.lifes = 25
            self.gems = 1600
        else:
            self.lifes = 5
            self.gems = 2000

    def generate_waves(self):
        """
        genera las oleadas de enemigos
        :return: enemy
        """
        if sum(self.current_wave) == 0:
            if len(self.enemies) == 0:
                self.wave += 1
                self.current_wave = waves[self.wave]
                self.pause = True
                self.play_button.paused = self.pause
        else:
            wave_enemies = [Enemy1()]
            for e in range(len(self.current_wave)):
                if self.current_wave[e] != 0:
                    self.enemies.append(wave_enemies[e])
                    self.current_wave[e] = self.current_wave[e] - 1
                    break

    def run(self):
        """
        Función básica del juego (main)
        :return: surface
        """
        pygame.mixer.music.play(loops=-1)
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(self.clock_speed)

            if self.pause == False:
                # oleadas de enemigos
                if time.time() - self.timer >= random.randrange(1, 5) / 2:
                    self.timer = time.time()
                    self.generate_waves()

            pos = pygame.mouse.get_pos()

            # mover torres y comprobar que no se solapen
            if self.object_moving:
                self.object_moving.move(pos[0], pos[1])
                allowed = True

                if self.within_limits(self.object_moving):
                    allowed = True
                    self.object_moving.set_color = (0, 0, 255, 100)
                else:
                    allowed = False
                    self.object_moving.set_color = (255, 0, 0, 100)
                for tower in self.towers[:]:
                    if tower.space_match(self.object_moving):
                        allowed = False
                        tower.set_color = (255, 0, 0, 100)
                        self.object_moving.set_color = (255, 0, 0, 100)
                    elif not self.within_limits(self.object_moving):
                        allowed = False
                        self.object_moving.set_color = (255, 0, 0, 100)
                    else:
                        tower.set_color = (0, 0, 255, 100)
                        if allowed:
                            self.object_moving.set_color = (0, 0, 255, 100)

            # main
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:
                    # escoger y mover torres por el mapa
                    if self.object_moving:
                        allowed = True
                        for tower in self.towers[:]:
                            if tower.space_match(self.object_moving):
                                allowed = False
                        if allowed and self.within_limits(self.object_moving):

                            if self.object_moving.name in towers_names:
                                self.towers.append(self.object_moving)
                            self.object_moving.moving = False
                            self.object_moving = None

                    else:
                        # mirar si esta en play o pausa
                        if self.play_button.click(pos[0], pos[1]):
                            self.pause = not (self.pause)
                            self.play_button.paused = self.pause

                        if self.sound_button.click(pos[0], pos[1]):
                            self.muted = not (self.muted)
                            self.sound_button.muted = self.muted
                            if not self.muted:
                                pygame.mixer.music.unpause()
                            else:
                                pygame.mixer.music.pause()

                        # mirar si se compra una torre del menú
                        button_buy = self.menu.selected(pos[0], pos[1])
                        if button_buy:
                            cost_tower = self.menu.get_tower_cost(button_buy)
                            if self.gems >= cost_tower:
                                self.gems -= cost_tower
                                self.add_towers(button_buy)

                        # mirar si se clica una torre del menú
                        button_clicked = None
                        if self.selected_tower:

                            button_clicked = self.selected_tower.menu.selected(pos[0], pos[1])
                            if button_clicked:
                                self.selected_tower.draw(self.win)
                                if button_clicked == "Upgrade":
                                    cost = self.selected_tower.get_upgrade_cost()
                                    if self.gems >= cost:
                                        self.gems -= cost
                                        self.selected_tower.upgrade()
                        if not (button_clicked):
                            for tower in self.towers:
                                if tower.click(pos[0], pos[1]):
                                    tower.selected = True
                                    self.selected_tower = tower
                                else:
                                    tower.selected = False

            # terminar loop y eliminar enemigos y vidas
            if not (self.pause):
                to_del = []
                for enemy in self.enemies:
                    enemy.move()
                    if enemy.y < -15:
                        to_del.append(enemy)
                for d in to_del:
                    self.lifes -= 1
                    self.enemies.remove(d)

                # terminar loop torres
                for tower in self.towers:
                    self.gems += tower.attack(self.enemies)

                # si se pierde
                if self.lifes <= 0:
                    print("GAME OVER")
                    run = False

            self.draw()

        pygame.quit()

    def draw(self):
        """
        dibujar los elementos del juego
        :return: surface
        """
        self.win.blit(self.background, (0, 0))
        # for p in self.clicks:
        #   pygame.draw.circle(self.win, (255,0,0), (p[0], p[1]), 5, 0) #se puede borrar era para crear camino enemigos

        # dibujar torres
        for tower in self.towers:
            tower.draw(self.win)

        # dibujar espacio destinado a torre
        if self.object_moving:
            for tower in self.towers:
                tower.draw_placement(self.win)
            self.object_moving.draw_placement(self.win)

        # dibujar enemigos
        for enemy in self.enemies:
            enemy.draw(self.win)

        # dibujar tablero superior
        self.win.blit(upper_menu, (-100, -10))

        # dibujar vidas
        life = lifes_image
        self.win.blit(life, (20, 10))
        value_life = self.text_font.render(str(self.lifes), 1, (255, 255, 255))
        self.win.blit(value_life, (65, 18))

        # dibujar gemas
        gems = gems_image
        self.win.blit(gems, (120, 10))
        value_gems = self.text_font.render(str(self.gems), 1, (255, 255, 255))
        self.win.blit(value_gems, (170, 18))

        # dibujar torre moviendose
        if self.object_moving:
            self.object_moving.draw(self.win)

        # dibujar menu
        self.menu.draw(self.win)

        # dibujar boton jugar
        self.play_button.draw(self.win)

        # dibujar oleada
        text = self.text_font.render("Wave " + str(self.wave + 1), 1, (255, 255, 255))
        self.win.blit(text, (300, 18))

        #       self.close_button.draw(self.win)

        self.sound_button.draw(self.win)

        pygame.display.update()

    def add_towers(self, name):
        """
        Añadir las torres en el mapa
        :param name: str
        :return: surface
        """
        x, y = pygame.mouse.get_pos()
        list_names = ["buy_tower1", "buy_tower2", "buy_tower3"]
        list_towers = [Tower1(x, y)]

        try:
            twr = list_towers[list_names.index(name)]
            self.object_moving = twr
            twr.moving = True
        except Exception as e:
            print(str(e) + "NOT VALID")

    def within_limits(self, object):
        """
        retorna si la torre se esta insertando dentro de la zona permitida
        :return: Bool
        """
        x, y = pygame.mouse.get_pos()
        count = 1

        # print ("(", object.x,",", object.y, ")")

        for rectangle in areas_permitidas:

            # los impares contienen xmin e ymin
            if count % 2 != 0:
                previously_ok = False
                if object.x > rectangle[0] and object.y > rectangle[1]:
                    previously_ok = True

            # pares contienen xmax e ymax
            else:
                if object.x < rectangle[0] and object.y < rectangle[1] and previously_ok:
                    return True

            count += 1
        return False