from modulos.avaliacoes import atualizaAvaliacao
from PySide6.QtWidgets import QMessageBox

class PerguntaAtualizarAvaliacao(QMessageBox):
    def __init__(self, telaMusicas, nomeAutor, nomeMusica, nota, avaliacaoTexto):
        super().__init__(parent=telaMusicas)
        self.setIcon(QMessageBox.Question)
        self.setWindowTitle("Aviso")
        self.setText("Deseja atualizar a avaliação existente?")
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setDefaultButton(QMessageBox.No)
        self.updateReviewDialog(nomeAutor, nomeMusica, nota, avaliacaoTexto)

    def updateReviewDialog(self, nomeAutor, nomeMusica, nota, avaliacaoTexto):
        resposta = self.exec()
        if resposta == QMessageBox.Yes:
            retornoAtualizacao = atualizaAvaliacao(nomeAutor=nomeAutor, nomeMusica=nomeMusica,  nota=nota, texto=avaliacaoTexto)
            QMessageBox.information(self, "Aviso", retornoAtualizacao["mensagem"])
        self.close()