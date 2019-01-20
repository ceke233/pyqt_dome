from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp,QMenu
from PyQt5.QtGui import QIcon
import sys
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.statusBar().showMessage('准备就绪')#状态栏

        self.setGeometry(300,300,400,300)
        self.setWindowTitle('关注微信公众号：学点编程吧--简单的菜单')

        exitAct = QAction(QIcon('accuweather.png'), '退出(&E)', self)#创建动作
        exitAct.setShortcut('Ctrl+Q')#快捷键
        exitAct.setStatusTip('退出程序')#更新状态栏
        exitAct.triggered.connect(qApp.quit)#连接退出

        saveMenu = QMenu('保存方式(&S)', self)
        saveAct = QAction(QIcon('save.png'), '保存...', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('保存文件')
        saveasAct = QAction(QIcon('saveas.png'), '另存为...(&O)', self)
        saveasAct.setStatusTip('文件另存为')
        saveMenu.addAction(saveAct)#添加到子菜单
        saveMenu.addAction(saveasAct)

        newAct = QAction(QIcon('accuweather.png'), '新建(&N)', self)
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('新建文件')

        menubar = self.menuBar()  # 创建菜单栏
        fileMenu = menubar.addMenu('文件(&F)')  # 创建菜单
        fileMenu.addAction(exitAct)  # 添加菜单操作
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()

        toolbar = self.addToolBar('工具栏')#工具栏
        toolbar.addAction(newAct)
        toolbar.addAction(exitAct)

        self.show()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)#创建上下文菜单

        newAct = cmenu.addAction("新建")
        opnAct = cmenu.addAction("保存")
        quitAct = cmenu.addAction("退出")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))#显示上下文菜单并获取指针对应的部件
        if action == quitAct:
            qApp.quit()

        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())