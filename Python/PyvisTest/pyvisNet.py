import sys
import random
from pyvis.network import Network
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, QTimer
import os
import tempfile
import io

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

class GraphApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualizador de Grafo con PyVis")
        self.setGeometry(100, 100, 800, 600)

        # Configuración de interfaz
        self.view = QWebEngineView()
        self.button = QPushButton("Añadir nodo aleatorio")
        self.button.clicked.connect(self.add_random_node)

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Inicializar grafo
        self.graph = Network(
            directed=False,
            notebook=False,
            cdn_resources='in_line',
            height="580px",
            width="100%"
        )
        self.graph.toggle_physics(True)
        self.node_count = 0
        
        # Create temporary file with explicit UTF-8 encoding
        self.html_file = tempfile.NamedTemporaryFile(
            mode='w', 
            suffix='.html', 
            encoding='utf-8', 
            delete=False
        )
        self.html_path = self.html_file.name
        self.html_file.close()
        
        # Initial empty graph with forced UTF-8 encoding
        self._save_graph_with_utf8()
        self.view.setUrl(QUrl.fromLocalFile(self.html_path))
        
        # Optimization flags
        self.pending_update = False
        self.update_timer = QTimer()
        self.update_timer.setSingleShot(True)
        self.update_timer.timeout.connect(self._perform_update)

    def add_random_node(self):
        new_node = f"Nodo {self.node_count}"
        self.graph.add_node(new_node, label=new_node)
        if self.node_count > 0:
            target = random.choice(self.graph.nodes)
            self.graph.add_edge(new_node, target["id"])
        self.node_count += 1
        self.schedule_update()

    def schedule_update(self):
        if not self.pending_update:
            self.pending_update = True
            self.update_timer.start(100)  # 100ms delay

    def _perform_update(self):
        if not self.graph.nodes:
            return
            
        try:
            self._save_graph_with_utf8()
            if self.isVisible():
                self.view.reload()
        except Exception as e:
            print(f"Error updating graph: {e}")
        finally:
            self.pending_update = False

    def _save_graph_with_utf8(self):
        """Custom save method that enforces UTF-8 encoding"""
        html = self.graph.generate_html()
        with io.open(self.html_path, 'w', encoding='utf-8') as f:
            f.write(html)

    def closeEvent(self, event):
        try:
            if os.path.exists(self.html_path):
                os.unlink(self.html_path)
        except:
            pass
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphApp()
    window.show()
    sys.exit(app.exec())