import sys
import csv
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QStackedWidget ,QGridLayout,QMenuBar,QFileDialog, QVBoxLayout, QPushButton
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

class CSVPlotterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("CSV Plotter")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        self.figure = Figure(figsize=(8, 6), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.load_button = QPushButton("Load CSV File")
        layout.addWidget(self.load_button)

        self.load_button.clicked.connect(self.loadCSV)

        self.status_label = QLabel()
        layout.addWidget(self.status_label)

    def loadCSV(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        filePath, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)
        
        if filePath:
            try:
                self.plotCSV(filePath)
                self.status_label.setText(f"Loaded: {filePath}")
            except Exception as e:
                self.status_label.setText(f"Error: {str(e)}")

    def plotCSV(self, filePath):
        data = [[] for _ in range(4)]  # Create empty lists for each column

        with open(filePath, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                for i in range(4):
                    data[i].append(float(row[i]))

        if any(len(column) == 0 for column in data):
            raise ValueError("CSV file is empty or missing columns.")

        self.figure.clear()

        # Create four subplots for each column
        for i in range(4):
            ax = self.figure.add_subplot(2, 2, i + 1)  # 2x2 grid of subplots
            ax.plot(data[i])
            ax.set_xlabel("Data Point")
            ax.set_ylabel(f"Value {i+1}")
            ax.set_title(f"Line Plot {i+1}")

        self.figure.tight_layout()
        self.canvas.draw()

class MENU(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        # create menu
        menubar = QMenuBar()
        layout.addWidget(menubar, 0, 0)
        actionFile = menubar.addMenu("Import CSV")
        actionFile.addAction("New")
        actionFile.addAction("Open")
        actionFile.addAction("Save")
        actionFile.addAction("Save as")
        actionFile.addSeparator()
        actionFile.addAction("Quit")
        menubar.addMenu("Export CSV")
        menubar.addMenu("Graph")
        menubar.addMenu("GPS")
        menubar.setStyleSheet(" font-size:30px;")
        actionFile.setStyleSheet("padding:10px;")
        
        
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

        def update_sensor_values():
         nonlocal roll, pitch, yaw
         roll += 0.1
         pitch += 0.2
         yaw += 0.3
         window.update_values(roll, pitch, yaw)

        timer = QTimer()
        timer.timeout.connect(update_sensor_values)
        timer.start(1000)  # Update values every second
        self.layout_bar.addWidget(MENU(),0,0,0,6)
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
        self.layout_bar.addWidget(self.circle_widget, 5, 2,3,4)

        #Create the rightBar
        self.right_side =SensorDisplay()
        self.layout_bar.addWidget(self.right_side,0,4,6,2)

        # Create the text input page
        self.text_input_page = TextInputPage()
        self.text_input_page.setStyleSheet("border: 3px solid black;")

        # Add the text input page to the layout
        self.layout_bar.addWidget(self.text_input_page, 5, 1, 2, 2)  # Span 2 row and 2 columns


        # Create a central widget to contain the layout
        central_widget = QWidget()
        central_widget.setLayout(self.layout_bar)

        # Set the central widget of the main window
        self.setCentralWidget(central_widget)

        
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(0,0,1900,900)
    window.show()
    sys.exit(app.exec_())