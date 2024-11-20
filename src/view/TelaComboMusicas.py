from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QMessageBox
from PySide6.QtCore import Qt

from modulos.musica import obtemMusicas
from modulos.playlist import adicionarMusicaNaPlaylist


class TelaComboMusicas(QWidget):
    def __init__(self, nomePlaylist):
        super().__init__()
        self.setWindowTitle(f"Adicionar Músicas à Playlist: {nomePlaylist}")
        self.nomePlaylist = nomePlaylist

        # Configuração inicial da janela
        self.setMinimumSize(400, 200)
        self.setWindowModality(Qt.ApplicationModal)

        # Layout principal
        self.mainLayout = QVBoxLayout(self)

        # Rótulo
        self.label = QLabel("Selecione uma música para adicionar:", self)
        self.mainLayout.addWidget(self.label)

        # ComboBox para exibir as músicas
        self.comboBoxMusicas = QComboBox(self)
        self.mainLayout.addWidget(self.comboBoxMusicas)

        # Botão para confirmar a adição
        self.botaoAdicionar = QPushButton("Adicionar à Playlist", self)
        self.botaoAdicionar.clicked.connect(self.adicionarMusica)
        self.mainLayout.addWidget(self.botaoAdicionar)

        # Preencher o ComboBox com as músicas
        self.preencheComboBox()

        # Configurar layout
        self.setLayout(self.mainLayout)

    def preencheComboBox(self):
 
        resultadoObterMusicas = obtemMusicas()
        if resultadoObterMusicas["codigo_retorno"]:
            musicas = resultadoObterMusicas["musicas"]
            for musica in musicas:
                nomeMusica = musica["nome"]
                nomeAutor = musica["autor"]

                textoComboBox = f"{nomeAutor} - {nomeMusica}"
                self.comboBoxMusicas.addItem(textoComboBox, userData={"musica": nomeMusica, "autor": nomeAutor})
        else:
            QMessageBox.warning(self, "Aviso!", "Não foi possível carregar as músicas.")

    def adicionarMusica(self):
        
        indexSelecionado = self.comboBoxMusicas.currentIndex()
        if indexSelecionado == -1:
            QMessageBox.warning(self, "Aviso!", "Nenhuma música foi selecionada.")
            return

        dadosMusica = self.comboBoxMusicas.itemData(indexSelecionado)
        nomeMusica = dadosMusica["musica"]
        nomeAutor = dadosMusica["autor"]

        resultadoAdicionar = adicionarMusicaNaPlaylist(self.nomePlaylist, nomeAutor, nomeMusica)
        QMessageBox.information(self, "Resultado", resultadoAdicionar["mensagem"])
