from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import Imatges_rc


class Game:
    def __init__(self):
        self.app = QApplication([])
        self.window = QMainWindow()
        self.ui = loadUi("Principal.ui", self.window)

        # Personaliza la interfaz y agrega las funcionalidades necesarias

        self.ui.PlayButton.clicked.connect(self.run)

        self.map_window = None
        self.map_ui = None

    def run(self):
        self.window.hide()

        # Cargar la interfaz del mapa
        self.map_window = QMainWindow()
        self.map_ui = loadUi("Mapa1.ui", self.map_window)

        # Personalizar la interfaz del mapa y agregar las funcionalidades necesarias

        # Mostrar la ventana del mapa
        self.map_window.show()

        # Iniciar el bucle de eventos de la aplicación
        self.app.exec_()


# Crear una instancia de la clase Game y comenzar el juego
game = Game()
game.ui.show()  # Mostrar la ventana principal
game.app.exec_()
