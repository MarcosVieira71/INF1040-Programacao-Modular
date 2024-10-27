
from PySide6.QtWidgets import QListView, QMenu, QWidget, QVBoxLayout
from PySide6.QtGui import QStandardItem, QStandardItemModel, QAction
from PySide6.QtCore import Qt, QPoint

class TelaMusica(QWidget):
    def __init__(self):
        super().__init__()

        # Criação do layout principal
        self.mainLayout = QVBoxLayout(self) 

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
            addAction.triggered.connect(self.addMusic)

            # Adicionando ações ao menu de contexto geral
            contextMenu.addAction(addAction)

        contextMenu.exec(self.listView.mapToGlobal(position))

    def playMusic(self, index):
        item = self.model.itemFromIndex(index)
        print(f"Tocando: {item.text()}")

    def deleteMusic(self, index):
        self.model.removeRow(index.row())
        print("Música excluída")

    def addMusic(self):
        newItem = QStandardItem(f"Música {self.model.rowCount() + 1} - Autor: Exemplo Autor - Duração: 3:355")
        newItem.setFlags(newItem.flags() & ~Qt.ItemIsEditable)  
        self.model.appendRow(newItem)
        print("Nova música adicionada")


