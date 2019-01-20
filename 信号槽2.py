import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QDial, QApplication, QLabel)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        #lcd = QLCDNumber(self)#led
        #dial = QDial(self)#旋钮

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('学点编程吧')

        #lcd.setGeometry(100,50,150,60)
        #dial.setGeometry(120,120,100,100)
        self.lab = QLabel('方向', self)
        self.lab.setGeometry(150, 100, 50, 50)

        #dial.valueChanged.connect(lcd.display)#旋钮的数值连接到led显示

        self.show()

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Up:#e.key()按键输入==qt按键代码
            self.lab.setText('↑')
        elif e.key() == Qt.Key_Down:
            self.lab.setText('↓')
        elif e.key() == Qt.Key_Left:
            self.lab.setText('←')
        else:
            self.lab.setText('→')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())