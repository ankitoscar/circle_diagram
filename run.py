import sys 
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QWidget
from mainWindow import * 

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.launchPopUp)
        self.show()

    def launchPopUp(self):
        pop = Popup(self)
        pop.show()   


class Popup(QDialog):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.resize(600, 300)
        self.label = QLabel('Pop Up Window', self)

if __name__=="__main__":

    app = QApplication(sys.argv)
    f = Window()
    f.show()
    sys.exit(app.exec_())