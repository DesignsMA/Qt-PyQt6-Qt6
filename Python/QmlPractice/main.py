# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
from __future__ import annotations

import sys
from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement
from PySide6.QtQuickControls2 import QQuickStyle
# generating resource file
# pyside6-rcc style.qrc -o rc_style.py
import rc_style  # noqa F401

# To be used on the @QmlElement decorator
# (QML_IMPORT_MINOR_VERSION is optional)
# QML import name used to import on qml documents
QML_IMPORT_NAME = "io.qt.textproperties"
QML_IMPORT_MAJOR_VERSION = 1

# Signals and slots
# Common toolkits used in the creation of user interfaces use
# Callbacks, a callback is a pointer to a function, there is a processing function
# that calls the callback (another function) when appropiate (event)
# However, qt uses an alternative to the callback technique
# A signal is emmited when an object changes its internal state in a way that is
# interesting to the object's client or owner,
# When a signal is emmited the slots connected to it are called in order of connection
# Slots are common python  or c++ functions that have the particularity of being 
# connected to signal

@QmlElement # Exposes class to be used in QML
class Bridge(QObject): # Inherits from QObject to use its signals and slots system
    
#Slot() decorator is used to explicitly mark a Python method as a Qt slot
#@Slot(str, result=str) 
#@Slot(str)
#Declares that the slot accepts a string argument (the signal must emit a str).
#result=str
#Specifies that the slot returns a string (useful when connecting to signals that expect a return value).


    @Slot(str, result=str)
    def getColor(self, s):
        if s.lower() == "red":
            return "#ef9a9a"
        if s.lower() == "green":
            return "#a5d6a7"
        if s.lower() == "blue":
            return "#90caf9"
        return "white"

    @Slot(float, result=int)
    def getSize(self, s):
        size = int(s * 34)
        return max(1, size)

    @Slot(str, result=bool)
    def getItalic(self, s):
        return s.lower() == "italic"

    @Slot(str, result=bool)
    def getBold(self, s):
        return s.lower() == "bold"

    @Slot(str, result=bool)
    def getUnderline(self, s):
        return s.lower() == "underline"


if __name__ == '__main__':
    #QGuiApplication contains the main event loop, where all events 
    # from the window system and other sources are processed and dispatched.
    # It also handles the application’s initialization and finalization, 
    # provides session management. In addition, QGuiApplication handles 
    # most of the system-wide and application-wide settings.
    app = QGuiApplication(sys.argv) # initializing main application, 
    
    QQuickStyle.setStyle("Material")
    engine = QQmlApplicationEngine() 
    # Add the current directory to the import paths and load the main module.
    engine.addImportPath(sys.path[0])
    engine.loadFromModule("QmlIntegration", "Main")

    if not engine.rootObjects():
        sys.exit(-1)

    exit_code = app.exec()
    del engine
    sys.exit(exit_code)
