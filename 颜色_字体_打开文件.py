from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QColorDialog, QFontDialog, QTextEdit, QFileDialog
#颜色选择对话框、字体选择对话框、打开文件对话框，QTextEdit则是将刚才提到的类的结果用于呈现。QTextEdit能够呈现富文本。
import sys
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--记得好看点')


        self.tx = QTextEdit(self)
        self.tx.setGeometry(20, 20, 300, 270)

        self.bt1 = QPushButton('打开文件',self)
        self.bt1.move(350,20)
        self.bt2 = QPushButton('选择字体',self)
        self.bt2.move(350,70)
        self.bt3 = QPushButton('选择颜色',self)
        self.bt3.move(350,120)

        self.bt1.clicked.connect(self.openfile)
        self.bt2.clicked.connect(self.choicefont)
        self.bt3.clicked.connect(self.choicecolor)

        self.show()
    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, '打开文件','./',('word(*.txt *.docx)'))
        #标题，指定工作目录，文件过滤器
        if fname[0]:
            with open(fname[0], 'r',encoding='gb18030',errors='ignore') as f:
                self.tx.setText(f.read())
    def choicefont(self):
        font, ok = QFontDialog.getFont()#弹出对话框，获取状态和信息
        if ok:
            self.tx.setCurrentFont(font)#改变字体
    def choicecolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.tx.setTextColor(col)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())