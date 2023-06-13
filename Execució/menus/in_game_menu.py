import pygame
import os
pygame.font.init()

moneda = pygame.transform.scale(pygame.image.load(os.path.join("Imatges/moneda.png")), (25, 25))

class Button:
    """
    Botones para los menus de subir nivel
    """
    def __init__(self, menu, imagenn, name):
        self.imagenn = imagenn
        self.name = name
        self.x = menu.x + 10
        self.y = menu.y + 5
        self.menu = menu
        self.width = self.imagenn.get_width()
        self.height = self.imagenn.get_height()

    def click(self, X, Y):
        """
        devuelve si se selecciona la torre del menu o no
        :param X: int
        :param Y: int
        :return: bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
            return False

    def draw(self, win):
        """
        Dibuja la imagenn del boton
        :param win: surface
        :return: None
        """
        win.blit(self.imagen, (self.x, self.y))

    def update(self):
        """
        Recarga el botón en caso de cambio de pausa a play o de sonio a mute
        :return: None
        """
        self.x = self.menu.x + 10
        self.y = self.menu.y + 5

class MuteButton(Button):
    """
    Menu para quitar la música
    """
    def __init__(self, music_on_imagen, music_off_imagen, x, y):
        self.music_on = music_on_imagen
        self.music_off = music_off_imagen
        self.x = x
        self.y = y
        self.width = self.music_on.get_width()
        self.height = self.music_on.get_height()
        self.muted = False

    def draw(self, win):
        """
        Dibuja los botones de musica on o off
        :param win: surface
        :return: None
        """
        if self.muted:
            win.blit(self.music_off, (self.x, self.y))
        else:
            win.blit(self.music_on, (self.x, self.y))

class BuyButton(Button):
    """
    Botones para menu de compra
    """
    def __init__(self,x,y, imagen, name, precio):
        self.imagen = imagen
        self.name = name
        self.x = x
        self.y = y
        self.width = self.imagen.get_width()
        self.height = self.imagen.get_height()
        self.precio = precio

class PlayButton(Button):
    """
    Botones para parar/iniciar oleada
    """
    def __init__(self, play_imagen, pause_imagen, x, y):
        self.play = play_imagen
        self.pause = pause_imagen
        self.x = x
        self.y = y
        self.width = self.play.get_width()
        self.height = self.play.get_height()
        self.paused = True

    def draw(self, win):
        """
        Dibuja los botones play/pause
        :param win: surface
        :return: None
        """
        if self.paused:
            win.blit(self.play, (self.x, self.y))
        else:
            win.blit(self.pause, (self.x, self.y))

class Menu:
    """
    Menu para seleccionar las torres
    """
    def __init__(self, torre, x, y, imagen, torre_precio):
        self.x = x
        self.y = y
        self.width = imagen.get_width()
        self.height = imagen.get_height()
        self.torres = 0
        self.buttons = []
        self.background = imagen
        self.mejora = 0
        self.imagen_mejora = imagen
        self.torres_precio = torre_precio
        self.mejora_precio = []
        self.text_precio = pygame.font.SysFont("freesansbold", 22)
        self.object = torre

    def get_object_precio(self):
        """
        da el precioe de subir de nivel la torre
        :return: int
        """
        return self.torres_precio[self.object.level - 1]

    def draw(self, win):
        """
        crea el menu y botones
        :param win: surface
        :return: None
        """
        win.blit(self.background, (self.x, self.y))
        for i in self.buttons:
            i.draw(win)
            win.blit(moneda, (i.x + i.width + 15, i.y + 5))
            text = self.text_precio.render(str(self.torres_precio[self.object.level - 1]), 1, (255, 255, 255))
            win.blit(text, (i.x + i.width + 8, i.y + moneda.get_height() + 5))


    def add_buttons_mejora(self, imagen_up, name):
        """
        añadir los botones de las torres
        :param imagen_up: surface
        :param name: str
        :return: None
        """
        self.mejora += 1
        self.buttons.append(Button(self, imagen_up, name))

    def selected(self, X, Y):
        """
        devuelve el elemento seleccionado
        :param X: int
        :param Y: int
        :return: str
        """
        for button in self.buttons:
            if button.click(X,Y):
                return button.name
        return None

    def update(self):
        """
        carga el menu de las torres que se colocan
        :return: None
        """
        for button in self.buttons:
           button.update()

class BuyMenu(Menu):
    """
    Menu para comprar torres
    """
    def __init__(self, x, y, imagen):
        self.x = x
        self.y = y
        self.width = imagen.get_width()
        self.height = imagen.get_height()
        self.torres = 0
        self.buttons = []
        self.background = imagen
        self.mejora = 0
        self.imagen_mejora = imagen
        self.mejora_precio = []
        self.text_precio = pygame.font.SysFont("freesansbold", 22)

    def add_buttons_torres(self, imagen, name, precio):
        """
        añadir los botones de las torres
        :param imagen: surface
        :param name: str
        :return: None
        """
        self.torres += 1
        button_y = self.y + 10 + (self.torres-1)*80
        button_x = self.x + 20
        self.buttons.append(BuyButton(button_x, button_y, imagen, name, precio))

    def get_torre_precio(self, name):
        """
        da el precio de la torre
        :param name: str
        :return: int
        """
        for button in self.buttons:
            if button.name == name:
                return button.precio
        return -1

    def draw(self, win):
        """
        crea el menu y botones
        :param win: surface
        :return: None
        """
        win.blit(self.background, (self.x, self.y))
        for i in self.buttons:
            i.draw(win)
            win.blit(moneda, (i.x + i.width + 15, i.y + 12))
            text = self.text_precio.render(str(i.precio), 1, (255, 255, 255))
            win.blit(text, (i.x + i.width + 8, i.y + moneda.get_height() + 15))
