# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'telaPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from view.TelaMusica import TelaMusica

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 0, 98, 515))
        self.widget.setStyleSheet(u"QWidget{background-color: rgb(106, 101, 91)}\n"
"QPushButton{background-color: \"orange\"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")


        self.verticalSpacer = QSpacerItem(20, 120, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.musicasButton = QPushButton(self.widget)
        self.musicasButton.setObjectName(u"musicasButton")

        self.verticalLayout.addWidget(self.musicasButton)

        self.verticalSpacer_2 = QSpacerItem(20, 120, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.playlistButton = QPushButton(self.widget)
        self.playlistButton.setObjectName(u"playlistButton")

        self.verticalLayout.addWidget(self.playlistButton)

        self.verticalSpacer_3 = QSpacerItem(20, 120, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(160, 20, 601, 461))
        self.musica = TelaMusica(MainWindow.player)
        self.musica.setObjectName(u"musica")
        self.stackedWidget.addWidget(self.musica)
        self.playlist = QWidget()
        self.playlist.setObjectName(u"playlist")
        self.stackedWidget.addWidget(self.playlist)
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(280, 490, 481, 51))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.playButton = QPushButton(self.centralwidget)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setGeometry(QRect(180, 490, 71, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuExportar = QMenu(self.menubar)
        self.menuExportar.setObjectName(u"menuExportar")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExportar.menuAction())
        self.menuFile.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.musicasButton.setText(QCoreApplication.translate("MainWindow", u"Musicas", None))
        self.playlistButton.setText(QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"Retomar", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"M\u00fasicas", None))
        self.menuExportar.setTitle(QCoreApplication.translate("MainWindow", u"Exportar", None))
    # retranslateUi

