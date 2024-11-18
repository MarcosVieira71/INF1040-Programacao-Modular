from modulos.avaliacoes import leJsonAvaliacoes
from modulos.musica import leJsonMusicas

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
    sys.exit(app.exec())
