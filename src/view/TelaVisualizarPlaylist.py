from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QMenu, QMessageBox, QHeaderView, QLabel
from PySide6.QtCore import Qt, QPoint

from modulos.playlist import obtemMusicasDePlaylist, excluirMusicaDaPlaylist
from modulos.musica import encontrarMusica


class TelaVisualizarPlaylist(QWidget):
    def __init__(self, nomePlaylist, player):
        super().__init__()
        self.setWindowTitle(f"Playlist: {nomePlaylist}")
        self.setMinimumSize(600, 400)  # Define o tamanho inicial da janela
        self.nomePlaylist = nomePlaylist
        self.player = player
        self.mainLayout = QVBoxLayout(self)

        # Rótulo para exibir informações gerais da playlist
        self.infoLabel = QLabel(self)
        self.infoLabel.setAlignment(Qt.AlignCenter)
        self.mainLayout.addWidget(self.infoLabel)

        # Configurar a tabela
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Nome da Música", "Autor", "Duração"])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.showContextMenu)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)  # Estende a coluna "Nome da Música"
        header.setSectionResizeMode(1, QHeaderView.Stretch)  # Estende a coluna "Autor"
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)  # Coluna "Duração" ajustada ao conteúdo

        self.mainLayout.addWidget(self.table)
        self.setLayout(self.mainLayout)

        self.preencheTabela()

    def preencheTabela(self):
        resultadoObterMusicas = obtemMusicasDePlaylist(self.nomePlaylist)
        if resultadoObterMusicas["codigo_retorno"]:
            musicas = resultadoObterMusicas["musicas"]
            self.table.setRowCount(len(musicas))

            duracaoTotalSegundos = 0
            for row, musica in enumerate(musicas):
                autor = musica[0]
                nomeMusica = musica[1]
                resultadoEncontrarMusica = encontrarMusica(autor, nomeMusica)
                if resultadoEncontrarMusica["codigo_retorno"]:
                    duracaoSegundos = int(resultadoEncontrarMusica["musica"]["duracao"])

                    minutos = duracaoSegundos // 60
                    segundos = duracaoSegundos % 60
                    duracaoFormatada = f"{minutos:02}:{segundos:02}"

                    self.table.setItem(row, 0, QTableWidgetItem(nomeMusica))  
                    self.table.setItem(row, 1, QTableWidgetItem(autor)) 
                    self.table.setItem(row, 2, QTableWidgetItem(duracaoFormatada))  
                    duracaoTotalSegundos += duracaoSegundos
                else: QMessageBox.warning(self, "Aviso", f"Não foi possível encontrar as informações da música {nomeMusica}")


            totalMinutos = duracaoTotalSegundos // 60
            totalSegundos = duracaoTotalSegundos % 60
            duracaoTotalFormatada = f"{totalMinutos:02}:{totalSegundos:02}"

            self.infoLabel.setText(
                f"Número de músicas: {len(musicas)} | Duração total: {duracaoTotalFormatada}"
            )
        else:
            QMessageBox.warning(self, "Aviso", resultadoObterMusicas["mensagem"])

    def showContextMenu(self, position: QPoint):

        index = self.table.indexAt(position)
        if index.isValid(): 
            row = index.row()
            nomeMusica = self.table.item(row, 0).text()  
            nomeAutor = self.table.item(row, 1).text()  

            menu = QMenu(self)
            tocarAction = menu.addAction("Tocar Música")
            removerAction = menu.addAction("Remover Música da Playlist")

            action = menu.exec(self.table.viewport().mapToGlobal(position))

            if action == tocarAction:
                self.acaoTocarMusica(nomeMusica, nomeAutor)
            elif action == removerAction:
                self.acaoRemoverMusica(nomeMusica, nomeAutor)

    def acaoTocarMusica(self, nomeMusica, nomeAutor):
        resultadoEncontrarMusica = encontrarMusica(nomeAutor, nomeMusica)
        if resultadoEncontrarMusica["codigo_retorno"]:
            musica = resultadoEncontrarMusica["musica"]
            self.player.tocaMusica(musica["caminho"])
        else:
            QMessageBox.warning(self, "Erro", resultadoEncontrarMusica["mensagem"])

    def acaoRemoverMusica(self, nomeMusica, nomeAutor):
        resposta = QMessageBox.question(
            self,
            "Remover Música",
            f"Tem certeza que deseja remover a música '{nomeMusica}' de {nomeAutor} da playlist '{self.nomePlaylist}'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if resposta == QMessageBox.Yes:
            resultado = excluirMusicaDaPlaylist(self.nomePlaylist, nomeAutor, nomeMusica)
            if resultado["codigo_retorno"]:
                QMessageBox.information(self, "Removido", f"A música '{nomeMusica}' foi removida da playlist.")
                self.preencheTabela()  # Atualiza a tabela
            else:
                QMessageBox.warning(self, "Erro", resultado["mensagem"])
