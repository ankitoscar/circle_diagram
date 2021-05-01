import sys 
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QWidget
from mainWindow import * 
from calculatedValues import *
import numpy as np  

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.launchPopUp)
        self.show()

    def launchPopUp(self):
        pop = Popup(self)
        pop.displayValues()
        pop.show()   


class Popup(QDialog):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.parent = parent
        self.ui.setupUi(self)
        self.show()
    
    def displayValues(self):
        pfA = self.parent.ui.lineEdit_3.text()
        pfB = self.parent.ui.lineEdit_4.text()

        phi_A = round(np.arccos(np.float(pfA)) * 180 / np.pi, 2)
        phi_B = round(np.arccos(np.float(pfB)) * 180 / np.pi, 2)

        phi_A_value = self.ui.label.text()
        phi_B_value = self.ui.label_2.text()
        self.ui.label.setText(phi_A_value + str(phi_A))
        self.ui.label_2.setText(phi_B_value + str(phi_B))
if __name__=="__main__":

    app = QApplication(sys.argv)
    f = Window()
    f.show()
    sys.exit(app.exec_())