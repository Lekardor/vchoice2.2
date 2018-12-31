

from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from source.userRecorde.userRecord import UserInf
from start import worker
import os








class controlWidget(QDialog):

    def __init__(self, id, date, authority = 1):
        super(controlWidget, self).__init__()
        self.id = id
        self.date = date
        self.authority = authority
        self.flag = False
        # 美化样式表
        self.setWindowFlags(Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint)
        self.setWindowTitle("Vchoice")
        self.setWindowIcon(QtGui.QIcon('./image/flash.ico'))
        self.Stylesheet = """
        QListWidget, QListView, QTreeWidget, QTreeView {
            outline: 0px;
        }
        QListWidget {
            min-width: 120px;
            max-width: 120px;
            color: white;
            background: rgb(61,61,61);
        }
        QListWidget::item:selected {
            background: rgb(52, 52, 52);
            border-left: 2px solid rgb(255, 200, 1);
        }

        HistoryPanel::item:hover {
            background: rgb(52, 52, 52);
        }


        QStackedWidget {
            background-image: url(:/new/prefix1/source/picture/极简灰白微立体通用PPT模板2.png);
        }
        QPushButton#loginButton {
            color: white;
            background-color: black;
        }
        #loginButton:hover {
            background-color: rgb(255, 200, 1);
        }
        #loginButton:pressed {
            background-color: #e57373;
        }

        """


        self.setStyleSheet(self.Stylesheet)
        self.resize(1000, 843)

        layout =QVBoxLayout(self, spacing=0)
        childLayout = QHBoxLayout(self, spacing=0)

        childLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self)
        childLayout.addWidget(self.listWidget)

        self.stackedWidget = QStackedWidget(self)

        # self.stackedWidget.setStyleSheet("background: rgb(61, 61, 61);")
        childLayout.addWidget(self.stackedWidget)

        headLayout = QHBoxLayout(self, spacing=0)
        headLayout.setContentsMargins(0, 0, 0, 0)

        logal = QLabel()
        logal.setStyleSheet("image: url(:/new/prefix1/source/picture/稿定设计导出-20181211-154931.png); background-color: black")
        logal.setAlignment(Qt.AlignLeft)
        logal.setScaledContents(True)
        logal.setMinimumSize(130,40)
        logal.setMaximumSize(130,40)

        black = QLabel('')
        black.setStyleSheet("background-color: black;")


        black.setText('管理模式')
        black.setStyleSheet('color : white; background-color: black;font: 14pt \"黑体\"')

        # if self.authority == 2:
        #     loginButton = QPushButton("立即登录",objectName="loginButton")
        # else:
        #     loginButton = QPushButton("注销", objectName="loginButton")
        # loginButton.setMaximumSize(130,40)
        # loginButton.clicked.connect(self.login)
        headLayout.addWidget(logal)
        headLayout.addWidget(black)
        # headLayout.addWidget(loginButton)


        layout.setContentsMargins(0, 0, 0, 0)
        layout.addLayout(headLayout)
        layout.addLayout(childLayout)

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()


        self.stack1UI()
        self.stack2UI()
        self.stack3UI()


        self.stackedWidget.addWidget(self.stack1)
        self.stackedWidget.addWidget(self.stack2)
        self.stackedWidget.addWidget(self.stack3)


        self.initUi()

    # def login(self):
    #     self.accept()
    #     self.close()
    #     return True




    def closeEvent(self, event):

        reply = QMessageBox.question(self, '警告', '你确认要退出吗？',
                                               QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        # self.reject



    def initUi(self):

        self.listWidget.currentRowChanged.connect(
            self.stackedWidget.setCurrentIndex)

        self.listWidget.setFrameShape(QListWidget.NoFrame)

        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)



        item = QListWidgetItem(str('用户管理'), self.listWidget)
        item.setSizeHint(QSize(16777215, 60))
        item.setTextAlignment(Qt.AlignCenter)

        item = QListWidgetItem(str('爬虫管理'), self.listWidget)
        item.setSizeHint(QSize(16777215, 60))
        item.setTextAlignment(Qt.AlignCenter)

        item = QListWidgetItem(str('数据下载'), self.listWidget)
        item.setSizeHint(QSize(16777215, 60))
        item.setTextAlignment(Qt.AlignCenter)


    def stack1UI(self):
        self.layout1 = QFormLayout()
        timeLayout = QHBoxLayout()
        namelabel = QLabel("账户名称", self)
        namelabel.setAlignment(Qt.AlignCenter)
        namelabel.setMaximumSize(100,30)
        namelabel.setStyleSheet('font: 10pt \"黑体\"')
        timeLayout.addWidget(namelabel)

        self.nameLine = QLineEdit()
        self.nameLine.setMaximumSize(150, 50)
        timeLayout.addWidget(self.nameLine)

        button = QPushButton('显示密码', self)
        button.setMaximumSize(120,50)
        button.clicked.connect(self.userExist)
        timeLayout.addWidget(button)

        self.passwordLabel = QLabel()
        self.passwordLabel.setAlignment(Qt.AlignCenter)
        self.passwordLabel.setMaximumSize(100, 30)
        self.passwordLabel.setStyleSheet('font: 10pt \"黑体\"')
        timeLayout.addWidget(self.passwordLabel)

        self.layout1.addRow(timeLayout)

        self.stack1.setLayout(self.layout1)

    def stack1UI_new(self):
        Layout2 = QHBoxLayout()
        label = QLabel("信息修改", self)
        label.setAlignment(Qt.AlignCenter)
        label.setMaximumSize(100, 30)
        label.setStyleSheet('font: 10pt \"黑体\"')
        Layout2.addWidget(label)

        label = QLabel("密码", self)
        label.setAlignment(Qt.AlignCenter)
        label.setMaximumSize(50, 30)
        label.setStyleSheet('font: 10pt \"黑体\"')
        Layout2.addWidget(label)

        self.passwordLine = QLineEdit()
        self.passwordLine.setMaximumSize(150, 50)
        Layout2.addWidget(self.passwordLine)

        button = QPushButton('确定', self)
        button.setMaximumSize(120, 50)
        button.clicked.connect(self.userPasswordChange)
        Layout2.addWidget(button)

        label = QLabel("密保问题", self)
        label.setAlignment(Qt.AlignCenter)
        label.setMaximumSize(100, 30)
        label.setStyleSheet('font: 10pt \"黑体\"')
        Layout2.addWidget(label)

        self.question = QComboBox()
        self.question.addItems(["你的英文名","你的生日"])
        self.question.setMaximumSize(150, 30)
        Layout2.addWidget(self.question)

        label = QLabel("答案", self)
        label.setAlignment(Qt.AlignCenter)
        label.setMaximumSize(50, 30)
        label.setStyleSheet('font: 10pt \"黑体\"')
        Layout2.addWidget(label)

        self.answerLine = QLineEdit()
        self.answerLine.setMaximumSize(150, 50)
        Layout2.addWidget(self.answerLine)

        button = QPushButton('确定', self)
        button.setMaximumSize(120, 50)
        button.clicked.connect(self.userQuestionChange)
        Layout2.addWidget(button)
        self.layout1.addRow(Layout2)
    def userExist(self):
        userName = self.nameLine.text()
        if len(userName) == 0:
            QMessageBox.information(self, '提示信息', "<font size='30' color='#f0f0f0'>账户名不能为空！</font>")
            self.passwordLabel.setText('')
        else:
            new = UserInf()
            if new.retrievePassword(userName) != False:
                self.passwordLabel.setText(new.retrievePassword(userName))
                if self.flag == False:
                    self.stack1UI_new()
                    self.flag = True
            else:
                QMessageBox.information(self, '提示信息', "<font size='30' color=black>用户不存在</font>")
            del new
    def userPasswordChange(self):
        userName = self.nameLine.text()
        password = self.passwordLine.text()
        if len(password) < 6 and len(password > 20):
            QMessageBox.information(self, '提示信息', "<font size='30' color=black>密码不合法</font>")
        elif len(userName) == 0:
            QMessageBox.information(self, '提示信息', "<font size='30' color=black>账户名不能为空！</font>")
        else:
            new = UserInf()
            if new.changePassword(userName,password):
                self.passwordLabel.setText(password)
                QMessageBox.information(self, '提示信息', "<font size='30' color=black>修改成功！</font>")
            else:
                QMessageBox.information(self, '提示信息', "<font size='30' color=black>用户不存在</font>")
            del new

    def userQuestionChange(self):
        userName = self.nameLine.text()
        question = self.question.currentText()
        answer = self.answerLine.text()
        if len(answer) == 0:
            QMessageBox.information(self, '提示信息', "<font size='30' color=black>答案不合法！</font>")
        elif len(userName) == 0:
            QMessageBox.information(self, '提示信息', "<font size='30' color=black>账户名不能为空！</font>")
        else:
            new = UserInf()
            if new.changeQuestion(userName, question, answer):
                QMessageBox.information(self, '提示信息', "<font size='30' color=black>修改成功！</font>")
            else:
                QMessageBox.information(self, '提示信息', "<font size='30' color=black>用户不存在</font>")
            del new

    def stack2UI(self):
        layout = QFormLayout()
        timeLayout = QHBoxLayout()
        timeLayout2 = QHBoxLayout()
        label = QLabel("爬取网站", self)
        label.setAlignment(Qt.AlignCenter)
        label.setMaximumSize(100, 30)
        label.setStyleSheet('font: 15pt \"新宋体\"')
        timeLayout.addWidget(label)

        self.webBox = QComboBox()
        self.webBox.setMaximumSize(80, 50)
        # self.yearBox4.setStyleSheet('color: rgb(199, 199 ,199)')
        self.webBoxinf = ['猫眼', '百度']
        self.webBox.addItems(self.webBoxinf)
        timeLayout.addWidget(self.webBox)

        label = QLabel("爬取间隔", self)
        label.setAlignment(Qt.AlignCenter)
        label.setMaximumSize(100, 30)
        label.setStyleSheet('font: 15pt \"新宋体\"')
        timeLayout.addWidget(label)

        self.timeBox = QComboBox()
        self.timeBox.setMaximumSize(50, 50)
        # self.rankBox4.setStyleSheet('color: rgb(199, 199 ,199)')
        self.timeInfor = ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
        self.timeBox.addItems(self.timeInfor)
        timeLayout.addWidget(self.timeBox)

        label = QLabel("chromedriver地址", self)
        label.setAlignment(Qt.AlignCenter)
        label.setMaximumSize(220, 30)
        label.setStyleSheet('font: 15pt \"新宋体\"')
        timeLayout.addWidget(label)

        button = QPushButton('选择路径', self)
        button.setMaximumSize(70, 50)
        button.clicked.connect(self.addGet)
        timeLayout.addWidget(button)

        self.addLine = QLineEdit()
        self.addLine.setMaximumSize(150, 50)
        timeLayout2.addWidget(self.addLine)

        button = QPushButton('开始爬取', self)
        button.setMaximumSize(70, 50)
        button.clicked.connect(self.start)
        timeLayout2.addWidget(button)

        layout.addRow(timeLayout)
        layout.addRow(timeLayout2)
        self.stack2.setLayout(layout)

    def addGet(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), "exe (*.exe)")
        self.addLine.setText(fileName_choose)
    def start(self):
        web_to = {'猫眼': 'maoyan', '百度':'baidu'}
        web = web_to[self.webBox.currentText()]
        time = int(self.timeBox.currentText())
        path = self.addLine.text()
        worker(web,time,path)



    def stack3UI(self):
        layout = QFormLayout()
        timeLayout = QHBoxLayout()

        label = QLabel("打印用户数据", self)
        label.setAlignment(Qt.AlignCenter)
        label.setMaximumSize(150, 30)

        label.setStyleSheet('font: 12pt \"黑体\"')
        timeLayout.addWidget(label)

        button = QPushButton("确定", self)
        button.setMaximumSize(150, 50)
        # button.setStyleSheet('color: rgb(199,199,199)')
        button.clicked.connect(self.csvBuild)
        timeLayout.addWidget(button)

        layout.addRow(timeLayout)
        layout.addRow(QLabel())

        self.stack3.setLayout(layout)

    def csvBuild(self):
        fileName, ok = QFileDialog.getSaveFileName(self, "文件保存", "/", "csv(*.csv)")
        print(fileName)
        print(ok)
        if len(fileName):
            new = UserInf()
            new.downLoadUserInf(fileName)
            del new





import source_rc





if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = controlWidget(1, '2018_12_18', 0)

    w.show()
    sys.exit(app.exec_())