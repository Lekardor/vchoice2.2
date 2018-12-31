# pyuic5 -o destination.py source.ui ui转py
import time
from PyQt5 import QtWidgets,uic,QtCore,QtGui
from login import Ui_widget
from register import Ui_Form
from changeCode import Ui_codeChange
from findBack import Ui_findBack
from source.userRecorde.userRecord import UserAdminister

from mainWin import *
from controlWin import controlWidget
from random import sample
import string

from PyQt5.QtCore import Qt, qrand, QPointF, QPoint, QBasicTimer
from PyQt5.QtGui import QPainter, QBrush, QPen, QPalette, QFontMetrics
from PyQt5.QtWidgets import QLabel

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QLineEdit



DEF_NOISYPOINTCOUNT = 60  # 噪点数量
COLORLIST = ("black", "gray", "red", "green", "blue", "magenta")
TCOLORLIST = (Qt.black, Qt.gray, Qt.red, Qt.green, Qt.blue, Qt.magenta)
QTCOLORLIST = (Qt.darkGray, Qt.darkRed, Qt.darkGreen, Qt.darkBlue, Qt.darkMagenta)
HTML = "<html><body>{html}</body></html>"
FONT = "<font color=\"{color}\">{word}</font>"
WORDS = list(string.ascii_letters + string.digits)
SINETABLE = (0, 38, 71, 92, 100, 92, 71, 38, 0, -38, -71, -92, -100, -92, -71, -38)
# MainWindowForm, MainWindowBase = uic.loadUiType(qtCreatorFile)


class testWindow(QtWidgets.QWidget, Ui_widget):
    def __init__(self):
        super(testWindow, self).__init__()

        self.setWindowTitle("Vchoice")
        self.setWindowIcon(QtGui.QIcon('./image/flash.ico'))
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('''background-color:cyan;''')
        self.setupUi(self)
        self.adminster = UserAdminister()

        self.m_flag = False

        self.child = childwindow(self.adminster)
        self.registerButton.clicked.connect(self.child.show)
        self.child2 = codeChangewindow(self.adminster)
        self.findBackButton.clicked.connect(self.child2.show)
        self.child3 = findBackwindow(self.adminster)
        self.pushButton_5.clicked.connect(self.child3.show)

        self.loginButton.clicked.connect(self.login)
        self.pushButton_4.clicked.connect(self.passengerLogin)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.returnPressed.connect(self.login)



    def passengerLogin(self):
        time.localtime(time.time())
        self.date = time.strftime('%Y_%m_%d', time.localtime(time.time()))
        self.close()
        w = LeftTabWidget(233, self.date, 2)
        w.show()
        if w.exec_():
            self.show()





    def login(self):
        self.adminster = self.child.adminster
        self.child.adminster.flesh
        if len(self.lineEdit.text()) == 0:
            QtWidgets.QMessageBox.information(self, '提示信息', "<font size='6' color='#f0f0f0'>账号不能为空</font>")
        elif len(self.lineEdit_2.text()) == 0:
            QtWidgets.QMessageBox.information(self, '提示信息', "<font size='6' color='#f0f0f0'>密码不能为空</font>")
        else:
            self.hide()
            QFontDatabase.addApplicationFont("itckrist.ttf")
            self.varifyWin = QWidget()
            self.setWindowTitle("请输入验证码")
            layout = QHBoxLayout(self.varifyWin)
            self.cwidget = WidgetCode(self.varifyWin, minimumHeight=35, minimumWidth=80)
            layout.addWidget(self.cwidget)
            self.varifylineEdit = QLineEdit(self.varifyWin, maxLength=4, placeholderText="请输入验证码并按回车验证")
            self.varifylineEdit.returnPressed.connect(self.codematching)
            layout.addWidget(self.varifylineEdit)
            self.varifyWin.show()


    def codematching(self):
        self.cwidget.check(self.varifylineEdit.text())
        if self.cwidget.checkRight:
            userName = self.lineEdit.text()
            password = self.lineEdit_2.text()
            allow = self.adminster.logIn(userName, password)
            if allow:
                QtWidgets.QMessageBox.information(self, '提示信息', "<font size='6' color='#f0f0f0'>登录成功！</font>")
                time.localtime(time.time())
                self.date = time.strftime('%Y_%m_%d', time.localtime(time.time()))
                self.close()
                self.varifyWin.close()
                w = LeftTabWidget(self.adminster.id, self.date, 1)
                w.show()
                if w.exec_():
                    self.show()
            else:
                QtWidgets.QMessageBox.information(self, '提示信息', "<font size='6' color='#f0f0f0'>账号或密码错误！</font>")
                self.varifyWin.close()
                self.show()
        else:
            QtWidgets.QMessageBox.information(self, '提示信息', "<font size='6' color='#f0f0f0'>验证码错误！</font>")





class childwindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self,adminster):
        super(childwindow, self).__init__()
        self.setWindowTitle("注册")
        self.setWindowIcon(QtGui.QIcon('./image/flash.ico'))
        self.setupUi(self)
        self.nameLegal = False
        self.passwordLegal = False
        self.passwordRight = False
        self.adminster = adminster

        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordAgain.setEchoMode(QtWidgets.QLineEdit.Password)
        self.account.editingFinished.connect(self.nameLegalJudge)
        self.password.editingFinished.connect(self.passwordLegalJudge)
        self.passwordAgain.editingFinished.connect(self.passwordMatching)
        self.registerButton.clicked.connect(self.regIn)

        self.account.setToolTip("用户名必须为数字或英文字母，长度在6-10之间")
        self.password.setToolTip("密码长度必须大于6小于20")
        self.passwordAgain.setToolTip("两次密码必须相同")

    def nameLegalJudge(self):
        userName = self.account.text()
        if 0 == len(userName):
            self.nameifo.setText("请输入用户名")

            self.nameLegal = False
        elif (not userName.isalnum()) or len(userName) < 5 or len(userName) > 11:
            self.nameifo.setText("用户名不合法")

            self.nameLegal = False

        elif self.adminster.usernameRepeatJudge(userName):
            self.nameifo.setText("用户名已被使用")

            self.nameLegal = False

        else:
            self.nameifo.setText("(๑•̀ㅂ•́)و✧")
            self.nameLegal = True


    def passwordLegalJudge(self):
        password = self.password.text()
        if self.nameLegal:
            if 0 == len(password):
                self.passwordinfo.setText("请输入密码")
                self.passwordLegal = False
            elif len(password) < 6:
                self.passwordinfo.setText("密码安全性太低")

                self.passwordLegal = False
            elif len(password) > 20:
                self.passwordinfo.setText("密码过长")

                self.passwordLegal = False
            else:
                self.passwordinfo.setText("φ(≧ω≦*)♪")
                self.passwordLegal = True
        else:
            self.passwordinfo.setText("")
            self.passwordLegal = False

    def passwordMatching(self):
        password = self.password.text()
        passwordAgain = self.passwordAgain.text()

        if self.nameLegal:
            if password != passwordAgain:
                self.passwordAinfo.setText("两次密码不一致")

                self.passwordRight = False
            elif self.passwordLegal:
                self.passwordAinfo.setText("(～￣▽￣)～")
                self.passwordRight = True
        else:
            self.passwordAinfo.setText("")
            self.passwordLegal = False

    def regIn(self):
        if not self.nameLegal:
            QtWidgets.QMessageBox.information(self, '提示信息', '请重新输入用户名')
        else:
            if not self.passwordLegal:
                QtWidgets.QMessageBox.information(self, '提示信息', '请重新密码')
            else:
                if not self.passwordRight:
                    QtWidgets.QMessageBox.information(self, '提示信息', '两次密码不一致')
                elif len(self.passwordAgain_2.text()) == 0:
                    QtWidgets.QMessageBox.information(self, '提示信息', '你没有输入问题')
                else:
                    self.adminster.dataIn(self.account.text(),self.password.text(),self.comboBox.currentText(),self.passwordAgain_2.text())
                    QtWidgets.QMessageBox.information(self, '提示信息', "<font size='30' color='#f0f0f0'>注册成功！</font>")
                    self.close()

    def closeEvent(self, event):
        self.account.clear()
        self.password.clear()
        self.passwordAgain.clear()
        self.nameifo.clear()
        self.passwordinfo.clear()
        self.passwordAinfo.clear()
        event.accept()
class codeChangewindow(QtWidgets.QWidget,Ui_codeChange):
    def __init__(self,adminster):
        super(codeChangewindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("密码修改")
        self.setWindowIcon(QtGui.QIcon('./image/flash.ico'))
        self.allow = False
        self.passwordLegal = False
        self.adminster = adminster

        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordAgain.setEchoMode(QtWidgets.QLineEdit.Password)
        self.account.editingFinished.connect(self.nameLegalJudge)
        self.password.editingFinished.connect(self.passwordRight)
        self.passwordAgain.editingFinished.connect(self.passwordLegalJudge)
        self.registerButton.clicked.connect(self.changeIn)

        self.passwordAgain.setToolTip("密码长度必须大于6小于20")

    def nameLegalJudge(self):
        userName = self.account.text()
        password = self.password.text()
        if 0 == len(userName):
            self.nameifo.setText("请输入用户名")
            self.allow = False
        else:
            self.nameifo.setText("(๑•̀ㅂ•́)و✧")
            if 0 != len(password):
                self.allow = self.adminster.logIn(userName, password)


    def passwordRight(self):
        userName = self.account.text()
        password = self.password.text()
        if 0 == len(password):
            self.passwordinfo.setText("请输入密码")
            self.allow = False
        else:
            self.allow = self.adminster.logIn(userName, password)
            if self.allow:
                self.passwordinfo.setText("φ(≧ω≦*)♪")
            else:
                self.passwordinfo.setText("密码错误")




    def passwordLegalJudge(self):
        password = self.passwordAgain.text()
        if self.allow:
            if 0 == len(password):
                self.passwordAinfo.setText("请输入密码")
                self.passwordLegal = False
            elif len(password) < 6:
                self.passwordAinfo.setText("密码安全性太低")

                self.passwordLegal = False
            elif len(password) > 20:
                self.passwordAinfo.setText("密码过长")

                self.passwordLegal = False
            else:
                self.passwordAinfo.setText("φ(≧ω≦*)♪")
                self.passwordLegal = True
        else:
            self.passwordAinfo.setText("")
            self.passwordLegal = False


    def changeIn(self):
        if self.allow:
            if self.passwordLegal:
                self.adminster.codeChange(self.passwordAgain.text())
                QtWidgets.QMessageBox.information(self, '提示信息', "<font size='30' color='#f0f0f0'>修改成功！</font>")
                self.close()
            else:
                QtWidgets.QMessageBox.information(self, '提示信息', "<font size='30' color='#f0f0f0'>密码不合法！</font>")
        else:
            QtWidgets.QMessageBox.information(self, '提示信息', "<font size='30' color='#f0f0f0'>账号或密码错误！</font>")
    def closeEvent(self, event):
        self.account.clear()
        self.password.clear()
        self.passwordAgain.clear()
        self.nameifo.clear()
        self.passwordinfo.clear()
        self.passwordAinfo.clear()
        event.accept()



class findBackwindow(QtWidgets.QWidget,Ui_findBack):
    def __init__(self,adminster):
        super(findBackwindow, self).__init__()
        self.setWindowTitle("找回密码")
        self.setWindowIcon(QtGui.QIcon('./image/flash.ico'))
        self.setupUi(self)
        self.allow = False
        self.passwordLegal = False
        self.adminster = adminster

        self.passwordAgain.setEchoMode(QtWidgets.QLineEdit.Password)
        self.account.editingFinished.connect(self.nameLegalJudge)
        self.passwordAgain.editingFinished.connect(self.passwordLegalJudge)
        self.registerButton.clicked.connect(self.changeIn)
        self.passwordAgain.setToolTip("密码长度必须大于6小于20")

    def nameLegalJudge(self):
        userName = self.account.text()
        if 0 == len(userName):
            self.nameifo.setText("请输入用户名")
            self.allow = False
        elif self.adminster.isExit(userName) == False:
            self.nameifo.setText("用户不存在")
            self.allow = False
        else:
            self.nameifo.setText("(๑•̀ㅂ•́)و✧")
            self.allow = True





    def passwordLegalJudge(self):
        password = self.passwordAgain.text()
        if self.allow:
            if 0 == len(password):
                self.passwordAinfo.setText("请输入密码")
                self.passwordLegal = False
            elif len(password) < 6:
                self.passwordAinfo.setText("密码安全性太低")

                self.passwordLegal = False
            elif len(password) > 20:
                self.passwordAinfo.setText("密码过长")

                self.passwordLegal = False
            else:
                self.passwordAinfo.setText("φ(≧ω≦*)♪")
                self.passwordLegal = True
        else:
            self.passwordAinfo.setText("")
            self.passwordLegal = False


    def changeIn(self):
        if not self.allow:
            QtWidgets.QMessageBox.information(self, '提示信息', "<font size='30' color='#f0f0f0'>账号不存在！</font>")
        elif not self.passwordLegal:
            QtWidgets.QMessageBox.information(self, '提示信息', "<font size='30' color='#f0f0f0'>密码不合法！</font>")
        elif not self.adminster.findback(self.account.text(),self.comboBox.currentText(),self.passwordAgain_2.text()):
            QtWidgets.QMessageBox.information(self, '提示信息', "<font size='30' color='#f0f0f0'>回答错误！</font>")
        else:
            self.adminster.codeChange(self.passwordAgain.text())
            self.close()
            QtWidgets.QMessageBox.information(self, '提示信息', "<font size='30' color='#f0f0f0'>成功</font>")



    def closeEvent(self, event):
        self.account.clear()
        self.passwordAgain.clear()
        self.passwordAgain_2.clear()
        self.nameifo.clear()
        self.passwordAinfo.clear()
        event.accept()






class WidgetCode(QLabel):

    def __init__(self, *args, **kwargs):
        super(WidgetCode, self).__init__(*args, **kwargs)
        self.setWindowTitle("验证码")
        self.setWindowIcon(QtGui.QIcon('./image/flash.ico'))
        self.checkRight = False
        self.changed = False
        self._sensitive = False  # 是否大小写敏感
        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setBackgroundRole(QPalette.Midlight)
        self.setAutoFillBackground(True)
        # 字体

        newFont = self.font()
        newFont.setPointSize(16)
        newFont.setFamily("Kristen ITC")
        newFont.setBold(True)
        self.setFont(newFont)
        self.reset()
        # 定时器
        self.step = 0
        self.timer = QBasicTimer()
        self.timer.start(60, self)

    def reset(self):
        self._code = "".join(sample(WORDS, 4))  # 随机4个字符
        self.setText(self._code)

    def check(self, code):
        self.checkRight =  self._code == str(code) if self._sensitive else self._code.lower() == str(code).lower()
        self.changed = True

    def setSensitive(self, sensitive):
        self._sensitive = sensitive


    def mouseReleaseEvent(self, event):
        super(WidgetCode, self).mouseReleaseEvent(event)
        self.reset()

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.step += 1
            return self.update()
        return super(WidgetCode, self).timerEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        # 背景白色
        painter.fillRect(event.rect(), QBrush(Qt.white))
        # 绘制边缘虚线框
        painter.setPen(Qt.DashLine)
        painter.setBrush(Qt.NoBrush)
        painter.drawRect(self.rect())
        # 随机画条线
        for _ in range(3):
            painter.setPen(QPen(QTCOLORLIST[qrand() % 5], 1, Qt.SolidLine))
            painter.setBrush(Qt.NoBrush)
            painter.drawLine(QPoint(0, qrand() % self.height()),
                             QPoint(self.width(), qrand() % self.height()))
            painter.drawLine(QPoint(qrand() % self.width(), 0),
                             QPoint(qrand() % self.width(), self.height()))
        # 绘制噪点
        painter.setPen(Qt.DotLine)
        painter.setBrush(Qt.NoBrush)
        for _ in range(self.width()):  # 绘制噪点
            painter.drawPoint(QPointF(qrand() % self.width(), qrand() % self.height()))
        # super(WidgetCode, self).paintEvent(event)  # 绘制文字
        # 绘制跳动文字
        metrics = QFontMetrics(self.font())
        x = (self.width() - metrics.width(self.text())) / 2
        y = (self.height() + metrics.ascent() - metrics.descent()) / 2
        for i, ch in enumerate(self.text()):
            index = (self.step + i) % 16
            painter.setPen(TCOLORLIST[qrand() % 6])
            painter.drawText(x, y - ((SINETABLE[index] * metrics.height()) / 400), ch)
            x += metrics.width(ch)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    test = UserAdminister()
    myshow = testWindow()
    myshow.show()
    sys.exit(app.exec_())