from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl

class Player(QMediaPlayer):
    def __init__(self, telaPrincipal):
        super().__init__(parent=telaPrincipal)
        self.audio_output = QAudioOutput(self.parent())
        self.setAudioOutput(self.audio_output)
        self.mediaStatusChanged.connect(self.statusPlayer)


    def setSlider(self):
        self.slider = self.parent().horizontalSlider
        self.playButton = self.parent().playButton
        self.positionChanged.connect(self.updateSlider)
        self.durationChanged.connect(self.setRangeSlider)
        self.playButton.clicked.connect(self.togglePlayPause)
        self.slider.sliderMoved.connect(self.setPosicao)

        self.volumeSlider = self.parent().volumeSlider  # Referência ao slider vertical
        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.setValue(self.audio_output.volume() * 100)  # Inicializa com o volume atual
        self.volumeSlider.valueChanged.connect(self.setVolume)

    def tocaMusica(self, filepath):
        self.setSource(QUrl.fromLocalFile(filepath))
        self.play()

    def setVolume(self, value):

        self.audio_output.setVolume(value / 100)  # Converte para valor entre 0.0 e 1.0


    def updateSlider(self, position):
        self.slider.setValue(position)

    def setRangeSlider(self, duration):
        self.slider.setRange(0, duration)

    def setPosicao(self, position):
        self.setPosition(position)

    def statusPlayer(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.setPosition(0)
            self.slider.setValue(0)
        
    def togglePlayPause(self):
        if self.playbackState() == QMediaPlayer.PlayingState:
            self.pause()
            self.playButton.setText("Retomar")
        else:
            self.play()
            self.playButton.setText("Pausar")