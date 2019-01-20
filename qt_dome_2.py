import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class Ico(QWidget):

   def __init__(self):
       super().__init__()
       self.initUI()#继承父类

   def initUI(self):

    self.setGeometry(300, 300, 300, 220)#创建窗口
    self.setWindowTitle(' ')
    self.setWindowIcon(QIcon('accuweather.png'))#图标

    qbtn = QPushButton('退出', self)#按钮
    qbtn.clicked.connect(QCoreApplication.instance().quit)#信号槽：外部函数是发送方，内部是接收方
    # 按钮发出被单击的信号，连接到退出程序的方法
    qbtn.resize(100, 100)
    qbtn.move(50, 50)

    self.show()
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Ico()
sys.exit(app.exec_())