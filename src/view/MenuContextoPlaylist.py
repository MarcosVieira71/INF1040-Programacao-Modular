from PySide6.QtWidgets import QMenu
from PySide6.QtGui import QAction

class MenuContextoPlaylist(QMenu):
    def __init__(self, telaPlaylists):
        super().__init__(parent=telaPlaylists)

    def opcaoIndexInvalido(self):
        addAction = QAction("Criar playlist", self.parent())
        addAction.triggered.connect(self.parent().acaoCriarPlaylist)
        self.addAction(addAction)


    def opcaoIndexValido(self, index):
        deletarPlaylist = QAction("Excluir playlist", self.parent())
        addMusicaToPlaylist = QAction("Adicionar música a playlist", self.parent())
        visualizarPlaylist = QAction("Visualizar playlist", self.parent())
        alterarNomePlaylist = QAction("Alterar nome da playlist", self.parent())

        deletarPlaylist.triggered.connect(lambda: self.parent().acaoExcluirPlaylist(index))
        addMusicaToPlaylist.triggered.connect(lambda: self.parent().acaoAdicionarMusicaPlaylist(index))
        alterarNomePlaylist.triggered.connect(lambda: self.parent().acaoAtualizarNome(index))
        visualizarPlaylist.triggered.connect(lambda:self.parent().acaoVisualizarPlaylist(index))

        self.addAction(deletarPlaylist)
        self.addAction(addMusicaToPlaylist)
        self.addSeparator()  
        self.addAction(visualizarPlaylist)
        self.addSeparator()
        self.addAction(alterarNomePlaylist)