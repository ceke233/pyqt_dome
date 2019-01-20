import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication,QPushButton,QHBoxLayout,QApplication,QVBoxLayout
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.initUI()


    def initUI(self):
        self.resize(1200, 600)
        self.setStyleSheet("background-color:grey")
        self.center()
        btn1 = QPushButton("关闭", self)
        btn1.clicked.connect(self.close)
        btn2 = QPushButton("最小化", self)
        btn2.clicked.connect(self.showMinimized)
        btn3 = QPushButton("最大化", self)
        btn3.clicked.connect(self.showMaximized)

        hbox1 = QHBoxLayout()
        hbox1.addStretch()
        hbox1.addWidget(btn1)
        hbox1.addWidget(btn2)
        hbox1.addWidget(btn3)

        vbox1=QVBoxLayout()
        vbox1.addLayout(hbox1)
        vbox1.addStretch()
        self.setLayout(vbox1)


        self.show()

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())