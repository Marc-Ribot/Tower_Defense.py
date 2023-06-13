import pygame
from pygame.locals import *
import os
import sys
from Bichos.Bicho1 import Bicho1
from Bichos.Bicho2 import Bicho2
from Bichos.Bicho3 import Bicho3
from torres.torre1 import Torre1
from torres.torre2 import Torre2
from torres.torre3 import Torre3
from menus.in_game_menu import *
import time
import random

pygame.init()
lifes_image = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/cor.jpg")), (40,40))
monedas_image = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/moneda.png")), (40,40))
background_menu = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/bg.png")), (150, 270))
upper_menu = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/bg.png")), (550, 80))
buy_torre1 = pygame.transform.scale(pygame.image.load(os.path.join("torres/1/200.png")), (70, 70))
buy_torre2 = pygame.transform.scale(pygame.image.load(os.path.join("torres/2/401.png")), (70, 70))
buy_torre3 = pygame.transform.scale(pygame.image.load(os.path.join("torres/3/301.png")), (70, 70))
play_button = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/play.jpg")), (70, 70))
pause_button = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/Pause.jpg")), (70, 70))
music_on_button = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/Musica.jpg")), (70, 70))
music_off_button= pygame.transform.scale(pygame.image.load(os.path.join("Imatges/Musicaoff.jpg")), (70, 70))
close_button = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/tancar.jpg")), (70, 70))

# cargar la música
pygame.mixer.music.load(os.path.join("Imatges/morenita.mp3"))

# definir colocación de torres en el mapa
torres_names = ["Torre1", "Torre2", "Torre3"]
areas_permitidas = [(27,285),(290, 425),(446, 385),(830, 420),(460, 50),(610, 190),(27, 50),(460,70),(1030,50),(1100, 650),(815,50),(1030,190)]
# Oleadas de enemigos [Bicho1(), Bicho2(), Bicho3()]
oleadas = [[25, 5, 0], [30, 5, 6], [0, 60, 10], [100, 50, 20], [0, 100, 40], [131, 12, 70], [75, 150, 60]]

class Juego:
    def __init__ (self, speed, difficulty):
        print (speed, difficulty)
        self.width = 1200
        self.height = 650
        self.win = pygame.display.set_mode((self.width, self.height))
        self.bichos = []
        self.torres = []
        self.background = pygame.image.load(os.path.join("Imatges/Mapa.png"))
        self.menu = BuyMenu(1050, 0, background_menu)
        self.menu.add_buttons_torres(buy_torre1, "buy_torre1", 400)
        self.menu.add_buttons_torres(buy_torre2, "buy_torre2", 620)
        self.menu.add_buttons_torres(buy_torre3, "buy_torre3", 750)
        self.timer = time.time()
        self.text_font = pygame.font.Font("freesansbold.ttf", 32)
        self.selected_torre = None
        self.object_moving = None
        self.oleada = 0
        self.current_oleada = oleadas[self.oleada][:]
        self.pause = True
        self.muted = False
        self.play_button = PlayButton(play_button, pause_button, 10, 575)
        self.sound_button = MuteButton(music_on_button, music_off_button, 100, 575)
#        self.close_button = Button ()

        # Cambiar modo de juego segun la velocidad y dificultad del menu ajustes
        if speed == "Media":
            self.clock_speed = 100
        else:
            self.clock_speed = 1000

        if difficulty == "Media":
            self.lifes = 50
            self.monedas = 1600
        elif difficulty == "Alta":
            self.lifes = 25
            self.monedas = 1600
        else:
            self.lifes = 5
            self.monedas = 2000



    def generar_oleadas(self):
        """
        genera las oleadas de enemigos
        :return: bicho
        """
        if sum(self.current_oleada) == 0:
            if len(self.bichos) == 0:
                self.oleada += 1
                self.current_oleada = oleadas[self.oleada]
                self.pause = True
                self.play_button.paused = self.pause
        else:
            oleada_bichos = [Bicho1(), Bicho2(), Bicho3()]
            for e in range(len(self.current_oleada)):
                if self.current_oleada[e] != 0:
                    self.bichos.append(oleada_bichos[e])
                    self.current_oleada[e] = self.current_oleada[e] - 1
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
            # oleadas de bichos
                if time.time() - self.timer >= random.randrange(1,5)/2:
                    self.timer = time.time()
                    self.generar_oleadas()

            pos = pygame.mouse.get_pos()


            # mover torres y comprobar que no se solapen
            if self.object_moving:
                self.object_moving.mover(pos[0], pos[1])
                allowed = True

                if self.within_limits(self.object_moving):
                    allowed = True
                    self.object_moving.set_color = (0, 0, 255, 100)
                else:
                    allowed = False
                    self.object_moving.set_color = (255, 0, 0, 100)
                for torre in self.torres[:]:
                    if torre.space_match(self.object_moving):
                        allowed = False
                        torre.set_color = (255, 0, 0, 100)
                        self.object_moving.set_color = (255, 0, 0, 100)
                    elif not self.within_limits(self.object_moving):
                        allowed = False
                        self.object_moving.set_color = (255, 0, 0, 100)
                    else:
                        torre.set_color = (0, 0, 255, 100)
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
                        for torre in self.torres[:]:
                            if torre.space_match(self.object_moving):
                                allowed = False
                        if allowed and self.within_limits(self.object_moving):

                            if self.object_moving.name in torres_names:
                                self.torres.append(self.object_moving)
                            self.object_moving.moving = False
                            self.object_moving = None

                    else:
                        #mirar si esta en play o pausa
                        if self.play_button.click(pos[0], pos[1]):
                            self.pause = not(self.pause)
                            self.play_button.paused = self.pause

                        if self.sound_button.click(pos[0], pos[1]):
                            self.muted = not(self.muted)
                            self.sound_button.muted = self.muted
                            if not self.muted:
                                pygame.mixer.music.unpause()
                            else:
                                pygame.mixer.music.pause()

                        # mirar si se compra una torre del menú
                        button_buy = self.menu.selected(pos[0], pos[1])
                        if button_buy:
                            precio_torre = self.menu.get_torre_precio(button_buy)
                            if self.monedas >= precio_torre:
                                self.monedas -= precio_torre
                                self.add_torres(button_buy)

                        # mirar si se clica una torre del menú
                        button_clicked = None
                        if self.selected_torre:

                            button_clicked = self.selected_torre.menu.selected(pos[0], pos[1])
                            if button_clicked:
                                self.selected_torre.draw(self.win)
                                if button_clicked == "mejora":
                                    precio = self.selected_torre.get_mejora_precio()
                                    if self.monedas >= precio:
                                        self.monedas -= precio
                                        self.selected_torre.mejora()
                        if not(button_clicked):
                            for torre in self.torres:
                                if torre.click(pos[0], pos[1]):
                                    torre.selected = True
                                    self.selected_torre = torre
                                else:
                                    torre.selected = False

            # terminar loop y eliminar enemigos y vidas
            if not(self.pause):
                to_del = []
                for bicho in self.bichos:
                    bicho.mover()
                    if bicho.y < -15:
                        to_del.append(bicho)
                for d in to_del:
                    self.lifes -= 1
                    self.bichos.remove(d)

                #terminar loop torres
                for torre in self.torres:
                    self.monedas += torre.attack(self.bichos)

                #si se pierde
                if self.lifes <= 0:
                    print("GAME OVER")
                    run = False

            self.draw()

        pygame.quit()

    def draw(self):
        """
        draw los elementos del juego
        :return: surface
        """
        self.win.blit(self.background, (0,0))
        #for p in self.clicks:
         #   pygame.draw.circle(self.win, (255,0,0), (p[0], p[1]), 5, 0) #se puede borrar era para crear camino enemigos

       #draw torres
        for torre in self.torres:
            torre.draw(self.win)

        #draw espacio destinado a torre
        if self.object_moving:
            for torre in self.torres:
                torre.draw_placement(self.win)
            self.object_moving.draw_placement(self.win)

        #draw enemigos
        for bicho in self.bichos:
            bicho.draw(self.win)


        #draw tablero superior
        self.win.blit(upper_menu, (-100,-10))

        #draw vidas
        life = lifes_image
        self.win.blit(life, (20, 10))
        value_life = self.text_font.render(str(self.lifes), 1, (255,255,255))
        self.win.blit(value_life, (65,18))

        #draw monedaas
        monedas = monedas_image
        self.win.blit(monedas, (120, 10))
        value_monedas = self.text_font.render(str(self.monedas), 1, (255, 255, 255))
        self.win.blit(value_monedas, (170, 18))

        #draw torre moviendose
        if self.object_moving:
            self.object_moving.draw(self.win)

        #draw menu
        self.menu.draw(self.win)

        # draw boton jugar
        self.play_button.draw(self.win)

        # draw oleada
        text = self.text_font.render("oleada " + str(self.oleada + 1), 1, (255,255,255))
        self.win.blit(text, (300, 18))

#       self.close_button.draw(self.win)

        self.sound_button.draw(self.win)


        pygame.display.update()

    def add_torres(self, name):
        """
        Añadir las torres en el mapa
        :param name: str
        :return: surface
        """
        x,y = pygame.mouse.get_pos()
        list_names = ["buy_torre1", "buy_torre2", "buy_torre3"]
        list_torres = [Torre1(x,y), Torre2(x,y), Torre3(x,y)]

        try:
            twr = list_torres[list_names.index(name)]
            self.object_moving = twr
            twr.moving = True
        except Exception as e:
            print(str(e) + "NOT VALID")
    
    def within_limits(self, object):
        """
        retorna si la torre se esta insertando dentro de la zona permitida
        :return: Bool
        """
        x,y = pygame.mouse.get_pos()
        count = 1

        #print ("(", object.x,",", object.y, ")")

        for rectangle in areas_permitidas:

            #los impares contienen xmin e ymin
            if count%2 != 0:
                previously_ok = False
                if object.x > rectangle[0] and object.y > rectangle[1]:
                   previously_ok = True
            
            #pares contienen xmax e ymax
            else:
                if object.x < rectangle[0] and object.y < rectangle[1] and previously_ok:
                    return True

            count += 1
        return False
