import sys
import csv
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QWidget, QPushButton, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

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

def main():
    app = QApplication(sys.argv)
    window = CSVPlotterApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()