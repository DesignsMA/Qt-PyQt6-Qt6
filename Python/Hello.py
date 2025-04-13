import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget): # heredar de la clase QtWidgets.QtWidget

  def __init__(self): # instancia de widget padre (contenedor de toda la ventana)
    super().__init__() # inicializar clase padre
    self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
    self.button = QtWidgets.QPushButton("Click me!") # instancia de widget boton tipo push
    self.txt = QtWidgets.QLabel("Hello World",
                                alignment = QtCore.Qt.AlignCenter) # añadir label en el centro

    self.layout = QtWidgets.QVBoxLayout(self) # crear contenedor de tipo caja
    self.layout.addWidget(self.txt) # añadir label al contenedor
    self.layout.addWidget(self.button)

    self.button.clicked.connect(self.magic) # conectar funcion al ser clickeado

  @QtCore.Slot() # define una funcion externa
  def magic(self): # recibe el widget padre
      self.txt.setText(random.choice(self.hello)) # elegir un texto aleatorio al instanciar


if __name__ == "__main__": # ejecutar codigo
    app = QtWidgets.QApplication([]) # instancia de app

    widget = MyWidget() # instancia del widget principal
    widget.resize(800,600) # cambiar tamaño
    widget.show() # mostrar widget

    sys.exit(app.exec()) # al salir ejecutar app
    
