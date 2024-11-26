import pygame
from PySide6.QtCore import QTimer

class Player:
    def __init__(self, telaPrincipal):
        pygame.mixer.init()
        self.telaPrincipal = telaPrincipal
        self.is_playing = False
        self.is_paused = False

        # Flag para verificar se o slider foi movido pelo usuário
        self.slider_being_moved = False

        # Timer para atualizar o slider
        self.timer = QTimer(self.telaPrincipal)
        self.timer.timeout.connect(self.updateSlider)
        self.timer.start(100)  # Atualiza o slider a cada 100ms

        self.song_duration = 0  # Duração total da música em segundos (a ser configurada)

    def setSlider(self):
        self.slider = self.telaPrincipal.horizontalSlider
        self.playButton = self.telaPrincipal.playButton
        self.volumeSlider = self.telaPrincipal.volumeSlider
        self.playButton.clicked.connect(self.togglePlayPause)
        self.slider.sliderMoved.connect(self.setPosicao)  # Movimentação manual do slider
        self.volumeSlider.valueChanged.connect(self.setVolume)

    def tocaMusica(self, filepath):
        """Carrega e toca a música."""
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()
        self.is_playing = True
        
        # Defina a duração da música
        self.song_duration = pygame.mixer.Sound(filepath).get_length()  # Obtém a duração em segundos
        self.slider.setRange(0, int(self.song_duration))  # Define o intervalo do slider

    def togglePlayPause(self):
        """Alterna entre play e pause."""
        if self.is_playing:
            pygame.mixer.music.pause()
            self.playButton.setText("Retomar")
        else:
            pygame.mixer.music.unpause()
            self.playButton.setText("Pausar")
        self.is_playing = not self.is_playing

    def setVolume(self, value):
        """Ajusta o volume do player de áudio."""
        pygame.mixer.music.set_volume(value / 100)

    def setPosicao(self):
        """Atualiza a posição da música de acordo com a posição do slider."""
        if not self.slider_being_moved:
            # Atualize a música para a posição do slider
            pygame.mixer.music.set_pos(self.slider.value())

    def updateSlider(self):
        """Atualiza a posição do slider enquanto a música está tocando."""
        if not self.slider_being_moved:  # Só atualiza o slider se o usuário não estiver movendo
            current_pos = pygame.mixer.music.get_pos() / 1000  # Posicionamento atual da música (em segundos)
            self.slider.setValue(int(current_pos))

    def sliderMoving(self):
        """Marca que o usuário está movendo o slider."""
        self.slider_being_moved = True

    def sliderReleased(self):
        """Marca que o usuário parou de mover o slider."""
        self.slider_being_moved = False
