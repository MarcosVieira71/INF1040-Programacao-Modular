from TelaHome import TelaHome
from TelaMusicas import TelaMusicas

from PySide6.QtWidgets import QMainWindow, QStackedWidget


class TelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        self.resize(800, 600)

        self.stackedWidget = QStackedWidget(self)
        self.setCentralWidget(self.stackedWidget)

        # Adicionando telas
        self.tela_principal = TelaHome(self.navegaPara)
        self.tela_musicas = TelaMusicas(self.navegaPara)

        self.stackedWidget.addWidget(self.tela_principal)
        self.stackedWidget.addWidget(self.tela_musicas)

    def navegaPara(self, index):
        self.stackedWidget.setCurrentIndex(index)
