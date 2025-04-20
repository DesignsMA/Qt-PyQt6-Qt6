from __future__ import annotations

import sys

from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement
from PySide6.QtQuickControls2 import QQuickStyle
# generating resource file
# pyside6-rcc style.qrc -o rc_style.py
import rc_style  # noqa F401
