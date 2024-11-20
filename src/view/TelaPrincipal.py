from modulos.musica import escreveJsonMusicas
from modulos.avaliacoes import escreveJsonAvaliacoes, exportarAvaliacoes
from modulos.playlist import escreveJsonPlaylists

from view.Player import Player
from view.assets.ui.TelaPrincipal_ui import Ui_MainWindow
from view.DialogoExportar import DialogoExportar

from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox, QSlider
from PySide6.QtCore import Qt


class TelaPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()        
        self.player = Player(self)
        self.setupUi(self)
        self.setSliderVertical()
        self.player.setSlider()
        self.setWindowTitle("Music Player")
        self.resize(800, 600)
    
        self.acaoExportarAvaliacoes = self.menuExportar.addAction("Exportar Avaliações")
        self.acaoExportarAvaliacoes.triggered.connect(self.abrirDialogo)
        self.musicasButton.clicked.connect(self.navegaParaMusica)
        self.playlistButton.clicked.connect(self.navegaParaPlaylist)
        self.show()

    def setSliderVertical(self):
        self.volumeSlider = QSlider(Qt.Vertical, self)  # Cria o slider
        self.volumeSlider.setGeometry(700, 100, 30, 200)  # Define a posição e tamanho do slider
        self.volumeSlider.setRange(0, 100)  # Define o intervalo do slider
        self.volumeSlider.setValue(50)  # Define o valor inicial como 50 (50% do volume)
        self.volumeSlider.setToolTip("Volume")  # Tooltip para o slider
        self.player.volumeSlider = self.volumeSlider  # Passa a referência ao player
        self.volumeSlider.valueChanged.connect(self.player.setVolume)  # Conecta ao método do player



    def navegaParaMusica(self):
        self.stackedWidget.setCurrentIndex(0)
        self.musica.show()

    def navegaParaPlaylist(self):
        self.stackedWidget.setCurrentIndex(1)

    def closeEvent(self, event):
        print("Avaliacoes:", escreveJsonAvaliacoes("app")["mensagem"])
        print("Musicas:", escreveJsonMusicas("app")["mensagem"])
        print("Playlist", escreveJsonPlaylists("app")["mensagem"])
        super().closeEvent(event)

    def abrirDialogo(self):
        dialogo = DialogoExportar(self)
        if dialogo.exec() == QDialog.Accepted:
            tipoCodificacao = dialogo.getCodificacao()
            resultadoExportar = exportarAvaliacoes(tipoCodificacao)
            QMessageBox.information(self, "Aviso", resultadoExportar["mensagem"])
            