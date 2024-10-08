
from PyQt6.QtWidgets import (
      QApplication, QVBoxLayout, QWidget, QLabel, QPushButton,
      QLineEdit      
)
from PyQt6 import QtCore, QtGui, QtWidgets
from CapturarImagen import CapturarImagen
from EntrenamientoImagen import EntrenamientoImagen
from ProbarImagen import ProbarImagen
from PyQt6.QtCore import Qt,QRect
from PyQt6.QtGui import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 50
        self.top = 50
        self.width = 700
        self.height = 500
        self.setWindowTitle("Reconocimiento Facial")
        self.startUI()

    def startUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Video",self)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label.setObjectName("label")
        self.label.setFixedWidth(500)
        self.label.setFixedHeight(400)

        layout.addWidget(self.label,10,Qt.AlignmentFlag.AlignHCenter)

        self.lblText = QLabel("Ingrese un nombre")
        self.lblText.setAlignment(Qt.AlignmentFlag.AlignJustify)

        layout.addWidget(self.lblText,1)

        self.input = QLineEdit(self)
        self.input.setGeometry(QtCore.QRect(180, 70, 320, 240))

        self.input.move(-300,-250)
        layout.addWidget(self.input)
        
        button = QPushButton("Capturar Imagen")
        button.clicked.connect(self.capturarImagen)
        layout.addWidget(button)

        button = QPushButton("Entrenar Imagen")
        button.clicked.connect(self.entrenarImagen)
        layout.addWidget(button)

        button = QPushButton("Probar Imagen")
        button.clicked.connect(self.probarImagen)
        layout.addWidget(button)

    def capturarImagen(self):
       continuar:bool = False;
       text:str = self.input.text()
       print(text)
       if text.strip() == "":
           self.lblText.setText("Nombre es obligatorio")
       else:
           continuar = True      
           CapturarImagen.capturar(continuar,text,0)
    
    def entrenarImagen(self):
        EntrenamientoImagen.entrenarImagen("imagenes")

    def probarImagen(self):
        ProbarImagen.probarImagen("imagenes",0)   
            
