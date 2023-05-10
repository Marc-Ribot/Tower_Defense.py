from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QApplication,QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

import sys

# Crea una instancia de QGraphicsScene
app = QApplication(sys.argv)

# Crea una instancia de QPixmap con la imagen del mapa
scene = QGraphicsScene()
view = QGraphicsView(scene)

# Crea un elemento QGraphicsPixmapItem y establece la imagen del mapa
image_path = r"C:\Users\mribo\Downloads\1.jpg"  # Ruta de la imagen
image = QPixmap(image_path)

# Agrega el elemento gráfico a la escena
pixmap_item = QGraphicsPixmapItem(image)



# Crea una instancia de QGraphicsView y establece la escena
scene.addItem(pixmap_item)

view.fitInView(scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
view.show()
sys.exit(app.exec_())



