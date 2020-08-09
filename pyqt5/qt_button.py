import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

class Example(QWidget):
    
    def __init__(self):   
      
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'MessageBox', "are you sure to exit", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accpt()
        else:
            event.ignore()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
