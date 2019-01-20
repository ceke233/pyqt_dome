import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':#主函数入口
    app = QApplication(sys.argv)#创建应用对象
    try:
        if len(sys.argv) < 2:
            raise ValueError
        else:
            title = " ".join(sys.argv[1:])
    except ValueError:
        title = "123"
    w = QWidget()#主窗口
    w.resize(250, 150)#控件大小
    w.move(300, 300)#把控件移动到指定位置
    w.setWindowTitle(title)#窗口标题
    w.show()#显示主窗口

sys.exit(app.exec_())#结束窗口循环
