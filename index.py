import socket

from PyQt5 import QtWidgets, QtCore, QtGui, QtPrintSupport
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import os
from os import path
import sys
import sqlite3
import pymysql

from logIn import *

from time import *




class Splash(QDialog):
    def __init__(self):
        super(Splash, self).__init__()
        QWidget.__init__(self)
        uic.loadUi(path.join(path.dirname(__file__), "ui/splash.ui"), self)


        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowTitle('welcome back')
        self.timer = QBasicTimer()
        self.step = 0
        self.prog()
        self.today = str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))



    def prog(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(100, self)

    def timerEvent(self, event):
        if self.step >= 100 :
            self.timer.stop()
            self.logi = LogIn()
            self.logi.show()
            self.close()
            return
        self.step += 4
        self.progressBar.setValue(self.step)



def main():
    app = QtWidgets.QApplication(sys.argv)
    splash_wn = Splash()
    splash_wn.show()
    sys.exit(app.exec_())
if __name__ == '__main__' :
    main()