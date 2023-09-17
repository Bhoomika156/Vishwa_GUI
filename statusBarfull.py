import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtCore import Qt

class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.stage = 1
        self.total_stages = 6

    def paintEvent(self, event):
        painter = QPainter(self)
        radius = 30  # Circle radius
        spacing = 20  # Spacing between circles
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
                painter.setPen(QPen(Qt.black, 2))
                painter.drawLine(x_prev + 2 * radius, y_prev, x, y + radius)

    def getStageColor(self, stage):
        # You can define your own colors here based on the stage number.
        # This is just a simple example.
        colors = [Qt.red, Qt.green, Qt.blue, Qt.yellow, Qt.cyan, Qt.magenta]
        return colors[stage % len(colors)]

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Connected Circles Example')
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Start button
        self.startButton = QPushButton('Start Process', self)
        self.startButton.clicked.connect(self.startProcess)
        layout.addWidget(self.startButton)

        # Circle widget
        self.circleWidget = CircleWidget()
        layout.addWidget(self.circleWidget)

    def startProcess(self):
        # Simulate stages progress
        if self.circleWidget.stage < self.circleWidget.total_stages:
            self.circleWidget.stage += 1
            self.circleWidget.update()  # Trigger repaint

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())