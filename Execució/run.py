#from games.game1 import Juego
#from menus.GUI_Menu import GUI_Menu

#menu = GUI_Menu
#menu.run()

#j = Juego()
#j.run()  Falta canviar noms de funcions i ses funcions en si. 
#i cuadrat

from Principal import MenuPrincipal
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TowerDefenseMainMenu = QtWidgets.QMainWindow()
    ui = MenuPrincipal()
    ui.setupUi(TowerDefenseMainMenu)
    TowerDefenseMainMenu.show()
    sys.exit(app.exec_())
