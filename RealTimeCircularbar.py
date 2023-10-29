import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QFileDialog, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QFont


class QProgressBarCircle(QWidget):
    def __init__(self, parent=None):
        super(QProgressBarCircle, self).__init__(parent)
        self.setMinimumSize(100, 120)  # Increased the height to accommodate the text
        self.setMaximumSize(100, 120)
        self.value = 0

    def setValue(self, value):
        self.value = value
        self.repaint()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw outer circle
        outer_pen = QPen()
        outer_pen.setWidth(2)
        outer_pen.setColor(QColor(0, 0, 0))
        painter.setPen(outer_pen)
        painter.drawEllipse(5, 5, 90, 90)

        # Draw inner circle
        inner_pen = QPen()
        inner_pen.setWidth(2)
        inner_pen.setColor(QColor(0, 0, 0))
        painter.setPen(inner_pen)
        painter.drawEllipse(25, 25, 50, 50)

        # Fill the gap between circles based on the value
        fill_brush = QBrush(QColor(0, 0, 255))
        painter.setBrush(fill_brush)

        painter.setPen(outer_pen)
        # Convert the values to expected types
        x, y, w, h = 5, 5, 90, 90
        a = 0
        alen = int(self.value * 16)
        
        painter.drawPie(x, y, w, h, a, alen)

       
        fill_brush = QBrush(QColor(0, 255,0))
        painter.setBrush(fill_brush)
        # Convert the values to expected types
        painter.setPen(inner_pen)
        x, y, w, h = 5, 5, 90, 90
        a = 0
        alen = int(self.value * 16)
        
        painter.drawPie(x, y, w, h, a, alen)


        # Display the value inside the circle with 2 decimal places
        value_text = "{:.2f}".format(self.value)
        font = QFont()
        font.setPointSize(10)
        painter.setFont(font)
        painter.setPen(QColor(0, 0, 0))
        painter.drawText(25, 25, 50, 50, Qt.AlignCenter, value_text)

        # Display the text "Temperature" below the value
        temp_text = "Temperature"
        temp_font = QFont()
        temp_font.setPointSize(8)  # Adjust font size as needed
        painter.setFont(temp_font)
        painter.drawText(5, 80, 90, 20, Qt.AlignCenter, temp_text)


class RealTimeCSVReader(QMainWindow):
    def __init__(self):
        super(RealTimeCSVReader, self).__init__()

        self.setWindowTitle("Real-Time CSV Reader")

        # Create widgets
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.progress_bar = QProgressBarCircle(self)
        self.layout.addWidget(self.progress_bar)

        self.load_button = QPushButton("Load CSV", self)
        self.load_button.clicked.connect(self.load_csv)
        self.layout.addWidget(self.load_button)

        # Timer to update the progress bar
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)

        # Initialize DataFrame
        self.data_frame = pd.DataFrame()

    def load_csv(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)

        if file_name:
            self.data_frame = pd.read_csv(file_name)

    def update_progress(self):
        if not self.data_frame.empty:
            # Get the last row value
            # Assuming the first column contains the value
            last_row_value = self.data_frame.iloc[-1, 0]

            # Update the progress bar
            self.progress_bar.setValue(last_row_value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RealTimeCSVReader()
    window.setGeometry(100, 100, 200, 200)
    window.show()
    sys.exit(app.exec_())
