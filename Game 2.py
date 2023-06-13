from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTableWidgetItem, QTableWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from Monedero import Monedero
from Bichoz import Bicho
from torre import Torre
from Mapa_qtdesigner2 import map_matrix, desired_height, desired_width
import Imatges_rc

# Bichos
Enemigo1 = Bicho(1, 50, 3, 0, (0, 12), 5)

# Torretas
Torre1 = Torre(10, 5, (4, 4), 5, 6, 2)

class Game:
    def __init__(self, map_matrix):
        self.app = QApplication([])
        self.window = QMainWindow()
        self.ui = loadUi("Principal.ui", self.window)

        # Guardar la matriz del mapa
        self.map_matrix = map_matrix

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
        self.torre_label = self.map_ui.findChild(QLabel, "torre_5")
        self.map_ui.findChild(QPushButton, "Torre_5").clicked.connect(self.enable_tower_placement)

        Torre1.label = self.torre_label

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

    def enable_tower_placement(self):
        # Desactivar la funcionalidad del botón "torre_5" mientras se selecciona la casilla
        self.map_ui.findChild(QPushButton, "Torre_5").setEnabled(False)

        # Conectar la señal de clic de cada casilla en el mapa a la función para agregar la torre
        table_widget = self.map_ui.findChild(QTableWidget, "nombre_de_tu_tabla")
        if table_widget is not None:
            table_widget.cellClicked.connect(self.on_cell_clicked)
        else:
            print("No se encontró la tabla en la interfaz del mapa.")

    def on_cell_clicked(self, row, col):
        # Verificar si la casilla está disponible
        if (row, col) in casillas_disponibles:
            # Agregar una torre en la posición seleccionada
            self.map_matrix[row][col] = 1  # Actualizar la matriz del mapa para marcar la casilla ocupada

            # Actualizar la interfaz del mapa para mostrar la torre en la casilla seleccionada
            item = QTableWidgetItem(str(1))
            table_widget = self.map_ui.findChild(QTableWidget, "nombre_de_tu_tabla")
            if table_widget is not None:
                table_widget.setItem(row, col, item)

            # Restar el costo de la torre del monedero del jugador
            if self.monedero.get_money() >= Torre1.preu:
                self.monedero.decrease_money(Torre1.preu)
                self.update_monedero()
            else:
                print("No tienes suficiente dinero para comprar esta torre.")

            # Desconectar el evento cellClicked
            table_widget.cellClicked.disconnect(self.on_cell_clicked)

        else:
            print("La casilla seleccionada no está disponible para colocar la torre.")

# Crear una instancia del juego y ejecutarlo
game = Game(map_matrix)
game.run()
