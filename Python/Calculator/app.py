from __future__ import annotations

import sys

from PySide6.QtCore import QObject, Slot, QFile, QTextStream
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement
from PySide6.QtQuickControls2 import QQuickStyle

# To be used on the @QmlElement decorator
# (QML_IMPORT_MINOR_VERSION is optional)
# QML import name used to import on qml documents
QML_IMPORT_NAME = "io.qt.mathops"

#@QmlElement
#class MathBridge(QObject): # use slots and signals
    #@Slot(str, result=str)
    #def getColor(self, s):
    
if __name__ == "__main__":
    app = QGuiApplication(sys.argv) # initialize main app loop with sent args
    engine = QQmlApplicationEngine()
    # Add the current directory to the import paths and load the main module.
    engine.addImportPath(sys.path[0])
    engine.loadFromModule("Modules", "Main")
    
    if not engine.rootObjects():
        sys.exit(-1)

    exit_code = app.exec()
    del engine
    sys.exit(exit_code)

    