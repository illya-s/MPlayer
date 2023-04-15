import sys
import random
import resource_rc
import mutagen
import pandas as pd
import os

from design import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, QDir, Qt, QSettings, QTime, QCoreApplication
from PyQt5.QtWidgets import QFileDialog, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist, QMediaMetaData


# from mutagen.mp3 import MP3
# from mutagen import id3 as mu
# from mutagen import *

# from os.path import expanduser
# from functools import partial
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.muted = False
		self.playPause = True
		self.rand_pressed = False
		self.setWindowFlags(Qt.FramelessWindowHint)

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

		self.ui.play_pushButton.setEnabled(False)

		self.ui.valume_Slider.sliderMoved.connect(self.volume_slider_changed)
		self.ui.horizontalSlider.sliderMoved.connect(self.play_slider_changed)

		self.ui._pushButton.clicked.connect(self.minimized)
		self.ui.pushButton.clicked.connect(self.close)
		self.ui.mute_pushButton.clicked.connect(self.volume_mute)
		self.ui.preview_pushButton.clicked.connect(self.prev)
		self.ui.next_pushButton.clicked.connect(self.next)
		self.ui.play_pushButton.clicked.connect(self.play)
		self.ui.loc_pushButton.clicked.connect(self.get_music)
		self.ui.del_pushButton.clicked.connect(self.delete)
		self.ui.clear_pushButton.clicked.connect(self.clear)
		self.ui.rand_pushButton.clicked.connect(self.sortRandom)

# ------------------------------------------------------------------------------------

	def get_music(self):
		files = QFileDialog.getOpenFileNames(None, filter='Audio Files (*.mp3 *.mp4 *.avi *.mov *.ogg *.wav)')
		for track in files[0]:
			self.playlist.addMedia(QMediaContent(self.url.fromLocalFile(track)))
			track = track.split('/')
			self.ui.listWidget.addItem(f'{track[-1][:-4]}')
		self.ui.play_pushButton.setEnabled(True)
		self.ui.listWidget.setCurrentRow(0)
		self.playlist.setCurrentIndex(0)

	def meta_data(self):
		if self.player.isMetaDataAvailable():
			if self.player.metaData(QMediaMetaData.Title) is None:
				result = "Name unknown"
				self.ui.track_label.setText(result)
			else:
				string = self.player.metaData(QMediaMetaData.Title)
				result = ""
				index = ["()","-",".","holycrds","pro"]
				for i in string:
					if i not in index:
						result += i
				self.ui.track_label.setText(result.translate({ord(i): None for i in 'holycrdspro'}))
			# -------------------------------------------------------
			if self.player.metaData(QMediaMetaData.Author) is None:
				result_string = "Name unknown"
				self.ui.artist_label.setText(result_string)
			else:
				my_string = self.player.metaData(QMediaMetaData.Author)
				result_string = ""
				index = ["[","]","'"]
				for i in my_string:
					if i not in index:
						result_string += i
				self.ui.artist_label.setText(result_string)
			# pixmap = QtGui.QPixmap()
			# # track = track.split('/')
			# metadata = mutagen.File(f'{QMediaContent(self.url.fromLocalFile())}')
			# for tag in metadata.tags.values():
			# 	if tag.FrameID == 'APIC':
			# 		pixmap.loadFromData(tag.data)
			# 		break
			# self.image_label.setPixmap(pixmap)

	# def stop(self):
	# 	self.player.stop()
	# 	self.playlist.setCurrentIndex(0)
	# 	self.listWidget.setCurrentRow(0)

	def play(self):
		if(self.playPause):
			self.paused()
		else:
			self.played()
	def paused(self):
		self.playlist.setCurrentIndex(self.ui.listWidget.currentRow())
		self.player.play()
		self.ui.play_pushButton.setIcon(QIcon(":/icons/play.png"))
		self.playPause = False
	def played(self):
		self.player.pause()
		self.ui.play_pushButton.setIcon(QIcon(":/icons/pause.png"))
		self.playPause = True

	def play_slider_changed(self, position):
		self.player.setPosition(position)

	def next(self):
		self.playlist.next()
		if self.playlist.currentIndex() == -1:
			self.playlist.setCurrentIndex(0)
			self.player.play()

	def prev(self):
		if self.playlist.previousIndex() == -1:
			self.playlist.setCurrentIndex(self.playlist.mediaCount()-1)
		else:
			self.playlist.previous()

	def delete(self):
		clicked = self.ui.listWidget.currentRow()
		self.ui.listWidget.takeItem(clicked)

	def clear(self):
		self.player.stop()
		self.ui.listWidget.clear()
		self.playlist.clear()
		self.ui.track_label.clear()
		self.ui.artist_label.clear()

	def update(self):
		self.ui.listWidget.setCurrentRow(self.playlist.currentIndex())
		if self.playlist.currentIndex() < 0:
			self.ui.listWidget.setCurrentRow(0)
			self.playlist.setCurrentIndex(0)

	def position_changed(self, position):
		if(self.ui.horizontalSlider.maximum() != self.player.duration()):
			self.ui.horizontalSlider.setMaximum(self.player.duration())
		self.ui.horizontalSlider.setValue(position)

		# seconds = (position / 1000) % 60
		# minutes = (position / 60000) % 60
		# hours = (position / 2600000) % 24

		# time = QTime(hours, minutes, seconds)
		# self.label.setText(time.toString())

	def duration_changed(self, duration):
		self.ui.horizontalSlider.setRange(0, duration)

	def volume_slider_changed(self, position):
		self.player.setVolume(position)

	def volume_mute(self):
		if(self.muted):
			self.player.setMuted(False)
			self.ui.mute_pushButton.setIcon(QIcon(":/icons/volume.png"))
			self.muted = False
		else:
			self.player.setMuted(True)
			self.ui.mute_pushButton.setIcon(QIcon(":/icons/mute.png"))
			self.muted = True


	def sortRandom(self):
		self.rand_pressed = True
		list_item = [self.ui.listWidget.item(row).text() for row in range(self.ui.listWidget.count())]
		data = pd.DataFrame(dict(
			Путь=[self.dir],
			Список=[list_item]))
		print(data)
		random.shuffle(list_item)
		print(data)
		# self.ui.listWidget

	def minimized(self):
		self.setWindowState(self.windowState() | Qt.WindowMinimized)


	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.old_pos = event.pos()

	def mouseReleaseEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.old_pos = None

	def mouseMoveEvent(self, event):
		if not self.old_pos:
			return
		delta = event.pos() - self.old_pos
		self.move(self.pos() + delta)
	# def closeEvent(self,event):
	# 	#сохраняешь что надо
	# 	event.accepr(self.ui.listWidget.items())

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())