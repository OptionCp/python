import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication

class Communicate(QObject):

        clossApp = pyqtSignal()

class Example(QMainWindow):

        def __init__(self):
            
            super().__init__()
            self.initUI()

        def initUI(self):

            self.c = Communicate()
            self.c.clossApp.connect(self.close)
            self.setGeometry(300,300,300,300)
            self.setWindowTitle('emit signal')
            self.show()
        
        def mousePressEvent(self, event):

            self.c.clossApp.emit()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
