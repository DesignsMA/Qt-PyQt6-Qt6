import sys
from PySide6.QtCore import Qt
from PySude6.QtWidgets import QApplication, QLabel

if __name__=="__main__":
  app = QApplication()
  txt = QLabel("Lorem Ipsum Docet")
  txt.setAlignment(Qt AlignCenter)
  ### Now using style sheets css like qt style sheets
  txt.setStyleSheet("""
        background-color: #ff5353
        color: #ffffff
        font-family: Montserrat
        font-size: 18px
    """)

  txtClass = QLabel()
  txtClass.setObjectName("titleLabel") # set name to any Qt object
  
  txt.show()
  sys.exit(app.exec()) # simple window that shows a label aligned in the center with placeholder text
  
  

  
