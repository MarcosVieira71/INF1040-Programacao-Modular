import re

from modulos.musica import adicionarMusica, excluirMusica, encontrarMusica, dicionarioMusicas


from PySide6.QtWidgets import QListView, QMenu, QWidget, QVBoxLayout, QFileDialog
from PySide6.QtGui import QStandardItem, QStandardItemModel, QAction
from PySide6.QtCore import Qt, QPoint, QUrl
from PySide6.QtCore import Qt, QPoint

class TelaMusica(QWidget):
    def __init__(self, player):
        super().__init__()
        # Criação do layout principal
        self.mainLayout = QVBoxLayout(self) 

        self.player = player
        self.listView = QListView(self)
        self.model = QStandardItemModel(self.listView)

        self.listView.setModel(self.model)

        self.mainLayout.addWidget(self.listView)

        self.listView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listView.customContextMenuRequested.connect(self.showContextMenu)

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
            addAction.triggered.connect(self.abreNavegacaoArquivos)

            # Adicionando ações ao menu de contexto geral
            contextMenu.addAction(addAction)

        contextMenu.exec(self.listView.mapToGlobal(position))

    def playMusic(self, index):
        item = self.model.itemFromIndex(index)
        item_texto = item.text()
        
        padrao = r"Música: (.+?) - Autor: (.+?) -"
        resultado = re.search(padrao, item_texto)
        
        if resultado:
            nome_musica = resultado.group(1).strip()
            autor = resultado.group(2).strip()
            resultadoBusca = encontrarMusica(autor, nome_musica)
            print(resultadoBusca)
            if resultadoBusca["codigo_retorno"]:
                musica = resultadoBusca["musica"]
                self.player.setSource(QUrl.fromLocalFile(musica["caminho"]))
                self.player.play()
                print(f"Tocando: {nome_musica} - {autor}")
            print(resultadoBusca["mensagem"])

    def deleteMusic(self, index):
        item_texto = self.model.itemFromIndex(index).text()
        padrao = r"Música: (.+?) - Autor: (.+?) -"
        resultado = re.search(padrao, item_texto)
        
        if resultado:
            nome_musica = resultado.group(1).strip()
            autor = resultado.group(2).strip()
            
            #print(nome_musica, autor)
            
            resultado_exclusao = excluirMusica(autor, nome_musica)
            if resultado_exclusao["codigo_retorno"] == 1:
                self.model.removeRow(index.row())
            print(resultado_exclusao["mensagem"])
        else:
            print("Erro ao extrair o autor e o nome da música do item selecionado.")

    def abreNavegacaoArquivos(self):
        arquivoNome, _ = QFileDialog.getOpenFileName(self, "Selecionar Arquivo", "", "Arquivos .mp3 (*.mp3)")
        resultadoAdicao = adicionarMusica(arquivoNome)
        if resultadoAdicao["codigo_retorno"]:
            metadadosMusica = resultadoAdicao["metadados_extraidos"]
            item = QStandardItem(f"Música: {metadadosMusica['nome']} - Autor: {metadadosMusica['autor']} - Duração: {metadadosMusica['duracao']} segundos")
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.model.appendRow(item)
            print("Nova música adicionada ao modelo")
        else:
            print(resultadoAdicao["mensagem"])