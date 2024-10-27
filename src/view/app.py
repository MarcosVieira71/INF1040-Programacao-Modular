from view.TelaPrincipal import TelaPrincipal

from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication()
    player = TelaPrincipal()
    player.show()  
    sys.exit(app.exec())
