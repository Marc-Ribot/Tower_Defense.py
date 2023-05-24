from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from Monedero import Monedero
import Imatges_rc


class Game:
    def __init__(self):
        self.app = QApplication([])
        self.window = QMainWindow()
        self.ui = loadUi("Principal.ui", self.window)

        # Personaliza la interfaz y agrega las funcionalidades necesarias
        self.timer = QTimer()

        self.ui.PlayButton.clicked.connect(self.run)

        self.map_window = None
        self.map_ui = None
        self.monedero = Monedero(20)

    def run(self):
        self.window.hide()

        # Cargar la interfaz del mapa
        self.map_window = QMainWindow()
        self.map_ui = loadUi("Mapa1.ui", self.map_window)

        # Personalizar la interfaz del mapa y agregar las funcionalidades necesarias

        # Obtener el QLabel del tiempo
        self.time_label = self.map_ui.findChild(QLabel, "timeLabel")
        self.money_label = self.map_ui.findChild(QLabel, "Dinero")

        # Mostrar la ventana del mapa
        self.map_window.show()

        # Configurar el temporizador para iniciar el tiempo de juego
        self.timer.timeout.connect(self.update_time_label)
        self.timer.start(1000)  # 1000 ms = 1 segundo
        self.elapsed_time = 0

        # Iniciar el bucle de eventos de la aplicación
        self.app.exec_()

    def update_time_label(self):
        self.elapsed_time += 1
        time_text = f"Tiempo: {self.elapsed_time}s"
        self.time_label.setText(time_text)

        self.update_monedero()  # Llamar al método para actualizar el valor del dinero

    def update_monedero(self):
        dinero_text = f"Dinero: {self.monedero.get_money()}$"
        self.money_label.setText(dinero_text)


# Crear una instancia de la clase Game y comenzar el juego
game = Game()
game.ui.show()  # Mostrar la ventana principal
game.app.exec_()
