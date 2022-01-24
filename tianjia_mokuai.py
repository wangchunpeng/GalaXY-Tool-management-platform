# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tianjia.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import json
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(QtWidgets.QMainWindow):


    def tickaa(self):
        with open("./config/config.json","r",encoding='UTF-8') as file:
            # tt = file.read()
            # text = tt.decode("gbk").encode("utf-8")
            data = json.load(file)  #config文件的配置信息转字典
        print(self.lineEdit.text())
        data[self.lineEdit.text()] = {}

        with open("./config/config.json","w",encoding='UTF-8') as file:
            json.dump(data, file)
        sys.exit()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(609, 262)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 15, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 65, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 115, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 15, 230, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 180, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 609, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Pictures/Saved Pictures/165135-16321278956369.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.tickaa)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "天河平台"))
        self.label.setText(_translate("MainWindow", "模块名称："))
        self.pushButton.setText(_translate("MainWindow", "确定并重启软件"))
        with open("./config/config.json","r",encoding='UTF-8') as file:
            # tt = file.read()
            # text = tt.decode("gbk").encode("utf-8")
            data = json.load(file)  #config文件的配置信息转字典

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_zhuye = Ui_MainWindow()
    ui_zhuye.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())