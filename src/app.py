from modulos.avaliacoes import leJsonAvaliacoes, escreveJsonAvaliacoes
from modulos.musica import leJsonMusicas, escreveJsonMusicas

from view.TelaPrincipal import TelaPrincipal

from PySide6.QtWidgets import QApplication
import sys

class ProgramaPrincipal(QApplication):
    def __init__(self):
        super().__init__()
        print(leJsonAvaliacoes()["mensagem"])
        print(leJsonMusicas()["mensagem"])
        self.telaPrincipal = TelaPrincipal()

if __name__ == "__main__":
    app = ProgramaPrincipal()
    print(escreveJsonMusicas()["mensagem"])
    print(escreveJsonAvaliacoes()["mensagem"])
    sys.exit(app.exec())