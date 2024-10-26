from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout


class TelaHome(QWidget):
    def __init__(self, navigateCallback):
        super().__init__()
        self.navigateCallback = navigateCallback
        
        layout = QVBoxLayout()
        btn_musicas = QPushButton("Ir para Músicas", self)
        btn_musicas.clicked.connect(self.mudaParaMusicas)
        
        layout.addWidget(btn_musicas)
        self.setLayout(layout)

    def mudaParaMusicas(self):
        self.navigateCallback(1)  # Muda para a tela de Músicas

