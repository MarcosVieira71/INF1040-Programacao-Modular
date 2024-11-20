from modulos.avaliacoes import verificaAvaliacao
from PySide6.QtWidgets import QMenu
from PySide6.QtGui import QAction

class MenuContextoMusicas(QMenu):
    def __init__(self, telaMusicas):
        super().__init__(parent=telaMusicas)

    def opcaoIndexInvalido(self):
        addAction = QAction("Adicionar Música", self.parent())
        addAction.triggered.connect(self.parent().acaoAdicionarMusica)
        self.addAction(addAction)

    def opcaoIndexValido(self, autor, musica, index):
        tocarMusica = QAction("Tocar", self.parent())
        deletarMusica = QAction("Excluir", self.parent())
        adicionarAvaliacao = QAction("Adicionar avaliação", self.parent())

        tocarMusica.triggered.connect(lambda: self.parent().acaoTocarMusica(index))
        deletarMusica.triggered.connect(lambda: self.parent().acaoDeletarMusica(index))
        adicionarAvaliacao.triggered.connect(lambda: self.parent().abreDialogoAvaliacao(index))

        self.addAction(tocarMusica)
        self.addAction(deletarMusica)
        self.addSeparator()  
        self.addSeparator()
        self.addAction(adicionarAvaliacao)
        if verificaAvaliacao(autor, musica)["codigo_retorno"]: self.setupAvaliacoesOptions(self, adicionarAvaliacao, index)
        
    def setupAvaliacoesOptions(self,contextMenu, adicionarAvaliacao, index):
        adicionarAvaliacao.setText("Atualizar avaliação")
        deletarAvaliacao = QAction("Excluir avaliação", self.parent())
        deletarAvaliacao.triggered.connect(lambda:self.parent().acaoDeletarAvaliacao(index))

        lerAvaliacao = QAction("Ler avaliação", self.parent())
        lerAvaliacao.triggered.connect(lambda:self.parent().acaoLerAvaliacao(index))
        self.addAction(lerAvaliacao)
        contextMenu.addAction(deletarAvaliacao)