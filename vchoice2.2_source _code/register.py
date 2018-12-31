# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '注册.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(410, 463)
        Form.setMinimumSize(QtCore.QSize(410, 463))
        Form.setMaximumSize(QtCore.QSize(410, 463))
        Form.setStyleSheet("background-color: rgb(61, 61, 61);")
        self.registerButton = QtWidgets.QPushButton(Form)
        self.registerButton.setGeometry(QtCore.QRect(90, 400, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("*{\n"
"    color: rgb(255, 255, 255);\n"
"    border: rgb(65, 173, 255);\n"
"    background-color: rgb(255, 200, 1);\n"
"}")
        self.registerButton.setObjectName("registerButton")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(101, 171, 211, 31))
        self.password.setStyleSheet("border:1px solid;\n"
"border-color: rgb(61, 61, 61);\n"
"background-color: rgb(38, 38, 38);\n"
"color: rgb(240, 240, 240)")
        self.password.setObjectName("password")
        self.passwordAgain = QtWidgets.QLineEdit(Form)
        self.passwordAgain.setGeometry(QtCore.QRect(100, 240, 211, 31))
        self.passwordAgain.setStyleSheet("border:1px solid;\n"
"border-color: rgb(61, 61, 61);\n"
"background-color: rgb(38, 38, 38);\n"
"color: rgb(240, 240, 240)")
        self.passwordAgain.setObjectName("passwordAgain")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(91, 11, 221, 71))
        self.label_4.setStyleSheet("\n"
"image: url(:/new/prefix1/source/picture/背景灰.png)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.account = QtWidgets.QLineEdit(Form)
        self.account.setGeometry(QtCore.QRect(99, 102, 211, 31))
        self.account.setStyleSheet("border:1px solid;\n"
"border-color: rgb(61, 61, 61);\n"
"background-color: rgb(38, 38, 38);\n"
"color: rgb(240, 240, 240)")
        self.account.setObjectName("account")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(31, 251, 60, 16))
        self.label_2.setStyleSheet("color: rgb(168, 168, 168);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(51, 181, 30, 16))
        self.label_3.setStyleSheet("color: rgb(168, 168, 168);")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(51, 111, 30, 16))
        self.label.setStyleSheet("color: rgb(168, 168, 168);")
        self.label.setObjectName("label")
        self.nameifo = QtWidgets.QLabel(Form)
        self.nameifo.setGeometry(QtCore.QRect(101, 141, 201, 21))
        self.nameifo.setStyleSheet("color: rgb(255, 200, 1);")
        self.nameifo.setText("")
        self.nameifo.setObjectName("nameifo")
        self.passwordinfo = QtWidgets.QLabel(Form)
        self.passwordinfo.setGeometry(QtCore.QRect(101, 211, 201, 21))
        self.passwordinfo.setStyleSheet("color: rgb(255, 200, 1);")
        self.passwordinfo.setText("")
        self.passwordinfo.setObjectName("passwordinfo")
        self.passwordAinfo = QtWidgets.QLabel(Form)
        self.passwordAinfo.setGeometry(QtCore.QRect(101, 271, 201, 21))
        self.passwordAinfo.setStyleSheet("color: rgb(255, 200, 1);")
        self.passwordAinfo.setText("")
        self.passwordAinfo.setObjectName("passwordAinfo")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(100, 300, 211, 31))
        self.comboBox.setStyleSheet("color: rgb(240, 240, 240);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 310, 60, 16))
        self.label_5.setStyleSheet("color: rgb(168, 168, 168);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(60, 360, 31, 16))
        self.label_6.setStyleSheet("color: rgb(168, 168, 168);")
        self.label_6.setObjectName("label_6")
        self.passwordAgain_2 = QtWidgets.QLineEdit(Form)
        self.passwordAgain_2.setGeometry(QtCore.QRect(100, 350, 211, 31))
        self.passwordAgain_2.setStyleSheet("border:1px solid;\n"
"border-color: rgb(61, 61, 61);\n"
"background-color: rgb(38, 38, 38);\n"
"color: rgb(240, 240, 240)")
        self.passwordAgain_2.setObjectName("passwordAgain_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "注册"))
        self.registerButton.setText(_translate("Form", "注册"))
        self.label_2.setText(_translate("Form", "确认密码"))
        self.label_3.setText(_translate("Form", "密码"))
        self.label.setText(_translate("Form", "账号"))
        self.comboBox.setItemText(0, _translate("Form", "你的英文名"))
        self.comboBox.setItemText(1, _translate("Form", "你的生日"))
        self.label_5.setText(_translate("Form", "密保问题"))
        self.label_6.setText(_translate("Form", "答案"))

import source_rc
