import sys
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QStackedWidget,QGridLayout,QMenuBar
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.stage = 1
        self.total_stages = 6

    def paintEvent(self, event):
        painter = QPainter(self)
        radius = 25  # Circle radius
        spacing = 32  # Spacing between circles
        x_offset = 50  # Horizontal offset

        for stage in range(self.total_stages):
            x = x_offset + (stage * (2 * radius + spacing))
            y = 50
            color = QColor(200, 200, 200) if stage >= self.stage else self.getStageColor(stage)

            painter.setPen(Qt.black)
            painter.setBrush(QBrush(color))
            painter.drawEllipse(x, y, radius * 2, radius * 2)

            # Draw connecting lines
            if stage > 0:
                x_prev = x_offset + ((stage - 1) * (2 * radius + spacing))
                y_prev = y + radius
                painter.setPen(QPen(Qt.black, 10))
                painter.drawLine(x_prev + 2 * radius, y_prev, x, y + radius)

                # Draw stage numbers
                painter.setFont(QFont("Arial", 12))
                painter.setPen(QColor(0, 0, 0))
                painter.drawText(x + radius - 10, y + radius + 5, str(stage + 1))

    def getStageColor(self, stage):
        # You can define your own colors here based on the stage number.
        # This is just a simple example.
        colors = [Qt.green, Qt.green, Qt.green, Qt.green, Qt.green, Qt.green]
        return colors[stage % len(colors)]