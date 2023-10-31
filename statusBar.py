import sys
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QStackedWidget, QGridLayout, QMenuBar
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPainter, QColor, QBrush, QPen

class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.stage = 1
        self.total_stages = 4
        self.stages_arr = ["start", "Parachute release", "Cansat deploy", "tether released"]
        self.altitude = 300  # Set the initial altitude value
        self.setStyleSheet("""
            background-color: white;
        """)

    def paintEvent(self, event):
        painter = QPainter(self)
        radius = 40  # Circle radius
        spacing = 110  # Spacing between circles
        x_offset = 50  # Horizontal offset

        for stage in range(self.total_stages):
            x = x_offset + (stage * (2 * radius + spacing))
            y = 50

            # Determine the circle color based on altitude
            color = self.getStageColor(stage)

            painter.setPen(Qt.black)
            painter.setBrush(QBrush(color))
            painter.drawEllipse(x, y, radius * 2, radius * 2)

            # Draw connecting lines
           
            x_prev = x_offset + ((stage - 1) * (2 * radius + spacing))
            y_prev = y + radius
            painter.setPen(QPen(Qt.black, 3))
            painter.drawLine(x_prev + 2 * radius, y_prev, x, y + radius)

            # Draw stage numbers and labels
            painter.setFont(QFont("Arial", 12))
            painter.setPen(QColor(0, 0, 0))
            painter.drawText(x + radius - 10, y + radius + 5, str(stage + 1))
            label = f"{self.stages_arr[stage]}"
            label_width = painter.fontMetrics().width(label)
            painter.drawText(int(x + (radius - label_width) / 2), y - 20, label)

    def getStageColor(self, stage):
    # Determine circle color based on altitude
        if self.altitude == 0 and stage == 0:
            return Qt.yellow
        elif self.altitude >= 300 and stage < 2:
            return Qt.green
        elif self.altitude >= 450 and stage < 3:
            return Qt.green
        elif self.altitude >= 750:
            return Qt.green
        else:
            return Qt.yellow