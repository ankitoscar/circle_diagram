import sys 

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow

from mainWindow import * 
from calculatedValues import *
from plot_diagram import *
import numpy as np  

import matplotlib 
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


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
        c = CircleDiagram(self)
        c.show()
        

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=9, height=9, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class CircleDiagram(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(CircleDiagram, self).__init__(*args, **kwargs)

        sc = MplCanvas(self, width=9, height=9)
        plot_circle_diagram(sc.axes)

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        

if __name__=="__main__":

    app = QApplication(sys.argv)
    f = Window()
    f.show()
    sys.exit(app.exec_())