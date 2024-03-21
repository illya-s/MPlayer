import sys, os, random, glob
import resource_rc

from PySide6.QtUiTools import QUiLoader, loadUiType
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QUrl, QDir, Qt, QFile, QPoint
from PySide6.QtWidgets import QFileDialog, QMainWindow
from PySide6.QtGui import QIcon
from pathlib import Path
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

from metadata import get_title, get_artist, get_cover

import pygame

def UiClass(path):
    formClass, widgetClass = loadUiType(path)
    name = os.path.basename(path).replace('.', '_')
    def __init__(self, parent=None):
        widgetClass.__init__(self, parent)
        formClass.__init__(self)
        self.setupUi(self)
    return type(name, (widgetClass, formClass), {'__init__': __init__})

class MainWindow(UiClass("gui/design.ui")):
    def __init__(self):
        super().__init__()

        self.dragging = False
        self.offset = None

        self.muted = False
        self.playPause = True
        self.rand_pressed = False
        self.setWindowFlags(Qt.FramelessWindowHint)

        # self.dir = f'{QDir.currentPath()}'
        # self.url = QUrl()
        self.player = pygame.mixer
        self.player.init()
        self.player.music.set_volume(0.7)
        self.playlist = []
        self.currentIndex = 0

        # self.player.metaDataChanged.connect(self.meta_data)
        # self.player.positionChanged.connect(self.position_changed)
        # self.player.durationChanged.connect(self.duration_changed)

        # self.play_pushButton.setEnabled(False)

        self.valumeSlider.sliderMoved.connect(self.volume_slider_changed)
        self.audioPosSlider.sliderMoved.connect(self.play_slider_changed)
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.updateSlider)
        # self.timer.start(1000)

        # self._pushButton.clicked.connect(self.minimized)
        self._pushButton.clicked.connect(self.showMinimized)
        # self.pushButton.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.close)
        self.chengeMuteBtn.clicked.connect(self.volume_mute)
        self.prevBtn.clicked.connect(self.prev)
        self.nextBtn.clicked.connect(self.next)
        self.chengePlayBtn.clicked.connect(self.togglePlay)
        self.openFolderBtn.clicked.connect(self.get_folder)
        # self.del_pushButton.clicked.connect(self.delete)
        # self.clear_pushButton.clicked.connect(self.clear)
        # self.rand_pushButton.clicked.connect(self.sortRandom)

# ------------------------------------------------------------------------------------

    def get_folder(self):
        directory = Path(QFileDialog.getExistingDirectory())
        extensions = ('*.mp3', '*.mp4', '*.avi', '*.mov', '*.ogg', '*.wav')
        directory_files = []
        for ext in extensions:
            directory_files.extend(glob.glob(f"{directory}/{ext}"))
        self.playlist = directory_files
        for i in directory_files:
            self.listMusic.addItem(i)
        self.currentIndex = 0
        self.player.music.load(self.playlist[self.currentIndex])
        self.get_meta_data()


    def get_meta_data(self):
        try:
            artist = get_artist(self.playlist[self.currentIndex])
            title = get_title(self.playlist[self.currentIndex])
            self.track_label.setText(title)
            self.artist_label.setText(artist)

            
            if '.mp3' in self.playlist[self.currentIndex]:
                pixmap = QtGui.QPixmap()
                image_data = get_cover(self.playlist[self.currentIndex])
                pixmap.loadFromData(image_data)
                self.image_label.setPixmap(pixmap)
            else:
                print("No cover found.")
                self.image_label.clear()
        except Exception as e:
            print("Error:", e)

    def togglePlay(self):
        if(self.playPause):
            self.pause()
        else:
            self.play()
    def pause(self):
        self.player.music.play()
        self.chengePlayBtn.setIcon(QIcon(":/icons/pause.png"))
        self.playPause = False
    def play(self):
        self.player.music.pause()
        self.chengePlayBtn.setIcon(QIcon(":/icons/play.png"))
        self.playPause = True

    def play_slider_changed(self, position):
        self.player.music.set_pos(position * 100)

    def next(self):
        if len(self.playlist) <= (self.currentIndex + 1):
            self.currentIndex = 0
        else:
            self.currentIndex += 1
        self.get_meta_data()
        self.player.music.load(self.playlist[self.currentIndex])
        self.player.music.play()

    def prev(self):
        if self.currentIndex <= 0:
            self.currentIndex = (len(self.playlist) - 1)
        else:
            self.currentIndex -= 1
        self.get_meta_data()
        self.player.music.load(self.playlist[self.currentIndex])
        self.player.music.play()

    # def delete(self):
    #     clicked = self.ui.listWidget.currentRow()
    #     self.ui.listWidget.takeItem(clicked)

    # def clear(self):
    #     # self.player.stop()
    #     self.ui.listWidget.clear()
    #     # self.playlist.clear()
    #     self.ui.track_label.clear()
    #     self.ui.artist_label.clear()

    # def update(self):
    #     # self.ui.listWidget.setCurrentRow(self.playlist.currentIndex())
    #     # if self.playlist.currentIndex() < 0:
    #         self.ui.listWidget.setCurrentRow(0)
    #         # self.playlist.setCurrentIndex(0)

    # def position_changed(self, position):
    #     if(self.ui.horizontalSlider.maximum() != self.player.duration()):
    #         self.ui.horizontalSlider.setMaximum(self.player.duration())
    #     self.ui.horizontalSlider.setValue(position)

        # seconds = (position / 1000) % 60
        # minutes = (position / 60000) % 60
        # hours = (position / 2600000) % 24

        # time = QTime(hours, minutes, seconds)
        # self.label.setText(time.toString())

    # def duration_changed(self, duration):
    #     self.ui.horizontalSlider.setRange(0, duration)

    def volume_slider_changed(self, position):
        if self.muted:
            self.chengeMuteBtn.setIcon(QIcon(":/icons/volume.png"))
            self.muted = False
        self.player.music.set_volume((position / 100))

    def volume_mute(self):
        if self.muted:
            self.valumeSlider.setTickPosition(100)
            self.player.music.set_volume(1)
            self.chengeMuteBtn.setIcon(QIcon(":/icons/volume.png"))
            self.muted = False
        else:
            self.valumeSlider.setTickPosition(0)
            self.player.music.set_volume(0)
            self.chengeMuteBtn.setIcon(QIcon(":/icons/mute.png"))
            self.muted = True


    # def sortRandom(self):
    #     self.rand_pressed = True
    #     list_item = [self.ui.listWidget.item(row).text() for row in range(self.ui.listWidget.count())]
        # data = pd.DataFrame(dict(
        # 	Путь=[self.dir],
        # 	Список=[list_item]))
        # print(data)
        # random.shuffle(list_item)
        # print(data)
        # self.ui.listWidget
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = QPoint(event.position().x(), event.position().y())
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:

            self.move(self.pos() + QPoint(event.scenePosition().x(),event.scenePosition().y()) - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())