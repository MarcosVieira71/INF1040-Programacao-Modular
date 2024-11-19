from modulos.musica import escreveJsonMusicas
from modulos.avaliacoes import escreveJsonAvaliacoes, exportarAvaliacoes

from view.Player import Player
from view.assets.ui.TelaPrincipal_ui import Ui_MainWindow
from view.DialogoExportar import DialogoExportar

from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox


class TelaPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()        
        self.player = Player(self)
        self.setupUi(self)
        self.player.setSlider()
        self.setWindowTitle("Music Player")
        self.resize(800, 600)
        
        self.acaoExportarAvaliacoes = self.menuExportar.addAction("Exportar Avaliações")
        self.acaoExportarAvaliacoes.triggered.connect(self.abrirDialogo)
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

    def abrirDialogo(self):
        dialogo = DialogoExportar(self)
        if dialogo.exec() == QDialog.Accepted:
            tipoCodificacao = dialogo.getCodificacao()
            resultadoExportar = exportarAvaliacoes(tipoCodificacao)
            QMessageBox.information(self, "Aviso", resultadoExportar["mensagem"])
            