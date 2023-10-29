
import sys
import csv
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QStackedWidget ,QGridLayout,QMenuBar,QFileDialog, QVBoxLayout, QPushButton,QAction
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtGui import QFont, QIcon, QPixmap, QColor
from PyQt5.QtCore import Qt,QTimer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from OnlyInput import TextInputPage
from CircProgBar import CircularProgressBar
from statusBar import CircleWidget
from graph import CSVPlotterApp
from SensorData import SensorDisplay
from sidebarinput import Sidebar,SET_TIMEOUT,SIM_ACTIVATE,SIM_DEACTIVATE,SIM_ENABLE,CAL,CX_OFF,CX_ON
from titlebar import Color  # Import the title bar code
from graph import CSVPlotterApp

class MENU(QWidget):

    openCSVSignal = pyqtSignal()

    def __init__(self, CSVPlotterApp):
        QWidget.__init__(self)
        self.CSVPlotterApp = CSVPlotterApp
        layout = QGridLayout()
        self.setLayout(layout)

        # create menu
        menubar = QMenuBar()
        layout.addWidget(menubar, 0, 0)
        actionFile = menubar.addMenu("File")

        open_action = QAction("Open CSV", self)
        open_action.triggered.connect(self.openCSV)
        actionFile.addAction(open_action)

        actionFile.addSeparator()
        actionFile.addMenu("Export CSV")
        actionFile.addMenu("Graph")
        actionFile.addMenu("GPS")
        menubar.setStyleSheet("font-size: 30px;")

    def openCSV(self):
        # self.CSVPlotterApp.loadCSV()
        self.CSVPlotterApp.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create and add the custom title bar
        titlebar = Color(QColor(81, 29, 102), 120, image_width_ratio=1, text_width_ratio=15, image2_width_ratio=5)
        self.setMenuWidget(titlebar)

        self.setWindowIcon(QIcon('cansat_logo.png'))
        self.setWindowTitle("Ground Station")

        self.layout_bar=QGridLayout()
        self.layout_bar.sidebar = Sidebar([
            {"name": "CAL", "component": CAL},
            {"name": "Set timeout", "component": SET_TIMEOUT},
            {"name": "CX_ON", "component": CX_ON},
            {"name": "CX_OFF", "component": CX_OFF},
            {"name": "SIM ENABLE", "component": SIM_ENABLE},
            {"name": "SIM ACTIVATE", "component": SIM_ACTIVATE},
            {"name": "SIM DEACTIVATE", "component": SIM_DEACTIVATE},
        ])
         # Simulate updating sensor values
        roll = 0.0
        pitch = 0.0
        yaw = 0.0

        def update_sensor_values(self):
         nonlocal roll, pitch, yaw
         roll += 0.1
         pitch += 0.2
         yaw += 0.3
         SensorDisplay.update_values(roll, pitch, yaw)


        timer = QTimer()
        timer.timeout.connect(update_sensor_values)
        timer.start(1000)  # Update values every second
        self.layout_bar.addWidget(MENU(CSVPlotterApp()),0,0,0,6)
        self.layout_bar.addWidget(self.layout_bar.sidebar,1,0,6,2)
        

        self.CirBar_page = CircularProgressBar()
        self.layout_bar.addWidget(self.CirBar_page, 1, 1,3,1)

        self.CirBar_page = CircularProgressBar()
        self.layout_bar.addWidget(self.CirBar_page, 1, 2,3,1)

        self.CirBar_page = CircularProgressBar()
        self.layout_bar.addWidget(self.CirBar_page, 1, 3,3,1)

        self.CirBar_page = CircularProgressBar()
        self.layout_bar.addWidget(self.CirBar_page, 3, 1,3,1)

        self.CirBar_page = CircularProgressBar()
        self.layout_bar.addWidget(self.CirBar_page, 3, 2,3,1)

        self.CirBar_page = CircularProgressBar()
        self.layout_bar.addWidget(self.CirBar_page, 3, 3,3,1)

        # Create the CircleWidget and add it to the layout
        self.circle_widget = CircleWidget()
        self.layout_bar.addWidget(self.circle_widget, 5, 1,3,4)

        #Create the rightBar
        self.right_side =SensorDisplay()
        self.layout_bar.addWidget(self.right_side,0,4,6,2)

        # Create a central widget to contain the layout
        central_widget = QWidget()
        central_widget.setLayout(self.layout_bar)

        # Set the central widget of the main window
        self.setCentralWidget(central_widget)
    
    def open_csv_plotter_app(self):
        self.csv_plotter_app.show()

        
       
if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.setGeometry(0,0,1900,900)
    window.show()
    sys.exit(app.exec_())