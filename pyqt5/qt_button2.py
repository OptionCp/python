from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QFrame, QApplication)
from PyQt5.QtGui import QColor
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        self.col = QColor(0, 0, 0) #将QWidget 背景色设置为黑色
        redb = QPushButton('red', self)
        redb.setCheckable(True) #将按钮设置为切换按钮
        redb.move(10, 10)

        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100) #设置QWidget的位置
        self.square.setStyleSheet("QWidget {background-color:%s}" %self.col.name()) #使用样式表对背景颜色进行修改
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()
    
    def setColor(self, pressed):

    source = self.sender() #获取被点击的信息

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "red":
            self.col.setRed(val)
        elif source.text() == "green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        
        self.square.setStyleSheet("QFrame {background-color:%s}" %self.col.name())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
