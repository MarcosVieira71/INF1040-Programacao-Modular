import pygame
from PySide6.QtCore import QTimer

class Player:
    def __init__(self, telaPrincipal):
        pygame.mixer.init()
        self.telaPrincipal = telaPrincipal
        self.is_playing = False
        self.is_paused = False

        self.slider_being_moved = False

        self.timer = QTimer(self.telaPrincipal)
        self.timer.timeout.connect(self.updateSlider)
        self.timer.start(100)  
        self.song_duration = 0  
        self.current_pos = 0  

    def setSlider(self):
        self.slider = self.telaPrincipal.horizontalSlider
        self.playButton = self.telaPrincipal.playButton
        self.volumeSlider = self.telaPrincipal.volumeSlider
        self.playButton.clicked.connect(self.togglePlayPause)
        self.slider.sliderMoved.connect(self.setPosicao) 
        self.volumeSlider.valueChanged.connect(self.setVolume)
        self.slider.setEnabled(False)
        self.volumeSlider.setValue(50)  
        pygame.mixer.music.set_volume(0.5)  

    def tocaMusica(self, filepath):
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()
        self.is_playing = True
        
        self.song_duration = pygame.mixer.Sound(filepath).get_length()  
        self.slider.setRange(0, int(self.song_duration))  

    def togglePlayPause(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.playButton.setText("Retomar")
        else:
            pygame.mixer.music.unpause()
            self.playButton.setText("Pausar")
        self.is_playing = not self.is_playing

    def setVolume(self, value):
        volume = value / 100.0 
        pygame.mixer.music.set_volume(volume)

    def updateSlider(self):
        if not self.slider_being_moved:
            self.current_pos = pygame.mixer.music.get_pos() / 1000 
            self.slider.setValue(int(self.current_pos))

    def setPosicao(self, value):
        self.slider_being_moved = True
        pygame.mixer.music.set_pos(value)
        self.current_pos = value
        self.slider_being_moved = False
