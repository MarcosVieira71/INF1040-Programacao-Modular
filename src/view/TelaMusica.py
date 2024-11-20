import re

from modulos.musica import adicionarMusica, excluirMusica, encontrarMusica, obtemMusicas
from modulos.avaliacoes import criarAvaliacao, geraStringAvaliacao, excluirAvaliacao
from view.DialogoAvaliacoes import DialogoAvaliacoes
from view.MenuContextoMusicas import MenuContextoMusicas
from view.PerguntaAtualizarAvaliacao import PerguntaAtualizarAvaliacao

from PySide6.QtWidgets import QListView, QWidget, QVBoxLayout, QFileDialog, QDialog, QMessageBox, QPlainTextEdit
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import Qt, QPoint, QUrl

class TelaMusica(QWidget):
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
        contextMenu = MenuContextoMusicas(self)
        index = self.listView.indexAt(position)
        if index.isValid():
            autor, musica = self.extraiNomesDoModel(index)
            contextMenu.opcaoIndexValido(autor, musica, index)

        else:
            contextMenu.opcaoIndexInvalido()

        contextMenu.exec(self.listView.mapToGlobal(position))

    def acaoTocarMusica(self, index):
        autor, nomeMusica = self.extraiNomesDoModel(index)
        resultadoBusca = encontrarMusica(autor, nomeMusica)
        if resultadoBusca["codigo_retorno"]:
            musica = resultadoBusca["musica"]
            self.player.tocaMusica(musica["caminho"])

    def acaoDeletarMusica(self, index):
        autor, nomeMusica = self.extraiNomesDoModel(index)
        resultadoExclusao = excluirMusica(autor, nomeMusica)
        if resultadoExclusao["codigo_retorno"] == 1:
            self.model.removeRow(index.row())
        QMessageBox.information(self, "Aviso", resultadoExclusao["mensagem"])

    def acaoAdicionarMusica(self):
        arquivoNome, _ = QFileDialog.getOpenFileName(self, "Selecionar Arquivo", "", "Arquivos .mp3 (*.mp3)")
        resultadoAdicao = adicionarMusica(arquivoNome)
        if resultadoAdicao["codigo_retorno"]:
            metadadosMusica = resultadoAdicao["metadados_extraidos"]
            self.adicionaItemModel(metadadosMusica=metadadosMusica)
        QMessageBox.information(self, "Aviso", resultadoAdicao["mensagem"])
    
    def adicionaItemModel(self, metadadosMusica):
        nomeMusica, nomeAutor = metadadosMusica["nome"], metadadosMusica["autor"]
        item = QStandardItem(f"Música: {nomeMusica} | Autor: {nomeAutor}")
        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
        self.model.appendRow(item)

    def extraiNomesDoModel(self, index):        
        item_texto = self.model.itemFromIndex(index).text()
        padrao = r"Música: (.+?) \| Autor: (.+)"
        resultado = re.search(padrao, item_texto)
        nomeMusica = resultado.group(1).strip()
        autor = resultado.group(2).strip()
        return autor, nomeMusica
  
    def preencheModel(self):
        resultadoObterMusicas = obtemMusicas()
        if resultadoObterMusicas["codigo_retorno"]:
            musicas = resultadoObterMusicas["musicas"]  
            for musica in musicas:
                self.adicionaItemModel(musica)
    
    def abreDialogoAvaliacao(self, index):
        dialog = DialogoAvaliacoes(self)
        if dialog.exec() == QDialog.Accepted:
            avaliacaoTexto, nota = dialog.pegaInputAvaliacao()
            nomeAutor, nomeMusica = self.extraiNomesDoModel(index)
            retornoCriacao = criarAvaliacao(nomeAutor=nomeAutor, nomeMusica=nomeMusica, nota=nota, texto=avaliacaoTexto)
            if retornoCriacao["codigo_retorno"] == -1:
                PerguntaAtualizarAvaliacao(self, nomeAutor, nomeMusica, nota, avaliacaoTexto)
            else:
                QMessageBox.information(self, "Aviso", retornoCriacao["mensagem"])
       
    def acaoDeletarAvaliacao(self, index):
        autor, musica = self.extraiNomesDoModel(index)
        retornoExclusaoAvaliacao = excluirAvaliacao(autor, musica)
        QMessageBox.information(self, "Aviso", retornoExclusaoAvaliacao["mensagem"])

    def acaoLerAvaliacao(self, index):
        autor, musica = self.extraiNomesDoModel(index)
        resultado = geraStringAvaliacao(autor, musica)
        if resultado["codigo_retorno"]:
            dialog = QDialog(self)
            dialog.setWindowTitle("Avaliação")
            layout = QVBoxLayout(dialog)        
            text_edit = QPlainTextEdit(dialog)
            text_edit.setPlainText(resultado["stringAvaliacao"])
            text_edit.setReadOnly(True) 
            layout.addWidget(text_edit)
            dialog.setLayout(layout)
            dialog.exec()
        else: QMessageBox.warning(self, "Aviso!", resultado["mensagem"])