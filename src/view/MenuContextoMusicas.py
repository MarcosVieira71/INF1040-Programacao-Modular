from modulos.avaliacoes import verificaAvaliacao
from PySide6.QtWidgets import QMenu
from PySide6.QtGui import QAction

class MenuContexto(QMenu):
    def __init__(self, telaMusicas):
        super().__init__(parent=telaMusicas)

    def opcaoIndexInvalido(self):
        addAction = QAction("Adicionar Música", self.parent())
        addAction.triggered.connect(self.parent().addMusic)
        self.addAction(addAction)

    def opcaoIndexValido(self, autor, musica, index):
        playAction = QAction("Tocar", self.parent())
        deleteAction = QAction("Excluir", self.parent())
        addToPlaylistAction = QAction("Adicionar a Playlist", self.parent())
        addToReviewsAction = QAction("Adicionar avaliação", self.parent())

        playAction.triggered.connect(lambda: self.parent().playMusic(index))
        deleteAction.triggered.connect(lambda: self.parent().deleteMusic(index))
        addToReviewsAction.triggered.connect(lambda: self.parent().openReviewDialog(index))

        self.addAction(playAction)
        self.addAction(deleteAction)
        self.addSeparator()  
        self.addAction(addToPlaylistAction)
        self.addSeparator()
        self.addAction(addToReviewsAction)
        if verificaAvaliacao(autor, musica)["codigo_retorno"]: self.setupAvaliacoesOptions(self, addToReviewsAction, index)
        
    def setupAvaliacoesOptions(self,contextMenu, addReviewAction, index):
        addReviewAction.setText("Atualizar avaliação")
        deleteReviewAction = QAction("Excluir avaliação", self.parent())
        deleteReviewAction.triggered.connect(lambda:self.parent().deleteReview(index))
        contextMenu.addAction(deleteReviewAction)