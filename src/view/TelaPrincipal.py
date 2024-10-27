from assets.TelaPrincipal_ui import Ui_MainWindow
from TelaMusica import TelaMusica

from PySide6.QtWidgets import QMainWindow


class TelaPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Music Player")
        self.resize(800, 600)
        self.homeButton.clicked.connect(self.navegaParaHome)
        self.musicasButton.clicked.connect(self.navegaParaMusica)
        self.playlistButton.clicked.connect(self.navegaParaPlaylist)
        self.avaliacoesButton.clicked.connect(self.navegaParaAvaliacoes)

    def navegaParaHome(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def navegaParaMusica(self):
        self.stackedWidget.setCurrentIndex(1)
        self.musica.show()

    def navegaParaAvaliacoes(self):
        self.stackedWidget.setCurrentIndex(3)
    
    
    def navegaParaPlaylist(self):
        self.stackedWidget.setCurrentIndex(2)
    