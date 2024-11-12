from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QTextEdit, QSpinBox, QPushButton

class DialogoAvaliacoes(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Criando Avaliação")
        self.resize(400, 300)
        
        layout = QVBoxLayout(self)
        
        labelTitulo = QLabel("Escreva sua avaliação:", self)
        layout.addWidget(labelTitulo)
        
        self.caixaTexto = QTextEdit(self)
        self.caixaTexto.setPlaceholderText("Digite sua review aqui...")
        layout.addWidget(self.caixaTexto)
        
        self.spinBoxAvaliacao = QSpinBox(self)
        self.spinBoxAvaliacao.setRange(0, 5)
        self.spinBoxAvaliacao.setSuffix(" estrelas")
        layout.addWidget(self.spinBoxAvaliacao)
        
        botaoConfirmar = QPushButton("Confirmar", self)
        layout.addWidget(botaoConfirmar)
        
        botaoConfirmar.clicked.connect(self.accept)
    
    def getReviewData(self):
        return self.caixaTexto.toPlainText(), self.spinBoxAvaliacao.value()
