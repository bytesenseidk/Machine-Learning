import os
import sys
from DownloadMethods import Download
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QCoreApplication, QObject, QRunnable


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 592, 316)
        self.setWindowTitle("Youtube Downloader")
        self.font = QtGui.QFont()
        self.font.setFamily("Leelawadee UI")
        self.std_download_path = str(os.path.join(os.path.expanduser("~"), "Downloads"))
        self.initUI()


    def initUI(self):
        self.label_top = QtWidgets.QLabel(self)
        self.label_top.setObjectName("label_top")
        self.label_top.setGeometry(QtCore.QRect(130, 10, 331, 41))
        self.font.setPointSize(22)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.label_top.setFont(self.font)
        self.label_top.setAlignment(QtCore.Qt.AlignCenter)
        self.label_top.setText("Youtube Downloader")

        self.button_download = QtWidgets.QPushButton(self)
        self.button_download.setObjectName("button_download")
        self.button_download.setGeometry(QtCore.QRect(240, 170, 111, 51))
        self.font.setPointSize(14)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.button_download.setFont(self.font)
        self.button_download.setText("Download")
        self.button_download.clicked.connect(self.download_button)

        self.check_video = QtWidgets.QCheckBox(self)
        self.check_video.setObjectName("check_video")
        self.check_video.setGeometry(QtCore.QRect(390, 190, 151, 21))
        self.font.setPointSize(12)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.check_video.setFont(self.font)
        self.check_video.setText("Download Video")

        self.input_url = QtWidgets.QLineEdit(self)
        self.input_url.setObjectName("input_url")
        self.input_url.setGeometry(QtCore.QRect(20, 60, 551, 41))
        self.font.setPointSize(10)
        self.input_url.setFont(self.font)
        self.input_url.setAlignment(QtCore.Qt.AlignCenter)
        self.input_url.setText("")
        self.input_url.setPlaceholderText("Enter URL Here...")

        self.button_set = QtWidgets.QPushButton(self)
        self.button_set.setObjectName("button_set")
        self.button_set.setGeometry(QtCore.QRect(500, 110, 71, 41))
        self.button_set.setFont(self.font)
        self.button_set.setText("Set")
        self.button_set.clicked.connect(self.set_button)

        self.input_path = QtWidgets.QLineEdit(self)
        self.input_path.setObjectName("input_path")
        self.input_path.setGeometry(QtCore.QRect(20, 110, 471, 41))
        self.input_path.setFont(self.font)
        self.input_path.setAlignment(QtCore.Qt.AlignCenter)
        self.input_path.setText(self.std_download_path)

        self.radio_single = QtWidgets.QRadioButton(self)
        self.radio_single.setObjectName("radio_single")
        self.radio_single.setGeometry(QtCore.QRect(390, 160, 81, 21))
        self.radio_single.setFont(self.font)
        self.radio_single.setText("Single")
        self.radio_single.setChecked(True)

        self.radio_playlist = QtWidgets.QRadioButton(self)
        self.radio_playlist.setObjectName("radio_playlist")
        self.radio_playlist.setGeometry(QtCore.QRect(470, 160, 81, 21))
        self.radio_playlist.setFont(self.font)
        self.radio_playlist.setText("Playlist")

        self.label_done = QtWidgets.QLabel(self)
        self.label_done.setObjectName("label_done")
        self.label_done.setGeometry(QtCore.QRect(210, 240, 171, 31))
        self.font.setPointSize(14)
        self.font.setBold(False)
        self.font.setWeight(50)
        self.label_done.setFont(self.font)
        self.label_done.setAlignment(QtCore.Qt.AlignCenter)
        self.label_done.setText("")

        self.combo_quality = QtWidgets.QComboBox(self)
        self.combo_quality.addItem("")
        self.combo_quality.addItem("")
        self.combo_quality.addItem("")
        self.combo_quality.setObjectName("combo_quality")
        self.combo_quality.setGeometry(QtCore.QRect(90, 190, 69, 22))
        self.font.setPointSize(10)
        self.font.setBold(True)
        self.font.setWeight(65)
        self.combo_quality.setFont(self.font)
        self.combo_quality.setItemText(0, "Best")
        self.combo_quality.setItemText(1, "Semi")
        self.combo_quality.setItemText(2, "Worst")

        self.label_quality = QtWidgets.QLabel(self)
        self.label_quality.setObjectName("label_quality")
        self.label_quality.setGeometry(QtCore.QRect(50, 160, 151, 21))
        self.label_quality.setFont(self.font)
        self.label_quality.setAlignment(QtCore.Qt.AlignCenter)
        self.label_quality.setText("Download Quality:")


    def set_button(self):
        file_name = QFileDialog.getExistingDirectory()
        if file_name:
            self.input_path.setText(file_name)


    def download_button(self):
        url = self.input_url.text()
        save_path = self.input_path.text()
        quality = self.combo_quality.currentText()
        if self.radio_single.isChecked():
            playlist = False
        else:
            playlist = True
        if self.check_video.isChecked():
            Download(url, save_path, quality, playlist).mp4_download()
        else:
            Download(url, save_path, quality, playlist).mp3_download()
        self.input_url.setText("")
        self.label_done.setText("Download Done!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
