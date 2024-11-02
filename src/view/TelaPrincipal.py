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

        
        self.homeButton.clicked.connect(self.navegaParaHome)
        self.musicasButton.clicked.connect(self.navegaParaMusica)
        self.playlistButton.clicked.connect(self.navegaParaPlaylist)
        self.avaliacoesButton.clicked.connect(self.navegaParaAvaliacoes)
        self.show()

    def navegaParaHome(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def navegaParaMusica(self):
        self.stackedWidget.setCurrentIndex(1)
        self.musica.show()

    def navegaParaAvaliacoes(self):
        self.stackedWidget.setCurrentIndex(3)
    
    
    def navegaParaPlaylist(self):
        self.stackedWidget.setCurrentIndex(2)
    