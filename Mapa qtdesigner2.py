from PIL import Image

# Carga la imagen del mapa
image_path = r"./imatges/1.jpg"

image = Image.open(image_path)

# Convierte la imagen a escala de grises
image_gray = image.convert("L")

# Obtén las dimensiones de la imagen
width, height = image_gray.size

# Define el tamaño deseado de la matriz
desired_width = 37
desired_height = 24

# Calcula los factores de escala para redimensionar la imagen
scale_x = width // desired_width
scale_y = height // desired_height

# Redimensiona la imagen para que se ajuste al tamaño deseado
resized_image = image_gray.resize((desired_width * scale_x, desired_height * scale_y))

# Obtiene los píxeles de la imagen redimensionada en forma de matriz
pixel_matrix = list(resized_image.getdata())

# Crea una matriz vacía para almacenar los valores del mapa
map_matrix = []

# Definir el conjunto de puntos del camino
path_points = {(0, 12), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (6, 11), (6, 10), (6, 9),
(6, 8), (6, 7), (6, 6), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (12, 5), (13, 5),
(13, 6), (13, 7), (13, 8), (13, 9), (13, 10), (13, 11), (13, 12), (13, 13), (13, 14), (13, 15), (13, 15),
(14, 15), (15, 15), (16, 15), (17, 15), (18, 15), (19, 15), (20, 15), (21, 15), (22, 15), (23, 15),
(23, 14), (23, 13), (23, 12), (23, 11), (23, 10), (24, 10), (25, 10), (26, 10), (27, 10), (28, 10), (29, 10),
(30, 10), (31, 10), (32, 10), (33, 10), (34, 10), (35, 10), (36, 10), (37, 10)}
# Agrega todos los puntos del camino

# Itera sobre los píxeles y asigna valores numéricos o símbolos según las coordenadas del camino
for i in range(desired_height):
    row = []
    for j in range(desired_width):
        # Verifica si las coordenadas están dentro del camino y asigna un valor representativo
        if (j, i) in path_points:
            row.append(1)  # Puedes utilizar cualquier número o símbolo que desees para representar el camino
        else:
            row.append(0)  # Puedes utilizar otro número o símbolo para representar otras áreas del mapa
    map_matrix.append(row)

# Ahora tienes la matriz 'map_matrix' que representa el mapa con el camino marcado utilizando el conjunto de puntos.
for row in map_matrix:
    for value in row:
        print(value, end=' ')
    print()

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
import sys


class MapWindow(QMainWindow):
    def __init__(self, map_matrix):
        super().__init__()
        self.setWindowTitle("Map Matrix")
        self.table = QTableWidget(self)
        self.table.setRowCount(len(map_matrix))
        self.table.setColumnCount(len(map_matrix[0]))

        for i, row in enumerate(map_matrix):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.table.setItem(i, j, item)

        self.setCentralWidget(self.table)
        self.show()


app = QApplication(sys.argv)
window = MapWindow(map_matrix)
sys.exit(app.exec_())

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5 import uic
import sys

