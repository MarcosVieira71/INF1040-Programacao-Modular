import re

from modulos.musica import adicionarMusica, excluirMusica, encontrarMusica, leJsonMusicas, obtemMusicas, dicionarioMusicas

from PySide6.QtWidgets import QListView, QMenu, QWidget, QVBoxLayout, QFileDialog
from PySide6.QtGui import QStandardItem, QStandardItemModel, QAction
from PySide6.QtCore import Qt, QPoint, QUrl

class TelaMusica(QWidget):
    def __init__(self, player):
        super().__init__()
        print(leJsonMusicas()["mensagem"])
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
        contextMenu = QMenu(self)

        # Obtendo o índice do item clicado
        index = self.listView.indexAt(position)

        if index.isValid():
            # Criando ações para o menu de contexto do item selecionado
            playAction = QAction("Tocar", self)
            deleteAction = QAction("Excluir", self)
            addToPlaylistAction = QAction("Adicionar a Playlist", self)

            # Conectando ações a métodos
            playAction.triggered.connect(lambda: self.playMusic(index))
            deleteAction.triggered.connect(lambda: self.deleteMusic(index))

            # Adicionando ações ao menu de contexto do item
            contextMenu.addAction(playAction)
            contextMenu.addAction(deleteAction)
            contextMenu.addSeparator()  
            contextMenu.addAction(addToPlaylistAction)
                        
        else:
            # Criando ações para o menu de contexto geral (sem item selecionado)
            addAction = QAction("Adicionar Música", self)

            # Conectando ações a métodos 
            addAction.triggered.connect(self.addMusic)

            # Adicionando ações ao menu de contexto geral
            contextMenu.addAction(addAction)

        contextMenu.exec(self.listView.mapToGlobal(position))

    def playMusic(self, index):
        autor, nomeMusica = self.extraiNomesDoModel(index)
        resultadoBusca = encontrarMusica(autor, nomeMusica)
        if resultadoBusca["codigo_retorno"]:
            musica = resultadoBusca["musica"]
            self.player.setSource(QUrl.fromLocalFile(musica["caminho"]))
            self.player.play()
            print(f"Tocando: {nomeMusica} - {autor}")
        print(resultadoBusca["mensagem"])

    def deleteMusic(self, index):
        autor, nomeMusica = self.extraiNomesDoModel(index)
        resultado_exclusao = excluirMusica(autor, nomeMusica)
        if resultado_exclusao["codigo_retorno"] == 1:
            self.model.removeRow(index.row())
        print(resultado_exclusao["mensagem"])

    def addMusic(self):
        arquivoNome, _ = QFileDialog.getOpenFileName(self, "Selecionar Arquivo", "", "Arquivos .mp3 (*.mp3)")
        resultadoAdicao = adicionarMusica(arquivoNome)
        if resultadoAdicao["codigo_retorno"]:
            metadadosMusica = resultadoAdicao["metadados_extraidos"]
            self.adicionaItemModel(metadadosMusica=metadadosMusica)
        print(resultadoAdicao["mensagem"])
    
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
    
