import re

from PySide6.QtWidgets import QListView, QWidget, QVBoxLayout, QDialog, QMessageBox, QInputDialog, QFileDialog
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import Qt, QPoint

from modulos.playlist import criarPlaylist, mudaNomePlaylist, excluirPlaylist, obterNomesPlaylists, dicionarioPlaylists
from view.MenuContextoPlaylist import MenuContextoPlaylist
from view.TelaComboMusicas import TelaComboMusicas

class TelaPlaylist(QWidget):
    def __init__(self, player):
        super().__init__()
        self.mainLayout = QVBoxLayout(self)
        self.player = player
        self.listView = QListView(self)
        self.model = QStandardItemModel(self.listView)
        self.listView.setModel(self.model)
        self.mainLayout.addWidget(self.listView)

        self.listView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listView.customContextMenuRequested.connect(self.showContextMenu)
        self.preencheModel()

    def showContextMenu(self, position: QPoint):
        index = self.listView.indexAt(position)
        menu = MenuContextoPlaylist(self)
        if index.isValid():
            menu.opcaoIndexValido(index)
        else:
            menu.opcaoIndexInvalido()
        print(dicionarioPlaylists)
        menu.exec(self.listView.mapToGlobal(position))

    def preencheModel(self):
        resultadoObterPlaylists = obterNomesPlaylists()
        if resultadoObterPlaylists["codigo_retorno"]:
            playlists = resultadoObterPlaylists["nomes"]
            for playlist in playlists:
                self.adicionaItemModel(playlist)

    def adicionaItemModel(self, playlist):
        item = QStandardItem(f"Playlist: {playlist}")
        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
        self.model.appendRow(item)

    def extraiNomeDoModel(self, index):
        item_texto = self.model.itemFromIndex(index).text()
        padrao = r"Playlist: (.+)"
        resultado = re.search(padrao, item_texto)
        return resultado.group(1).strip()

    def acaoCriarPlaylist(self):
        nomeNovaPlaylist, ok = QInputDialog.getText(self, "Criar Nova Playlist", "Digite o nome da nova playlist:")
        if ok and nomeNovaPlaylist:
            resultadoCriar = criarPlaylist(nomeNovaPlaylist)
            if resultadoCriar["codigo_retorno"]:
                self.adicionaItemModel(f"{nomeNovaPlaylist}")
            QMessageBox.information(self, "Aviso", resultadoCriar["mensagem"])

    def acaoAtualizarNome(self, index):
        nomeAtual = self.extraiNomeDoModel(index)
        novoNome, ok = QInputDialog.getText(self, "Atualizar Nome", "Digite o novo nome da playlist:", text=nomeAtual)
        if ok and novoNome:
            resultadoAtualizar = mudaNomePlaylist(nomeAtual, novoNome)
            if resultadoAtualizar["codigo_retorno"]:
                self.model.itemFromIndex(index).setText(f"Playlist: {novoNome}")
            QMessageBox.information(self, "Aviso", resultadoAtualizar["mensagem"])

    def acaoExcluirPlaylist(self, index):
        nomePlaylist = self.extraiNomeDoModel(index)
        resultadoExcluir = excluirPlaylist(nomePlaylist)
        if resultadoExcluir["codigo_retorno"]:
            self.model.removeRow(index.row())
        QMessageBox.information(self, "Aviso", resultadoExcluir["mensagem"])

    def acaoVisualizarPlaylist(self, nomePlaylist):
        dialog = QDialog(self)
        dialog.setWindowTitle(f"Playlist: {nomePlaylist}")
        layout = QVBoxLayout(dialog)
        for musica in :
            layout.addWidget(QLabel(f"{musica['nome']} - {musica['autor']}"))
        dialog.setLayout(layout)
        dialog.exec()


    def acaoAdicionarMusicaPlaylist(self, index):
        if hasattr(self,"telaAdicao"): self.telaAdicao.close()
        nomePlaylist = self.extraiNomeDoModel(index)
        self.telaAdicao = TelaComboMusicas(nomePlaylist)
        self.telaAdicao.show()