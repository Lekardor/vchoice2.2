# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '登录界面.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.setWindowModality(QtCore.Qt.NonModal)
        widget.resize(525, 316)
        widget.setMinimumSize(QtCore.QSize(525, 316))
        widget.setMaximumSize(QtCore.QSize(525, 316))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        widget.setFont(font)
        widget.setMouseTracking(False)
        widget.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"border:1px solid;\n"
"border-color: rgb(61, 61, 61);")
        self.loginButton = QtWidgets.QPushButton(widget)
        self.loginButton.setGeometry(QtCore.QRect(150, 210, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("*{\n"
"    color: rgb(255, 255, 255);\n"
"    border: rgb(65, 173, 255);\n"
"    background-color: rgb(255, 200, 1);\n"
"}")
        self.loginButton.setObjectName("loginButton")
        self.label = QtWidgets.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(70, 140, 79, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(198, 198, 198);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(widget)
        self.label_2.setGeometry(QtCore.QRect(70, 180, 79, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(198, 198, 198);")
        self.label_2.setObjectName("label_2")
        self.registerButton = QtWidgets.QPushButton(widget)
        self.registerButton.setGeometry(QtCore.QRect(392, 140, 68, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("color: rgb(255, 200, 1);\n"
"border: rgb(61, 61, 61);")
        self.registerButton.setObjectName("registerButton")
        self.findBackButton = QtWidgets.QPushButton(widget)
        self.findBackButton.setGeometry(QtCore.QRect(390, 180, 68, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.findBackButton.setFont(font)
        self.findBackButton.setStyleSheet("color: rgb(255, 200, 1);\n"
"border: rgb(61, 61, 61);")
        self.findBackButton.setObjectName("findBackButton")
        self.label_3 = QtWidgets.QLabel(widget)
        self.label_3.setGeometry(QtCore.QRect(150, 40, 221, 71))
        self.label_3.setStyleSheet("\n"
"image: url(:/new/prefix1/source/picture/背景灰.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(widget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 280, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("\n"
"color: rgb(184, 184, 184);\n"
"\n"
"border: rgb(61, 61, 61);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(widget)
        self.lineEdit.setGeometry(QtCore.QRect(147, 137, 231, 31))
        self.lineEdit.setStyleSheet("border:1px solid;\n"
"border-color: rgb(61, 61, 61);\n"
"background-color: rgb(38, 38, 38);\n"
"color: rgb(240, 240, 240)")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(147, 171, 231, 31))
        self.lineEdit_2.setStyleSheet("border:1px solid;\n"
"border-color: rgb(61, 61, 61);\n"
"background-color: rgb(38, 38, 38);\n"
"rgb: rgb(240, 240, 240)")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_5 = QtWidgets.QPushButton(widget)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 280, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("\n"
"color: rgb(184, 184, 184);\n"
"\n"
"border: rgb(61, 61, 61);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label.setBuddy(self.lineEdit)
        self.label_2.setBuddy(self.lineEdit_2)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)
        widget.setTabOrder(self.lineEdit, self.lineEdit_2)
        widget.setTabOrder(self.lineEdit_2, self.loginButton)
        widget.setTabOrder(self.loginButton, self.registerButton)
        widget.setTabOrder(self.registerButton, self.findBackButton)
        widget.setTabOrder(self.findBackButton, self.pushButton_4)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "登录"))
        self.loginButton.setText(_translate("widget", "登录"))
        self.label.setText(_translate("widget", "&用户账号"))
        self.label_2.setText(_translate("widget", "&用户密码"))
        self.registerButton.setText(_translate("widget", "注册账号"))
        self.findBackButton.setText(_translate("widget", "修改密码"))
        self.pushButton_4.setText(_translate("widget", "游客模式"))
        self.pushButton_5.setText(_translate("widget", "找回密码"))

import source_rc
