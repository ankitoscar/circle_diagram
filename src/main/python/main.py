import sys 

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from mainWindow import * 
from calculatedValues import *
from plot_diagram import *
import numpy as np  

import matplotlib 
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

i_A = 0
i_B = 0
i_sc = 0
v_o = 0
v_sc = 0
pfA = 0
pfB = 0
x = 0
w_o = 0
w_sv = 0


class Window(QWidget):

    """
    Class for the main window where the inputs will be entered.
    """

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

    """
    Class for the popup which has intermediate values.
    """
    
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.parent = parent
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.launchDiagram)
        self.show()
    
    def displayValues(self):
        global pfA
        pfA = np.float(self.parent.ui.lineEdit_4.text())
        global pfB
        pfB = np.float(self.parent.ui.lineEdit_7.text())

        phi_A = round(np.arccos(pfA) * 180 / np.pi, 2)
        phi_B = round(np.arccos(pfB) * 180 / np.pi, 2)

        phi_A_value = self.ui.label.text()
        phi_B_value = self.ui.label_2.text()
        self.ui.label.setText(phi_A_value + str(phi_A) + ' degrees')
        self.ui.label_2.setText(phi_B_value + str(phi_B) + ' degrees')

        global i_sc
        i_sc = np.float(self.parent.ui.lineEdit_6.text())
        global i_A
        i_A = np.float(self.parent.ui.lineEdit_3.text())

        global v_o
        v_o = np.float(self.parent.ui.lineEdit_2.text())
        global v_sc
        v_sc = np.float(self.parent.ui.lineEdit_5.text())

        global x
        x = np.float(self.parent.ui.lineEdit_8.text())
        
        global i_B
        i_B = i_sc * (v_o/v_sc)

        global w_sv
        w_sv = round(np.sqrt(3)*v_o*i_B*pfB, 2)

        global w_o
        w_o = np.float(self.parent.ui.lineEdit.text())

        global w_sc

        self.ui.label_3.setText(self.ui.label_3.text() + str(i_B) + ' A')
        self.ui.label_4.setText(self.ui.label_4.text() + str(w_sv) + ' W')

    def launchDiagram(self):
        c = CircleDiagram(self)
        c.show()
        

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=15, height=9, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class CircleDiagram(QMainWindow):
    """
    Class for the window which has the circle diagram.
    """

    def __init__(self, *args, **kwargs):
        super(CircleDiagram, self).__init__(*args, **kwargs)

        sc = MplCanvas(self, width=15, height=9)
        plot_circle_diagram(sc.axes, i_A=i_A, i_B=i_B, pfA=pfA, pfB=pfB, w_o=w_o, w_sv=w_sv, x=0.5)
        

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
    appctxt = ApplicationContext()
    f = Window()
    f.show()
    sys.exit(appctxt.app.exec())