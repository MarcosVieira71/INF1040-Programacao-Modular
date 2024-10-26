from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
class TelaMusicas(QWidget):
    def __init__(self, navigateCallback):
        super().__init__()
        layout = QVBoxLayout()
        self.navigateCallback = navigateCallback
        layout.addWidget(QLabel("Aqui estarão as músicas."))
        self.setLayout(layout)

        btn_voltar = QPushButton("Voltar para Tela Principal", self)
        btn_voltar.clicked.connect(self.voltarParaPrincipal)
        
        layout.addWidget(btn_voltar)
        self.setLayout(layout)

    def voltarParaPrincipal(self):
        self.navigateCallback(0)  # Muda para a tela principal

