from assets.telaPrincipal_ui import Ui_MainWindow

from PySide6.QtWidgets import QMainWindow


class TelaPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Music Player")
        self.resize(800, 600)