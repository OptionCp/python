import sys 
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QApplication, QAction
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    
    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction(QIcon('icon/1.icon'), 'exit', self)
        exitAction.setShortcut('Ctrl+W')
        exitAction.setStatusTip('exit app')
        exitAction.triggered.connect(self.close)

        self.statusBar

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('file')
        fileMenu.addAction(exitAction)
        menubar.setNativeMenuBar(False)

        toolbar = self.addToolBar('exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('main')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())