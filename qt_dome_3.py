import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from random import randint

class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        self.num = randint(1,100)

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('猜数字')
        self.setWindowIcon(QIcon('accuweather.png'))

        self.bt1 = QPushButton('我猜', self)
        self.bt1.setGeometry(115, 150, 70, 30)
        self.bt1.setToolTip('<b>点击这里猜数字</b>')
        self.bt1.clicked.connect(self.showMessage)#点击执行弹窗函数

        self.text = QLineEdit('在这里输入数字', self)#输入框
        self.text.selectAll()#全选文字
        self.text.setFocus()#焦点文本框
        self.text.setGeometry(80, 50, 150, 30)#控件坐标和大小

        self.show()

    def showMessage(self):
        guessnumber = int(self.text.text())#获取输入
        if guessnumber > self.num:
            QMessageBox.about(self, '看结果', '猜大了!')#弹窗
            self.text.setFocus()
        elif guessnumber < self.num:
            QMessageBox.about(self, '看结果', '猜小了!')
            self.text.setFocus()
        else:
            QMessageBox.about(self, '看结果', '答对了!进入下一轮!')
            self.num = randint(1, 100)
            self.text.clear()#清空文本
            self.text.setFocus()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        #标题，文本内容，选项，默认选项
        if reply == QMessageBox.Yes:
            event.accept()#结束程序
        else:
            event.ignore()#忽视


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
