# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(575, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(575, 500))
        MainWindow.setMaximumSize(QSize(575, 500))
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(10)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle(u"")
        icon = QIcon()
        icon.addFile(u":/icons/player.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        MainWindow.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        MainWindow.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background: #121212;\n"
"	border-top-right-radius: 10px;\n"
"	border-top-left-radius:  10px;\n"
"}\n"
"*{\n"
"	color: #fff;\n"
"	margin: 0;\n"
"	padding: 0;\n"
"}\n"
"QWidget {\n"
"	background-color: #121212;\n"
"	font-family: Rubik;\n"
"	font-weight: 600;\n"
"}\n"
"QPushButton {\n"
"	border: none;\n"
"}\n"
"QListWidget {\n"
"	border: none;\n"
"	background-color: #121212;\n"
"}\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	outline: none;\n"
"	background: #676767;\n"
"	width: 8px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: #676767;\n"
"}\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	outline: none;\n"
"	background: #676767;\n"
"	height: 8px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: #676767;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	border: none;\n"
"	background: #32CC99;\n"
"	width: 20px;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"	border: none;\n"
"	background: #32CC99;\n"
"	width: 20px;\n"
"}\n"
"QScrollBar:left-arrow:horizontal, QScrollB"
                        "ar::right-arrow:horizontal {\n"
"	border: none;\n"
"	background: #121212;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: #999;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	background: #999;\n"
"}")
        MainWindow.setWindowFilePath(u"")
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.Main = QWidget(MainWindow)
        self.Main.setObjectName(u"Main")
        self.Main.setEnabled(True)
        self.Main.setMaximumSize(QSize(575, 500))
        self.Main.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.Main)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.image_label = QLabel(self.Main)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setMinimumSize(QSize(150, 150))
        self.image_label.setMaximumSize(QSize(150, 150))
        self.image_label.setStyleSheet(u"margin: 0;\n"
"border: none;\n"
"background-color: #fff;")
        self.image_label.setIndent(0)

        self.horizontalLayout_2.addWidget(self.image_label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(365, -1, -1, -1)
        self._pushButton = QPushButton(self.Main)
        self._pushButton.setObjectName(u"_pushButton")
        self._pushButton.setMinimumSize(QSize(30, 30))
        self._pushButton.setMaximumSize(QSize(30, 30))
        self._pushButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color:#353535;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self._pushButton.setIcon(icon1)
        self._pushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self._pushButton)

        self.pushButton = QPushButton(self.Main)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setMaximumSize(QSize(30, 30))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color:#353535;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.track_label = QLabel(self.Main)
        self.track_label.setObjectName(u"track_label")
        self.track_label.setMinimumSize(QSize(0, 75))
        self.track_label.setMaximumSize(QSize(425, 75))
        font1 = QFont()
        font1.setFamilies([u"Rubik"])
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setKerning(False)
        self.track_label.setFont(font1)
        self.track_label.setCursor(QCursor(Qt.ArrowCursor))
        self.track_label.setStyleSheet(u"font-size: 24pt;\n"
"padding: 0 0 0 10px;")
        self.track_label.setText(u"")
        self.track_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.track_label.setIndent(0)

        self.verticalLayout.addWidget(self.track_label)

        self.artist_label = QLabel(self.Main)
        self.artist_label.setObjectName(u"artist_label")
        self.artist_label.setMinimumSize(QSize(0, 45))
        self.artist_label.setMaximumSize(QSize(425, 45))
        font2 = QFont()
        font2.setFamilies([u"Rubik"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setKerning(False)
        self.artist_label.setFont(font2)
        self.artist_label.setStyleSheet(u"font-size: 10pt;\n"
"padding: 0 0 0 10px;")
        self.artist_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.artist_label)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalSlider = QSlider(self.Main)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimumSize(QSize(0, 25))
        self.horizontalSlider.setMaximumSize(QSize(16777215, 26))
        self.horizontalSlider.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    background: #fff;\n"
"    width: 5px;\n"
"    margin: -2px 0;\n"
"    border: 5px solid #fff;\n"
"    border-radius: 4px;\n"
" }\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: #888;\n"
"	margin: 2px 0;\n"
"	border-radius: 2px;\n"
" }")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider)

        self.management_menu = QHBoxLayout()
        self.management_menu.setSpacing(5)
        self.management_menu.setObjectName(u"management_menu")
        self.management_menu.setContentsMargins(2, 4, 2, 4)
        self.preview_pushButton = QPushButton(self.Main)
        self.preview_pushButton.setObjectName(u"preview_pushButton")
        self.preview_pushButton.setMinimumSize(QSize(0, 0))
        self.preview_pushButton.setMaximumSize(QSize(40, 40))
        self.preview_pushButton.setFont(font)
        self.preview_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.preview_pushButton.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/back-.png", QSize(), QIcon.Normal, QIcon.Off)
        self.preview_pushButton.setIcon(icon3)
        self.preview_pushButton.setIconSize(QSize(40, 40))
        self.preview_pushButton.setFlat(False)

        self.management_menu.addWidget(self.preview_pushButton)

        self.play_pushButton = QPushButton(self.Main)
        self.play_pushButton.setObjectName(u"play_pushButton")
        self.play_pushButton.setMinimumSize(QSize(0, 0))
        self.play_pushButton.setMaximumSize(QSize(40, 40))
        self.play_pushButton.setFont(font)
        self.play_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.play_pushButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play_pushButton.setIcon(icon4)
        self.play_pushButton.setIconSize(QSize(40, 40))
        self.play_pushButton.setFlat(False)

        self.management_menu.addWidget(self.play_pushButton)

        self.next_pushButton = QPushButton(self.Main)
        self.next_pushButton.setObjectName(u"next_pushButton")
        self.next_pushButton.setMinimumSize(QSize(0, 0))
        self.next_pushButton.setMaximumSize(QSize(40, 40))
        self.next_pushButton.setFont(font)
        self.next_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_pushButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/forward+.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_pushButton.setIcon(icon5)
        self.next_pushButton.setIconSize(QSize(40, 40))
        self.next_pushButton.setFlat(False)

        self.management_menu.addWidget(self.next_pushButton)

        self.mute_pushButton = QPushButton(self.Main)
        self.mute_pushButton.setObjectName(u"mute_pushButton")
        self.mute_pushButton.setMinimumSize(QSize(25, 25))
        self.mute_pushButton.setMaximumSize(QSize(40, 40))
        self.mute_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.mute_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.mute_pushButton.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/volume.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mute_pushButton.setIcon(icon6)
        self.mute_pushButton.setIconSize(QSize(40, 40))

        self.management_menu.addWidget(self.mute_pushButton)

        self.valume_Slider = QSlider(self.Main)
        self.valume_Slider.setObjectName(u"valume_Slider")
        self.valume_Slider.setMinimumSize(QSize(100, 25))
        self.valume_Slider.setMaximumSize(QSize(100, 25))
        self.valume_Slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.valume_Slider.setToolTipDuration(-1)
        self.valume_Slider.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    background: #fff;\n"
"    width: 5px;\n"
"    margin: -2px 0;\n"
"    border: 5px solid #fff;\n"
"    border-radius: 4px;\n"
" }\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: #888;\n"
"	margin: 2px 0;\n"
"	border-radius: 2px;\n"
" }")
        self.valume_Slider.setMaximum(100)
        self.valume_Slider.setSingleStep(1)
        self.valume_Slider.setValue(100)
        self.valume_Slider.setTracking(True)
        self.valume_Slider.setOrientation(Qt.Horizontal)
        self.valume_Slider.setInvertedAppearance(False)
        self.valume_Slider.setTickInterval(0)

        self.management_menu.addWidget(self.valume_Slider)


        self.verticalLayout_2.addLayout(self.management_menu)

        self.listWidget = QListWidget(self.Main)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 0))
        self.listWidget.setMaximumSize(QSize(16777215, 300))
        self.listWidget.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.listWidget)

        self.select_btns = QHBoxLayout()
        self.select_btns.setSpacing(0)
        self.select_btns.setObjectName(u"select_btns")
        self.select_btns.setContentsMargins(-1, 0, 0, 2)
        self.rand_pushButton = QPushButton(self.Main)
        self.rand_pushButton.setObjectName(u"rand_pushButton")
        self.rand_pushButton.setMaximumSize(QSize(40, 40))
        self.rand_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/random.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rand_pushButton.setIcon(icon7)
        self.rand_pushButton.setIconSize(QSize(40, 40))

        self.select_btns.addWidget(self.rand_pushButton)

        self.loc_pushButton = QPushButton(self.Main)
        self.loc_pushButton.setObjectName(u"loc_pushButton")
        self.loc_pushButton.setMinimumSize(QSize(0, 30))
        self.loc_pushButton.setMaximumSize(QSize(40, 40))
        self.loc_pushButton.setFont(font)
        self.loc_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.loc_pushButton.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/select.png", QSize(), QIcon.Normal, QIcon.Off)
        self.loc_pushButton.setIcon(icon8)
        self.loc_pushButton.setIconSize(QSize(40, 40))

        self.select_btns.addWidget(self.loc_pushButton)

        self.del_pushButton = QPushButton(self.Main)
        self.del_pushButton.setObjectName(u"del_pushButton")
        self.del_pushButton.setMinimumSize(QSize(0, 30))
        self.del_pushButton.setMaximumSize(QSize(40, 40))
        self.del_pushButton.setFont(font)
        self.del_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.del_pushButton.setStyleSheet(u"")
        self.del_pushButton.setIcon(icon1)
        self.del_pushButton.setIconSize(QSize(40, 40))

        self.select_btns.addWidget(self.del_pushButton)

        self.clear_pushButton = QPushButton(self.Main)
        self.clear_pushButton.setObjectName(u"clear_pushButton")
        self.clear_pushButton.setMinimumSize(QSize(0, 30))
        self.clear_pushButton.setMaximumSize(QSize(40, 40))
        self.clear_pushButton.setFont(font)
        self.clear_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_pushButton.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_pushButton.setIcon(icon9)
        self.clear_pushButton.setIconSize(QSize(40, 40))

        self.select_btns.addWidget(self.clear_pushButton)


        self.verticalLayout_2.addLayout(self.select_btns)

        MainWindow.setCentralWidget(self.Main)
        QWidget.setTabOrder(self.valume_Slider, self.del_pushButton)
        QWidget.setTabOrder(self.del_pushButton, self.clear_pushButton)

        self.retranslateUi(MainWindow)

        self.listWidget.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.image_label.setText("")
        self._pushButton.setText("")
        self.pushButton.setText("")
        self.artist_label.setText("")
        self.preview_pushButton.setText("")
        self.play_pushButton.setText("")
        self.next_pushButton.setText("")
        self.mute_pushButton.setText("")
        self.rand_pushButton.setText("")
        self.loc_pushButton.setText("")
        self.del_pushButton.setText("")
        self.clear_pushButton.setText("")
        pass
    # retranslateUi

