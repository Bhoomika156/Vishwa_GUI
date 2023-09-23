import sys
import os
# import time
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QWidget, QPushButton, QLabel
from matplotlib.figure import Figure
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import *

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

        # Create a spacer item to push the 'Load' button to the bottom
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        self.load_button = QPushButton("Load CSV File")
        layout.addWidget(self.load_button)

        self.load_button.clicked.connect(self.loadCSV)

        self.status_label = QLabel()
        layout.addWidget(self.status_label)

        # Initialize file path and modification time
        self.filePath = None
        self.last_modification_time = None

        # Create a timer for updating the plot
        self.update_timer = QtCore.QTimer(self)
        self.update_timer.timeout.connect(self.update_plot)

    def update_plot(self):
        if self.filePath:
            try:
                modification_time = os.path.getmtime(self.filePath)

                # Check if the file has been modified
                if modification_time != self.last_modification_time:
                    self.last_modification_time = modification_time
                    data = pd.read_csv(self.filePath)
                    c1 = data.iloc[:, 0]  # Values from the first column
                    c2 = data.iloc[:, 1]  # Values from the second column
                    c3 = data.iloc[:, 2]  # Values from the third column
                    c4 = data.iloc[:, 3]  # Values from the fourth column
                    
                    # Clear the previous plot
                    self.figure.clear()

                    # Create four subplots
                    ax1 = self.figure.add_subplot(221)
                    ax2 = self.figure.add_subplot(222)
                    ax3 = self.figure.add_subplot(223)
                    ax4 = self.figure.add_subplot(224)

                    # Plot data on the subplots
                    ax1.plot(c2, c1, label='Graph 1')
                    ax2.plot(c2, c3, label='Graph 2')
                    ax3.plot(c2, c4, label='Graph 3')
                    ax4.plot(c4, c1, label='Graph 4')

                    # Customize plot details for each subplot
                    ax1.set_xlabel('X-axis')
                    ax1.set_ylabel('Y-axis')
                    ax1.set_title('Graph 1')
                    ax1.legend()

                    ax2.set_xlabel('X-axis')
                    ax2.set_ylabel('Y-axis')
                    ax2.set_title('Graph 2')
                    ax2.legend()

                    ax3.set_xlabel('X-axis')
                    ax3.set_ylabel('Y-axis')
                    ax3.set_title('Graph 3')
                    ax3.legend()

                    ax4.set_xlabel('X-axis')
                    ax4.set_ylabel('Y-axis')
                    ax4.set_title('Graph 4')
                    ax4.legend()

                    # Redraw the canvas
                    self.canvas.draw()

            except Exception as e:
                self.status_label.setText(f"Error: {str(e)}")

    def loadCSV(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)

        if filePath:
            # print(f"Loaded: {filePath}")
            self.filePath = filePath  # Store the file path
            try:
                # Start the update timer with a 1-second interval
                self.update_timer.start(1000)

                self.status_label.setText(f"Loaded: {filePath}")

            except Exception as e:
                self.status_label.setText(f"Error: {str(e)}")

def main():
    app = QApplication(sys.argv)
    window = CSVPlotterApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()