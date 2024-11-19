from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton

class DialogoExportar(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Confirmação")

        # Layout principal
        layout = QVBoxLayout(self)

        # Mensagem
        label = QLabel("Deseja gerar um relatório das avaliações salvas?")
        layout.addWidget(label)

        # ComboBox para selecionar a codificação
        self.comboBox = QComboBox(self)
        self.comboBox.addItems(["UTF-8", "UTF-32"])
        layout.addWidget(self.comboBox)

        # Botões de confirmação
        self.botaoConfirmar = QPushButton("Confirmar", self)
        self.botaoCancelar = QPushButton("Cancelar", self)

        self.botaoConfirmar.clicked.connect(self.accept)
        self.botaoCancelar.clicked.connect(self.reject)

        layout.addWidget(self.botaoConfirmar)
        layout.addWidget(self.botaoCancelar)

    def getCodificacao(self):
        return self.comboBox.currentText()