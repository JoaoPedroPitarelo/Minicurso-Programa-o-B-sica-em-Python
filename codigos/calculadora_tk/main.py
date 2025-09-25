from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFrame
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
import sys

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora Simples")
        self.setGeometry(250, 250, 300, 250)

        # Layout principal
        layout = QVBoxLayout()
        layout.setContentsMargins(22, 22, 22, 22)

        # Titulo do nosso programa
        titulo = QLabel("Calculadora")
        titulo.setFont(QFont("Ubuntu Mono", 16, weight=300))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titulo)
        
        layout.addSpacing(23)

        # Entradas
        self.label1 = QLabel("Número 1:")
        self.label1.setFont(QFont("Ubuntu Mono", 11, weight=200))
        layout.addWidget(self.label1)
        
        self.entry1 = QLineEdit()
        layout.addWidget(self.entry1)

        self.label2 = QLabel("Número 2:")
        self.label2.setFont(QFont("Ubuntu Mono", 11, weight=200))
        layout.addWidget(self.label2)
        
        self.entry2 = QLineEdit()
        layout.addWidget(self.entry2)

        layout.addSpacing(20)

        # Botões
        self.btn_somar = QPushButton(" + ")
        self.btn_somar.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; font-size: 20px")
        self.btn_somar.clicked.connect(self.somar)
        layout.addWidget(self.btn_somar)

        self.btn_subtrair = QPushButton(" - ")
        self.btn_subtrair.setStyleSheet("background-color: #F54927; color: white; font-weight: bold; font-size: 20px")
        self.btn_subtrair.clicked.connect(self.subtrair)
        layout.addWidget(self.btn_subtrair)

        layout.addSpacing(10)

        divisor = QFrame()
        divisor.setFrameShape(QFrame.HLine)   # Linha horizontal
        divisor.setFrameShadow(QFrame.Sunken) # Estilo "afundado"
        layout.addWidget(divisor)

        layout.addSpacing(10)

        # Resultado
        self.resultado = QLabel("Resultado = ")
        self.setFont(QFont("Ubuntu Mono", 12, weight=200))
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def somar(self):
        try:
            num1 = float(self.entry1.text())
            num2 = float(self.entry2.text())
            self.resultado.setText(f"Resultado: {num1 + num2}")
        except ValueError:
            self.resultado.setText("Erro: insira números válidos")

    def subtrair(self):
        try:
            num1 = float(self.entry1.text())
            num2 = float(self.entry2.text())
            self.resultado.setText(f"Resultado: {num1 - num2}")
        except ValueError:
            self.resultado.setText("Erro: insira números válidos")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Calculadora()
    janela.show()
    sys.exit(app.exec())
