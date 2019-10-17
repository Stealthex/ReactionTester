#!/usr/bin/env python3

import time
from functools import partial
import random
import sys
from threading import Timer

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(450, 350))
        self.setWindowTitle(
            "Reaction Timer")
        
        self.setStyleSheet('background-color: gray')
        self.setAutoFillBackground(True)

        self.pybutton = QPushButton('', self)
        self.pybutton.clicked.connect(partial(self.clickMethod, self.pybutton))
        self.pybutton.setGeometry(QtCore.QRect(30, 20, 71, 51))
        self.pybutton.setEnabled(False)

        self.pybutton2 = QPushButton('', self)
        self.pybutton2.clicked.connect(partial(self.clickMethod, self.pybutton2))
        self.pybutton2.setGeometry(QtCore.QRect(200, 20, 71, 51))
        self.pybutton2.setEnabled(False)

        self.pybutton3 = QPushButton('', self)
        self.pybutton3.clicked.connect(partial(self.clickMethod, self.pybutton3))
        self.pybutton3.setGeometry(QtCore.QRect(360, 20, 71, 51))
        self.pybutton3.setEnabled(False)

        self.pybutton4 = QPushButton('', self)
        self.pybutton4.clicked.connect(partial(self.clickMethod, self.pybutton4))
        self.pybutton4.setGeometry(QtCore.QRect(30, 150, 71, 51))
        self.pybutton4.setEnabled(False)

        self.pybutton5 = QPushButton('', self)
        self.pybutton5.clicked.connect(partial(self.clickMethod, self.pybutton5))
        self.pybutton5.setGeometry(QtCore.QRect(200, 150, 71, 51))
        self.pybutton5.setEnabled(False)

        self.pybutton6 = QPushButton('', self)
        self.pybutton6.clicked.connect(partial(self.clickMethod, self.pybutton6))
        self.pybutton6.setGeometry(QtCore.QRect(360, 150, 71, 51))
        self.pybutton6.setEnabled(False)

        self.pybutton7 = QPushButton('', self)
        self.pybutton7.clicked.connect(partial(self.clickMethod, self.pybutton7))
        self.pybutton7.setGeometry(QtCore.QRect(360, 280, 71, 51))
        self.pybutton7.setEnabled(False)

        self.pybutton8 = QPushButton('', self)
        self.pybutton8.clicked.connect(partial(self.clickMethod, self.pybutton8))
        self.pybutton8.setGeometry(QtCore.QRect(200, 280, 71, 51))
        self.pybutton8.setEnabled(False)

        self.pybutton9 = QPushButton('', self)
        self.pybutton9.clicked.connect(partial(self.clickMethod, self.pybutton9))
        self.pybutton9.setGeometry(QtCore.QRect(30, 280, 71, 51))
        self.pybutton9.setEnabled(False)

        self.buttonsClicked = 0
        self.buttonTimer = 0 
        self.buttonSpeed = .75

        buttonList = [self.pybutton, self.pybutton2, self.pybutton3, self.pybutton4, self.pybutton5, self.pybutton6, self.pybutton7, self.pybutton8, self.pybutton9]
        
        self.startTime = time.perf_counter() 
        self.clickTimes = []

        for i in range(10):
            randomButton = random.choice(buttonList)
            Timer(self.buttonTimer, self.activateButton, [randomButton]).start()
            Timer(self.buttonTimer + 2, self.deactivateButton, [randomButton]).start()
            self.buttonTimer += self.buttonSpeed

        Timer(self.buttonTimer + 2, self.showResults).start()

    def showResults(self):
        #avgTime = sum(self.clickTimes)/ len(self.clickTimes)
        fastestTime = round(min(self.clickTimes), 2)
        accuracy = int(self.buttonsClicked/10 * 100)
        alert = QMessageBox()
        alert.setText("Fastest time: " + str(fastestTime) + " Accuracy: " + str(accuracy) + "%")
        alert.exec_()

    def clickMethod(self, buttonChosen):
        endTime = time.perf_counter()
        self.clickTimes.append(endTime - self.startTime)
        self.startTime += self.buttonSpeed
        buttonChosen.setEnabled(False)
        buttonChosen.setStyleSheet("background-color: Darkred")
        self.buttonsClicked += 1
    
    def deactivateButton(self, pybutton):
        if pybutton.isEnabled():
            self.startTime += self.buttonSpeed
            pybutton.setEnabled(False)
            pybutton.setStyleSheet("background-color: Darkred")
        
    def activateButton(self, pybutton): 
        pybutton.setStyleSheet("background-color: green")
        pybutton.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(
        sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
