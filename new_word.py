import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget,QPushButton, QHBoxLayout, QApplication, QVBoxLayout, \
    QLabel,QComboBox
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.initUI()

    def initUI(self):
        self.resize(1200, 600)
        self.center()

        h1_btn1 = QPushButton("关闭", self)
        h1_btn1.clicked.connect(self.close)
        h1_btn2 = QPushButton("最小化", self)
        h1_btn2.clicked.connect(self.showMinimized)
        h1_btn3 = QPushButton("最大化", self)
        h1_btn3.clicked.connect(self.showMaximized)
        hbox1 = QHBoxLayout()
        hbox1.addStretch()
        hbox1.addWidget(h1_btn2)
        hbox1.addWidget(h1_btn3)
        hbox1.addWidget(h1_btn1)

        h2_btn1 = QPushButton("1", self)
        h2_btn2 = QPushButton("2", self)
        h2_btn3 = QPushButton("3", self)
        h2_lab1 = QLabel(self)
        h2_lab1.setText('123')
        h2_btn4 = QPushButton("4", self)
        h2_btn5 = QPushButton("5", self)
        h2_btn6 = QPushButton("6", self)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(h2_btn1)
        hbox2.addWidget(h2_btn2)
        hbox2.addWidget(h2_btn3)
        hbox2.addStretch()
        hbox2.addWidget(h2_lab1)
        hbox2.addStretch()
        hbox2.addWidget(h2_btn4)
        hbox2.addWidget(h2_btn5)
        hbox2.addWidget(h2_btn6)

        v1_btn1 = QPushButton("1", self)
        v1_btn2 = QPushButton("2", self)
        v1_btn3 = QPushButton("3", self)
        v1_btn4 = QPushButton("4", self)
        v1_btn5 = QPushButton("5", self)
        v1_btn6 = QPushButton("6", self)
        v1_btn7 = QPushButton("7", self)
        vbox1 = QVBoxLayout()
        vbox1.addWidget(v1_btn1)
        vbox1.addWidget(v1_btn2)
        vbox1.addWidget(v1_btn3)
        vbox1.addWidget(v1_btn4)
        vbox1.addWidget(v1_btn5)
        vbox1.addWidget(v1_btn6)
        vbox1.addWidget(v1_btn7)
        vbox1.addStretch()

        h3_btn1 = QPushButton("1", self)
        h4_btn2 = QPushButton("2", self)
        h3_btn3 = QPushButton("3", self)
        h3_btn4 = QPushButton("4", self)
        hbox3 = QHBoxLayout()
        hbox3.addWidget(h3_btn1)
        hbox3.addWidget(h4_btn2)
        hbox3.addWidget(h3_btn3)
        hbox3.addWidget(h3_btn4)

        h4_btn1 = QPushButton("1", self)
        h4_btn2 = QPushButton("2", self)
        h4_btn3 = QPushButton("3", self)
        h4_btn4 = QPushButton("4", self)
        h4_btn5 = QPushButton("5", self)
        hbox4 = QHBoxLayout()
        hbox4.addWidget(h4_btn1)
        hbox4.addWidget(h4_btn2)
        hbox4.addWidget(h4_btn3)
        hbox4.addWidget(h4_btn4)
        hbox4.addWidget(h4_btn5)

        h5_btn1 = QPushButton("1", self)
        h5_btn2 = QPushButton("2", self)
        h5_btn3 = QPushButton("3", self)
        h5_btn4 = QPushButton("4", self)
        h5_btn5 = QPushButton("5", self)
        hbox5 = QHBoxLayout()
        hbox5.addWidget(h5_btn1)
        hbox5.addWidget(h5_btn2)
        hbox5.addWidget(h5_btn3)
        hbox5.addWidget(h5_btn4)
        hbox5.addWidget(h5_btn5)

        self.h6_combobox1=QComboBox(self)
        self.h6_combobox2 = QComboBox(self)
        hbox6=QVBoxLayout()
        hbox6.addWidget(self.h6_combobox1)
        hbox6.addWidget(self.h6_combobox2)

        v2_lab=QLabel(self)
        v2_lab.setText('字体')
        self.v2_combobox=QComboBox(self)
        vbox2=QVBoxLayout()
        vbox2.addLayout(hbox3)
        vbox2.addWidget(v2_lab)
        vbox2.addWidget(self.v2_combobox)
        vbox2.addLayout(hbox6)
        vbox2.addLayout(hbox4)
        vbox2.addLayout(hbox5)
        vbox2.addStretch()

        hbox7=QHBoxLayout()
        hbox7.addLayout(vbox1)
        hbox7.addStretch()
        hbox7.addLayout(vbox2)




        main_vbox1 = QVBoxLayout()
        main_vbox1.addLayout(hbox1)
        main_vbox1.addLayout(hbox2)
        main_vbox1.addLayout(hbox7)
        main_vbox1.addStretch()
        self.setLayout(main_vbox1)

        self.show()

    # def mousePressEvent(self, event):
    #
    #     if event.button() == Qt.LeftButton:
    #         self.m_drag = True
    #         self.m_DragPosition = event.globalPos() - self.pos()
    #         event.accept()
    #
    # def mouseMoveEvent(self, QMouseEvent):
    #     if Qt.LeftButton and self.m_drag:
    #         self.move(QMouseEvent.globalPos() - self.m_DragPosition)
    #         QMouseEvent.accept()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
