from modulos.musica import escreveJsonMusicas
from modulos.avaliacoes import escreveJsonAvaliacoes

from view.assets.ui.TelaPrincipal_ui import Ui_MainWindow
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import QMainWindow


class TelaPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()
        self.setupUi(self, self.player)
        self.setWindowTitle("Music Player")
        self.resize(800, 600)

        self.musicasButton.clicked.connect(self.navegaParaMusica)
        self.playlistButton.clicked.connect(self.navegaParaPlaylist)
        self.show()

    def navegaParaMusica(self):
        self.stackedWidget.setCurrentIndex(0)
        self.musica.show()

    def navegaParaPlaylist(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def closeEvent(self, event):
        print(escreveJsonMusicas()["mensagem"])
        print(escreveJsonAvaliacoes()["mensagem"])
        super().closeEvent(event)