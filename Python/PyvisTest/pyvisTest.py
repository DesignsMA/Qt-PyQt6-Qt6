import random
import sys
from PySide6.QtWidgets import (QWidget, QPushButton, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QMainWindow)
from PySide6.QtCore import Slot, Qt, QUrl, QTextStream, QFile, QIODevice
from PySide6.QtGui import QFontDatabase, QColor
import res_rc
# WEB
from pyvis.network import Network
import os
import tempfile
import io
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings

os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = (
    "--disable-gpu "          # Matches your hardware-accelerated rasterization
    "--use-angle=d3d11 "                 
    "--enable-webgl "                    
    "--enable-webgl2 "                 
    "--enable-webgpu "                   
    "--enable-accelerated-video-decode "  
    "--enable-accelerated-video-encode "  
    "--num-raster-threads=4 "             
    "--disable-gpu-driver-bug-workarounds" # Avoid problematic workarounds
)

os.environ["QT_OPENGL"] = "hardware"



def load_font_from_resource():
    # Cargar fuente desde recursos
    font_file = QFile(":/fonts/redhat.ttf")
    if not font_file.open(QIODevice.ReadOnly):
        print("Error al abrir el archivo de fuente")
        return False
    
    font_data = font_file.readAll()
    font_file.close()
    
    font_id = QFontDatabase.addApplicationFontFromData(font_data)
    return font_id != -1


class MainWindow(QMainWindow):
    def __init__(self, title: str = ' ', w: int = 600, h: int = 300):
        super().__init__()
        load_font_from_resource()
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowTitle(title)
        self.setMinimumSize(w, h)
        self.showMaximized()
        
        # Create central widget and main layout
        central_widget = QWidget()
        central_widget.setObjectName("Main")
        self.setCentralWidget(central_widget)
    
        
        # Main horizontal layout
        self.main_layout = QHBoxLayout(central_widget)  # Set parent here
        
        # Create menu and net layouts
        self.menu = QWidget()
        self.menu.setLayout(QVBoxLayout())
        self.net = QWidget()
        self.net.setLayout(QHBoxLayout())
        
        # Add layouts to main layout with stretch factors
        self.main_layout.addWidget(self.menu, 1)  # Takes 1 part of space
        self.main_layout.addWidget(self.net, 4)  # Takes 4 parts of space
        
        self.initMenu()
        
        # Load stylesheet
        file = QFile(":/styles/main.css")
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
            file.close()
        else:
            print("Failed to load stylesheet:", file.errorString())
    
    def initMenu(self):
        buttons = [
            ("Editar el árbol", "edit", None),
            ("Cargar el árbol desde archivo", "load", None),
            ("Buscar un elemento", "search", None),
            ("Insertar un elemento", "insert", self.add_random_node),
            ("Eliminar un elemento", "delete", None)
        ]
        
        self.menu.layout().addStretch() # funciona como un resorte, empuja los botones hacia arriba

        for label, btnid, slot in buttons:
            button = QPushButton(label, self.menu)
            button.setObjectName(btnid)
            if slot:
                button.clicked.connect(slot)
            self.menu.layout().addWidget(button)
        
        self.menu.layout().addStretch() # funciona como un resorte, empuja los botones hacia arriba

        # Inicializar grafo
        self.view = QWebEngineView() # visualizador web
        self.view.page().settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        self.view.page().settings().setAttribute(QWebEngineSettings.WebAttribute.ForceDarkMode, True) 
        self.view.page().settings().setAttribute(QWebEngineSettings.WebAttribute.WebGLEnabled, True) 
        self.view.page().settings().setAttribute(QWebEngineSettings.WebAttribute.Accelerated2dCanvasEnabled, True) 

        self.net.layout().addWidget(self.view) # añadir a la zona del grafo
        self.net = Network( # crear red
            directed=False,
            notebook=False,
            cdn_resources='in_line',
            width="100%",
            height="100%",
            bgcolor='#161616',
            neighborhood_highlight=True
        )
        self.net.toggle_physics(True)
        self.node_count = 0
        
        # Cargar HTML inicial
        self.update_net()

    def add_random_node(self):
        new_node = f"Nodo {self.node_count}"
        self.net.add_node(new_node, 
            label=new_node,
            color={
                "background": "#161616",    # Fondo
                "border": "#ff5353",       # Borde
                "highlight": {
                    "background": "#ff2222", # Resaltado
                    "border": "#ff2222"     # Borde resaltado
                },
                "hover": {
                    "background": "#121212", # Hover
                    "border": "#ff5353"     # Borde hover
                }
            },
            borderWidth=2,                 # Grosor del borde
            borderWidthSelected=3,         # Grosor cuando está seleccionado
            font={
                "color": "#ffffff",       # Color texto
                "size": 12           # Tamaño texto
            }
        )
        if self.node_count > 0:
            target = random.choice(self.net.nodes)
            self.net.add_edge(new_node, target["id"])
        self.node_count += 1
        self.update_net()

    def update_net(self):
        if not self.net.nodes:
            return  
        # Generar HTML y cargarlo directamente
        html = self.net.generate_html()
        # Usar baseUrl para que los recursos se carguen correctamente
        base_url = QUrl.fromLocalFile(".")  # Directorio actual como base
        self.view.setHtml(html, base_url)


if __name__ == '__main__':
    
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    window = MainWindow()
    window.show()
    # Run the main Qt loop
    sys.exit(app.exec())