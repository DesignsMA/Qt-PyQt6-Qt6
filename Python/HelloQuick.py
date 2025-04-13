import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

# Crear instancia de QQmlApplicationEngine donde cargaremos el QML (Version declarativa)

if __name__=="__main__":
  app = QGuiApplication(sys.argv) # mandar argumentos de ejecucion
  engine = QQmlApplicationEngine() # instancia de engine de ejecucion
  engine.addImportPath(sys.path[0]) # aniadir ruta de importacion | Ruta actual
  engine.loadFromModule("Modules", "Main") # Cargar programa de el modulo Modules | Main
  if not engine.rootObjects(): # error de creacion
    sys.exit()
  exit_code=app.exec() # ejecutar app construida del modulo y guardar codigo de salida recibido
  del engine # borrar instancia de engine
  sys.exit(exit_code) # salir y mandar el mismo codigo al salir de la app principal



