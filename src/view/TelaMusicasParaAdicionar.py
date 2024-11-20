from PySide6.QtWidgets import QListView, QWidget, QVBoxLayout, QMessageBox
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import Qt

from modulos.musica import obtemMusicas
from modulos.playlist import adicionarMusicaNaPlaylist

import re

class TelaMusicasParaAdicionar(QWidget):
    def __init__(self, nomePlaylist, telaPlaylist):
        super().__init__(parent=telaPlaylist)
        self.setWindowTitle("Adicionar Músicas na Playlist")
        self.nomePlaylist = nomePlaylist  # Nome da playlist onde a música será adicionada
        self.mainLayout = QVBoxLayout(self)

        self.listView = QListView(self)
        self.model = QStandardItemModel(self.listView)
        self.listView.setModel(self.model)
        self.mainLayout.addWidget(self.listView)

        self.listView.doubleClicked.connect(self.acaoAdicionarMusica)

        self.preencheModel()
        self.show()

    def preencheModel(self):
        resultadoObterMusicas = obtemMusicas()
        if resultadoObterMusicas["codigo_retorno"]:
            musicas = resultadoObterMusicas["musicas"]
            for musica in musicas:
                self.adicionaItemModel(musica)
        else:
            QMessageBox.warning(self, "Aviso!", "Não foi possível carregar as músicas.")

    def adicionaItemModel(self, musica):
        item = QStandardItem(f"Música: {musica['nome']} | Autor: {musica['autor']}")
        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
        self.model.appendRow(item)

    def acaoAdicionarMusica(self, index):
        itemTexto = self.model.itemFromIndex(index).text()
        nomeMusica, nomeAutor = self.extraiNomesDoModel(itemTexto)

        resposta = QMessageBox.question(
            self,
            "Adicionar Música",
            f"Deseja adicionar a música '{nomeMusica}' de {nomeAutor} na playlist '{self.nomePlaylist}'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if resposta == QMessageBox.Yes:
            resultadoAdicionar = adicionarMusicaNaPlaylist(self.nomePlaylist, nomeMusica)
            QMessageBox.information(self, "Resultado", resultadoAdicionar["mensagem"])

    def extraiNomesDoModel(self, itemTexto):
        padrao = r"Música: (.+?) \| Autor: (.+)"
        resultado = re.search(padrao, itemTexto)
        nomeMusica = resultado.group(1).strip()
        nomeAutor = resultado.group(2).strip()
        return nomeMusica, nomeAutor
