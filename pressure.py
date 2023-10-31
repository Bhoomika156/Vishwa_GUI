import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor, QBrush, QFont, QPen
from PyQt5.QtCore import Qt, QTimer,pyqtSignal
import pandas as pd
import csv

class Pressure(QWidget):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.max_value = 100
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateValue)
        self.timer.start(1000)  # Update the value every second
        # layout = QVBoxLayout(self)
      
 
    def loadCSVData(self, file_path):
        df = pd.read_csv(file_path)
        # Get the last row
        last_row = df.iloc[-1]

        # Extract the value from a specific column (e.g., 'ColumnName')
        last_value = last_row[1]
        self.value = last_value
        self.update()

    def updateValue(self):
        try:
            with open('receivedPackets.csv', 'r') as csv_file:
                # print("Opened")
                csv_reader = csv.reader(csv_file)
                last_row = None  # Initialize a variable to store the last row
                second_last_row = None  # Initialize a variable to store the last row

                for row in csv_reader:
                    second_last_row=last_row
                    last_row=row  # Store the current row

                if second_last_row :
                    self.value = float(second_last_row[2])
            # self.value = (self.value + 10) % (self.max_value + 1)
                    self.update()
        except FileNotFoundError:
            self.roll = 0.0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Calculate the progress angle
        progress_angle = int(360 * self.value / 1000)

        # Draw the outer circle
        painter.setPen(QPen(QColor(200, 200, 200), 20))  # Set the border thickness
        painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(30, 30, 180, 180)

        # Draw the progress arc as a border
        painter.setPen(QPen(QColor(128, 0, 128), 20))  # Set the progress border color and thickness
        painter.drawArc(30, 30, 180, 180, 90 * 16, progress_angle * 16)

        # Draw the value text
        painter.setPen(Qt.black)
        painter.setFont(QFont('Arial', 12))
        painter.drawText(30, 30, 180, 180, Qt.AlignCenter, f'{self.value}%°C')
        painter.drawText(15, 15, 250, 240, Qt.AlignCenter, f'Pressure    ')


    



    

