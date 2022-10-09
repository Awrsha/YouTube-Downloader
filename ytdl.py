from __future__ import unicode_literals
import youtube_dl
from PyQt5 import QtCore, QtGui, QtWidgets
#pip install youtube_dl

class Ui_ytdl(object):
    def setupUi(self, ytdl):
        ytdl.setObjectName("ytdl")
        ytdl.resize(894, 193)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        ytdl.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ytdl.setWindowIcon(icon)
        ytdl.setLayoutDirection(QtCore.Qt.RightToLeft)
        ytdl.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(ytdl)
        self.centralwidget.setObjectName("centralwidget")
        self.lblLink = QtWidgets.QLabel(self.centralwidget)
        self.lblLink.setGeometry(QtCore.QRect(760, 10, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(False)
        font.setKerning(False)
        self.lblLink.setFont(font)
        self.lblLink.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLink.setObjectName("lblLink")
        self.txtLink = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLink.setGeometry(QtCore.QRect(10, 10, 750, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.txtLink.setFont(font)
        self.txtLink.setObjectName("txtLink")
        self.btnDownload = QtWidgets.QPushButton(self.centralwidget)
        self.btnDownload.setGeometry(QtCore.QRect(10, 60, 300, 90))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnDownload.setFont(font)
        self.btnDownload.setObjectName("btnDownload")
        ytdl.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ytdl)
        self.statusbar.setObjectName("statusbar")
        ytdl.setStatusBar(self.statusbar)
        self.retranslateUi(ytdl)
        QtCore.QMetaObject.connectSlotsByName(ytdl)

    def retranslateUi(self, ytdl):
        _translate = QtCore.QCoreApplication.translate
        ytdl.setWindowTitle(_translate("ytdl", "نرم افزار دانلود از یوتیوب"))
        self.lblLink.setText(_translate("ytdl", "لینک دانلود"))
        self.btnDownload.setText(_translate("ytdl", "دانلود کن"))
        self.btnDownload.clicked.connect(self.downloadt)

    def downloadt(self):
        link=str(self.txtLink.text())
        ydl_opts = {}
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
                self.lblLink.setText("دانلود شد")
        except:
            self.lblLink.setText("خطا")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ytdl = QtWidgets.QMainWindow()
    ui = Ui_ytdl()
    ui.setupUi(ytdl)
    ytdl.show()
    sys.exit(app.exec_())
