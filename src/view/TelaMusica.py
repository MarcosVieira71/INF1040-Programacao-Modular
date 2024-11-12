import re

from modulos.musica import adicionarMusica, excluirMusica, encontrarMusica, leJsonMusicas, obtemMusicas
from modulos.avaliacoes import criarAvaliacao, atualizaAvaliacao, excluirAvaliacao, leJsonAvaliacoes, dicionarioAvaliacoes
from view.DialogoAvaliacoes import DialogoAvaliacoes
from view.MenuContextoMusicas import MenuContexto
from view.PerguntaAtualizarAvaliacao import PerguntaAtualizarAvaliacao

from PySide6.QtWidgets import QListView, QMenu, QWidget, QVBoxLayout, QFileDialog, QDialog, QMessageBox
from PySide6.QtGui import QStandardItem, QStandardItemModel, QAction
from PySide6.QtCore import Qt, QPoint, QUrl

class TelaMusica(QWidget):
    def __init__(self, player):
        super().__init__()
        print(leJsonAvaliacoes()["mensagem"])
        print(leJsonMusicas()["mensagem"])
        print(dicionarioAvaliacoes)
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
        contextMenu = MenuContexto(self)
        index = self.listView.indexAt(position)
        if index.isValid():
            autor, musica = self.extraiNomesDoModel(index)
            contextMenu.opcaoIndexValido(autor, musica, index)

        else:
            contextMenu.opcaoIndexInvalido()

        contextMenu.exec(self.listView.mapToGlobal(position))

    def playMusic(self, index):
        autor, nomeMusica = self.extraiNomesDoModel(index)
        resultadoBusca = encontrarMusica(autor, nomeMusica)
        if resultadoBusca["codigo_retorno"]:
            musica = resultadoBusca["musica"]
            self.player.setSource(QUrl.fromLocalFile(musica["caminho"]))
            print(f"Tocando: {nomeMusica} - {autor}")
        print(resultadoBusca["mensagem"])

    def deleteMusic(self, index):
        autor, nomeMusica = self.extraiNomesDoModel(index)
        resultadoExclusao = excluirMusica(autor, nomeMusica)
        if resultadoExclusao["codigo_retorno"] == 1:
            self.model.removeRow(index.row())
        QMessageBox.information(self, "Aviso", resultadoExclusao["mensagem"])

    def addMusic(self):
        arquivoNome, _ = QFileDialog.getOpenFileName(self, "Selecionar Arquivo", "", "Arquivos .mp3 (*.mp3)")
        resultadoAdicao = adicionarMusica(arquivoNome)
        if resultadoAdicao["codigo_retorno"]:
            metadadosMusica = resultadoAdicao["metadados_extraidos"]
            self.adicionaItemModel(metadadosMusica=metadadosMusica)
        QMessageBox.information(self, "Aviso", resultadoAdicao["mensagem"])
    
    def adicionaItemModel(self, metadadosMusica):
        nomeMusica, nomeAutor, duracao = metadadosMusica["nome"], metadadosMusica["autor"], metadadosMusica["duracao"]
        item = QStandardItem(f"Música: {nomeMusica} - Autor: {nomeAutor} - Duração: {duracao} segundos")
        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
        self.model.appendRow(item)

    def extraiNomesDoModel(self, index):        
        item_texto = self.model.itemFromIndex(index).text()
        padrao = r"Música: (.+?) - Autor: (.+?) -"
        resultado = re.search(padrao, item_texto)
        nomeMusica = resultado.group(1).strip()
        autor = resultado.group(2).strip()
        return autor, nomeMusica

    def preencheModel(self):
        resultadoObterMusicas = obtemMusicas()
        if resultadoObterMusicas["codigo_retorno"]:
            dicionarioMusicas = resultadoObterMusicas["musicas"]  # Acessa o dicionário de músicas
            for musica in dicionarioMusicas.values():
                self.adicionaItemModel(musica)
    
    def openReviewDialog(self, index):
        dialog = DialogoAvaliacoes(self)
        if dialog.exec() == QDialog.Accepted:
            avaliacaoTexto, nota = dialog.getReviewData()
            nomeAutor, nomeMusica = self.extraiNomesDoModel(index)
            retornoCriacao = criarAvaliacao(nomeAutor=nomeAutor, nomeMusica=nomeMusica, nota=nota, texto=avaliacaoTexto)
            if retornoCriacao["codigo_retorno"] == -1:
                PerguntaAtualizarAvaliacao(self, nomeAutor, nomeMusica, nota, avaliacaoTexto)
            else:
                QMessageBox.information(self, "Aviso", retornoCriacao["mensagem"])
       
    def deleteReview(self, index):
        autor, musica = self.extraiNomesDoModel(index)
        retornoExclusaoAvaliacao = excluirAvaliacao(autor, musica)
        QMessageBox.information(self, "Aviso", retornoExclusaoAvaliacao["mensagem"])
