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

    def tocaMusica(self, filepath):
        self.setSource(QUrl.fromLocalFile(filepath))
        self.play()

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