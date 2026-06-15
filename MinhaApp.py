import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class MinhaApp(QWidget):
    def __init__(self):
        super().__init__()

        #Configurações da Janela
        self.setWindowTitle("Minha Primeira App PyQt6")
        self.setGeometry(100, 100, 300, 200)

        #Layout e Widgets
        layout = QVBoxLayout()

        #1. Label para exibir a imagem (iniciando vazio)
        self.label_imagem = QLabel("A imagem aparecerá aqui")
        self.label_imagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_imagem)

        #2. Botão de ação
        self.botao = QPushButton("Mostrar Imagem")
        self.botao.clicked.connect(self.exibir_imagem)
        layout.addWidget(self.botao)

        self.setLayout(layout)

    def exibir_imagem(self):
        #3. Carregar a imagem
        pixmap = QPixmap("botao_on.png")

        # Verificar se a imagem foi carregada corretamente
        if not pixmap.isNull():
            # Redimensionar a imagem para caber no label mantendo proporção
            self.label_imagem.setPixmap(pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))
            self.label_imagem.setText("") # Remove o texto de aviso
        else:
            self.label_imagem.setText("Erro: Imagem não encontrada!")

#Execução
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MinhaApp()
    janela.show()
    sys.exit(app.exec())