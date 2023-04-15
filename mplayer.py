#Libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QUrl, QDir
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, \
QFrame, QGraphicsDropShadowEffect, QGraphicsView, QGraphicsScene, QLabel, \
QPushButton, QHBoxLayout, QStyle, QListWidget, QFileDialog, QSlider, QVBoxLayout
from PyQt5.QtGui import QGradient, QFont, QColor, QCursor, QIcon, QPixmap
from PyQt5.QtMultimedia import (QMediaPlayer, QMediaContent, QMediaPlaylist, QMediaMetaData)
import sys
from os.path import expanduser
from functools import partial
import os
import pygame

#Base Structure
class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(982, 633)
        SecondWindow.setStyleSheet("background-color: rgb(38, 88, 15);")
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.detail_label = QtWidgets.QLabel(self.centralwidget)
        self.detail_label.setGeometry(QtCore.QRect(0, 100, 221, 511))
        self.detail_label.setStyleSheet("background-color: rgb(136, 220, 61);")
        self.detail_label.setText("")
        self.detail_label.setObjectName("detail_label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 0, 331, 611))
        self.label_3.setStyleSheet("background-color: rgb(57, 231, 95);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(230, 10, 311, 291))
        self.image_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.image_label.setText("")
        self.image_label.setPixmap(QtGui.QPixmap("41ZYmSCDO4L._AC_SY580_.jpg"))
        self.image_label.setObjectName("image_label")
        self.track_label = QtWidgets.QLabel(self.centralwidget)
        self.track_label.setGeometry(QtCore.QRect(240, 320, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        self.track_label.setFont(font)
        self.track_label.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.track_label.setStyleSheet("background-color: rgb(57, 231, 95);\n"
"color: rgb(255, 158, 165);\n"
"color: rgb(209, 50, 69);")
        self.track_label.setText("")
        self.track_label.setAlignment(QtCore.Qt.AlignCenter)
        self.track_label.setObjectName("track_label")
        self.preview_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.prev())
        self.preview_pushButton.setGeometry(QtCore.QRect(246, 476, 81, 45))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.preview_pushButton.setFont(font)
        self.preview_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.preview_pushButton.setStyleSheet("background-color: rgb(57, 231, 95);\n"
"")
        self.preview_pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icons/icons/preview5.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.preview_pushButton.setIcon(icon)
        self.preview_pushButton.setIconSize(QtCore.QSize(69, 68))
        self.preview_pushButton.setFlat(False)
        self.preview_pushButton.setObjectName("preview_pushButton")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(240, 392, 293, 22))
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.horizontalSlider.setStyleSheet("background-color: rgb(57, 231, 95);")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.loc_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.get_music())
        self.loc_pushButton.setGeometry(QtCore.QRect(560, 10, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        self.loc_pushButton.setFont(font)
        self.loc_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loc_pushButton.setStyleSheet("background-color: rgb(255, 193, 130);\n"
"color: rgb(20, 125, 27);\n"
"border-radius: 20px;")
        self.loc_pushButton.setObjectName("loc_pushButton")
        self.del_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.delete())
        self.del_pushButton.setGeometry(QtCore.QRect(690, 10, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        self.del_pushButton.setFont(font)
        self.del_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.del_pushButton.setStyleSheet("background-color: rgb(255, 193, 130);\n"
"color: rgb(20, 125, 27);\n"
"border-radius: 20px;")
        self.del_pushButton.setObjectName("del_pushButton")
        self.pause_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.puase())
        self.pause_pushButton.setGeometry(QtCore.QRect(350, 550, 81, 45))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.pause_pushButton.setFont(font)
        self.pause_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pause_pushButton.setStyleSheet("background-color: rgb(57, 231, 95);\n"
"")
        self.pause_pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icons/icons/puase555.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_pushButton.setIcon(icon1)
        self.pause_pushButton.setIconSize(QtCore.QSize(69, 68))
        self.pause_pushButton.setFlat(False)
        self.pause_pushButton.setObjectName("pause_pushButton")
        self.play_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.play())
        self.play_pushButton.setGeometry(QtCore.QRect(350, 476, 81, 45))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.play_pushButton.setFont(font)
        self.play_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.play_pushButton.setStyleSheet("background-color: rgb(57, 231, 95);\n"
"\n"
"\n"
"")
        self.play_pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icons/icons/play555.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_pushButton.setIcon(icon2)
        self.play_pushButton.setIconSize(QtCore.QSize(68, 69))
        self.play_pushButton.setFlat(False)
        self.play_pushButton.setObjectName("play_pushButton")
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.next())
        self.next_pushButton.setGeometry(QtCore.QRect(448, 476, 81, 45))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next_pushButton.setStyleSheet("background-color: rgb(57, 231, 95);\n"
"")
        self.next_pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/icons/icons/next555.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_pushButton.setIcon(icon3)
        self.next_pushButton.setIconSize(QtCore.QSize(68, 69))
        self.next_pushButton.setFlat(False)
        self.next_pushButton.setObjectName("next_pushButton")
        self.stop_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.stop())
        self.stop_pushButton.setGeometry(QtCore.QRect(450, 550, 81, 45))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.stop_pushButton.setFont(font)
        self.stop_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_pushButton.setStyleSheet("background-color: rgb(57, 231, 95);\n"
"")
        self.stop_pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/icons/icons/stop.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_pushButton.setIcon(icon4)
        self.stop_pushButton.setIconSize(QtCore.QSize(69, 68))
        self.stop_pushButton.setFlat(False)
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.repeat_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.repeat())
        self.repeat_pushButton.setGeometry(QtCore.QRect(244, 550, 81, 45))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.repeat_pushButton.setFont(font)
        self.repeat_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.repeat_pushButton.setStyleSheet("background-color: rgb(57, 231, 95);\n"
"")
        self.repeat_pushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/icons/icons/oooo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.repeat_pushButton.setIcon(icon5)
        self.repeat_pushButton.setIconSize(QtCore.QSize(69, 68))
        self.repeat_pushButton.setFlat(False)
        self.repeat_pushButton.setObjectName("repeat_pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(970, -3, 20, 81))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.album_label = QtWidgets.QLabel(self.centralwidget)
        self.album_label.setGeometry(QtCore.QRect(10, 269, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.album_label.setFont(font)
        self.album_label.setStyleSheet("background-color: rgb(136, 220, 61);\n"
"color: rgb(236, 29, 164);")
        self.album_label.setObjectName("album_label")
        self.released_label = QtWidgets.QLabel(self.centralwidget)
        self.released_label.setGeometry(QtCore.QRect(10, 385, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.released_label.setFont(font)
        self.released_label.setStyleSheet("background-color: rgb(136, 220, 61);\n"
"color: rgb(236, 29, 164);")
        self.released_label.setObjectName("released_label")
        self.genre_label = QtWidgets.QLabel(self.centralwidget)
        self.genre_label.setGeometry(QtCore.QRect(10, 494, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.genre_label.setFont(font)
        self.genre_label.setStyleSheet("background-color: rgb(136, 220, 61);\n"
"color: rgb(236, 29, 164);")
        self.genre_label.setObjectName("genre_label")
        self.clear_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clear())
        self.clear_pushButton.setGeometry(QtCore.QRect(840, 10, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        self.clear_pushButton.setFont(font)
        self.clear_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_pushButton.setStyleSheet("background-color: rgb(255, 193, 130);\n"
"color: rgb(20, 125, 27);\n"
"border-radius: 20px;")
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(550, 70, 429, 541))
        self.listWidget.setStyleSheet("background-color: rgb(135, 171, 105);")
        self.listWidget.setObjectName("listWidget")
        self.artist_label = QtWidgets.QLabel(self.centralwidget)
        self.artist_label.setGeometry(QtCore.QRect(10, 151, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.artist_label.setFont(font)
        self.artist_label.setStyleSheet("background-color: rgb(136, 220, 61);\n"
"color: rgb(236, 29, 164);")
        self.artist_label.setObjectName("artist_label")
        self.volume_label = QtWidgets.QLabel(self.centralwidget)
        self.volume_label.setGeometry(QtCore.QRect(100, 40, 21, 29))
        self.volume_label.setStyleSheet("background-color: rgb(38, 88, 15);")
        self.volume_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.volume_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.volume_label.setLineWidth(1)
        self.volume_label.setText("")
        self.volume_label.setPixmap(QtGui.QPixmap("images/icons/icons/speaker-volume.png"))
        self.volume_label.setObjectName("volume_label")
        self.vplus_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.low_v())
        self.vplus_pushButton.setGeometry(QtCore.QRect(10, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        self.vplus_pushButton.setFont(font)
        self.vplus_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.vplus_pushButton.setStyleSheet("background-color: rgb(38, 88, 15);")
        self.vplus_pushButton.setIconSize(QtCore.QSize(69, 68))
        self.vplus_pushButton.setFlat(False)
        self.vplus_pushButton.setObjectName("vplus_pushButton")
        self.vminus_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.high_v())
        self.vminus_pushButton.setGeometry(QtCore.QRect(120, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        self.vminus_pushButton.setFont(font)
        self.vminus_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.vminus_pushButton.setStyleSheet("background-color: rgb(38, 88, 15);")
        self.vminus_pushButton.setIconSize(QtCore.QSize(69, 68))
        self.vminus_pushButton.setFlat(False)
        self.vminus_pushButton.setObjectName("vminus_pushButton")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

        # Create playlist
        self.dir = f'{QDir.currentPath()}'
        self.url = QUrl()
        self.player = QMediaPlayer()
        self.content = QMediaContent()
        self.playlist = QMediaPlaylist(self.player)
        self.player.setPlaylist(self.playlist)

        self.playlist.currentIndexChanged.connect(self.update)
        self.player.metaDataChanged.connect(self.meta_data)

        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MusicPlayer"))
        self.vplus_pushButton.setText(_translate("SecondWindow", "v-"))
        self.vminus_pushButton.setText(_translate("SecondWindow", "v+"))
        self.artist_label.setText(_translate("SecondWindow", "  Автор:  "))
        self.album_label.setText(_translate("SecondWindow", "  Альбом:   "))
        self.genre_label.setText(_translate("SecondWindow", "  Genre:  "))
        self.released_label.setText(_translate("SecondWindow", "  Released: "))
        self.loc_pushButton.setText(_translate("SecondWindow", "Select Music"))
        self.del_pushButton.setText(_translate("SecondWindow", "Delete From Playlist"))
        self.clear_pushButton.setText(_translate("SecondWindow", "Clear Playlist"))
# import resource


    # Get music metadata
    def meta_data(self):
        if self.player.isMetaDataAvailable():
            self.artist_label.setText(f'Artist: {self.player.metaData(QMediaMetaData.Author)}')
            self.album_label.setText(f'Album: {self.player.metaData(QMediaMetaData.AlbumTitle)}')
            self.track_label.setText(f'Track: {self.player.metaData(QMediaMetaData.Title)}')
            self.released_label.setText(f'Released: {self.player.metaData(QMediaMetaData.Year)}')
            self.genre_label.setText(f'Genre: {self.player.metaData(QMediaMetaData.Genre)}')
            # pixmap = QtGui.QPixmap()
            # metadata = mutagen.File()
            # for tag in metadata.tags.values():
            #     if tag.FrameID == 'APIC':
            #         pixmap.loadFromData(tag.data)
            #         break
            # self.image_label.setPixmap(pixmap)

    #Get a track and add the playlist
    def get_music(self):
        files = QFileDialog.getOpenFileNames(None, filter='Audio Files (*.mp3 *.mp4 *.avi *.mov *.ogg *.wav)')
        for track in files[0]:
            self.playlist.addMedia(QMediaContent(self.url.fromLocalFile(track)))
            track = track.split('/')
            self.listWidget.addItem(f'{track[-1][:-4]}')
        self.listWidget.setCurrentRow(0)
        self.playlist.setCurrentIndex(0)

    #Play a track
    def play(self):
        self.playlist.setCurrentIndex(self.listWidget.currentRow())
        self.player.play()
    
    #For move position slider
    def position_changed(self, position):
        self.horizontalSlider.setValue(position)

    #For move duration slider
    def duration_changed(self, duration):
        self.horizontalSlider.setRange(0, duration)

    #For puase current track
    def puase(self):
        self.player.pause()

    #For stop current track
    def stop(self):
        self.player.stop()
        self.playlist.setCurrentIndex(0)
        self.listWidget.setCurrentRow(0)

    #For playing next track in playlist
    def next(self):
        self.playlist.next()
        if self.playlist.currentIndex() == -1:
            self.playlist.setCurrentIndex(0)
            self.player.play()

    #For playing preview track in playlist
    def prev(self):
        if self.playlist.previousIndex() == -1:
            self.playlist.setCurrentIndex(self.playlist.mediaCount()-1)
        else:
            self.playlist.previous()

    #For repeat playlist
    def repeat(self):
        pygame.mixer.init()
        pygame.mixer.music.play(loops=-1)

    #For decrease volume
    def low_v(self):
        vol = self.player.volume()
        vol = max(vol-5,0)
        self.player.setVolume(vol)

    #For increase volume
    def high_v(self):
        vol = self.player.volume()
        vol = min(vol+5,100)
        self.player.setVolume(vol)

    #For delete track from playlist
    def delete(self):
        #Grab the selected row or current row
        clicked = self.listWidget.currentRow()
        #Delete selected row
        self.listWidget.takeItem(clicked)

    #For clear playlist
    def clear(self):
        self.player.stop()
        self.listWidget.clear()
        self.playlist.clear()
        self.track_label.setText('Track: ')
        self.artist_label.setText('Artist: ')
        self.album_label.setText('Album: ')
        self.released_label.setText('Released: ')
        self.genre_label.setText('Genre: ')

    #For updating the listbox when the playlist updates
    def update(self):
        self.listWidget.setCurrentRow(self.playlist.currentIndex())
        if self.playlist.currentIndex() < 0:
            self.listWidget.setCurrentRow(0)
            self.playlist.setCurrentIndex(0)

        
    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MusicPlayer"))
        self.loc_pushButton.setText(_translate("SecondWindow", "Select Music"))
        self.del_pushButton.setText(_translate("SecondWindow", "Delete From Playlist"))
        self.album_label.setText(_translate("SecondWindow", "Album:   "))
        self.released_label.setText(_translate("SecondWindow", "Released: "))
        self.genre_label.setText(_translate("SecondWindow", "Genre:  "))
        self.clear_pushButton.setText(_translate("SecondWindow", "Clear Playlist"))
        self.artist_label.setText(_translate("SecondWindow", "Artist:  "))
        self.vplus_pushButton.setText(_translate("SecondWindow", "v-"))
        self.vminus_pushButton.setText(_translate("SecondWindow", "v+"))

#Initialize The App
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
