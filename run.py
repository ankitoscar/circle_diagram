import sys 
import os
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from mainWindow import * 
from calculatedValues import *
import numpy as np  
from plot import *

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.pressed.connect(self.launchPopUp)
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
        self.ui.pushButton.clicked.connect(self.launchDiagram)
        self.show()
    
    def displayValues(self):
        pfA = self.parent.ui.lineEdit_3.text()
        pfB = self.parent.ui.lineEdit_4.text()

        phi_A = round(np.arccos(np.float(pfA)) * 180 / np.pi, 2)
        phi_B = round(np.arccos(np.float(pfB)) * 180 / np.pi, 2)

        phi_A_value = self.ui.label.text()
        phi_B_value = self.ui.label_2.text()
        self.ui.label.setText(phi_A_value + str(phi_A) + ' degrees')
        self.ui.label_2.setText(phi_B_value + str(phi_B) + ' degrees')

        i_sc = self.parent.ui.lineEdit_6.text()
        i_o = self.parent.ui.lineEdit_2.text()

        v_o = self.parent.ui.lineEdit.text()
        v_sc =  self.parent.ui.lineEdit_5.text()
        
        i_sv = float(i_sc) * (float(v_o)/float(v_sc))

        w_sv = round(np.sqrt(3)*np.float(v_o)*i_sv*np.float(pfB), 2)

        self.ui.label_3.setText(self.ui.label_3.text() + str(i_sv) + ' A')
        self.ui.label_4.setText(self.ui.label_4.text() + str(w_sv) + ' W')

    def launchDiagram(self):
        os.system('python plot.py')
        

if __name__=="__main__":

    app = QApplication(sys.argv)
    f = Window()
    f.show()
    sys.exit(app.exec_())