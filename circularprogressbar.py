import sys
import csv
import pandas as pd

from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Color(QWidget):

    def __init__(self, color, height, image_width_ratio=1, text_width_ratio=1, image2_width_ratio=1):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(self.backgroundRole(), color)
        self.setPalette(palette)
        self.setFixedHeight(height)

        h_layout = QHBoxLayout()

        pixmap = QPixmap("logo.png")
        desired_image_size = QSize(100, 100)
        pixmap = pixmap.scaled(desired_image_size, Qt.KeepAspectRatio)

        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)
        self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        h_layout.addWidget(self.image_label, image_width_ratio)

        self.text_label = QLabel("TEAM AETHER", self)

        font = QFont()
        font.setPointSize(30)
        self.text_label.setFont(font)
        self.text_label.setStyleSheet("color: black;")

        text_height = self.text_label.fontMetrics().height()
        self.text_label.setFixedHeight(text_height + 20)
        self.text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        h_layout.addWidget(self.text_label, text_width_ratio)

        v_layout = QVBoxLayout()

        pixmap2 = QPixmap("flag.png")
        desired_image_size2 = QSize(150, 300)
        pixmap2 = pixmap2.scaled(desired_image_size2, Qt.KeepAspectRatio)

        self.second_image_label = QLabel(self)
        self.second_image_label.setPixmap(pixmap2)
        self.second_image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        v_layout.addWidget(self.second_image_label)

        self.second_text_label = QLabel("                    INDIA", self)

        font2 = QFont()
        font2.setPointSize(8)
        font2.setFamily("Times New Roman")
        self.second_text_label.setFont(font2)
        self.second_text_label.setStyleSheet("color: black;")
        self.second_text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        v_layout.addWidget(self.second_text_label)

        h_layout.addStretch()
        h_layout.addLayout(v_layout)

        self.setLayout(h_layout)


# class CircularProgressBar(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.value = 0
#         self.max_value = 100
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.updateValue)
#         self.timer.start(1000)  # Update the value every second

#     def updateValue(self):
#         self.value = (self.value + 10) % (self.max_value + 1)
#         self.update()

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)

#         # Calculate the progress angle
#         progress_angle = int(360 * self.value / self.max_value)

#         # Draw the outer circle
#         painter.setPen(QPen(QColor(200, 200, 200), 20))  # Set the border thickness
#         painter.setBrush(Qt.NoBrush)
#         painter.drawEllipse(50, 50, 200, 200)

#         # Draw the progress arc as a border
#         painter.setPen(QPen(QColor(0, 0, 255), 20))  # Set the progress border color and thickness
#         painter.drawArc(50, 50, 200, 200, 90 * 16, progress_angle * 16)

#         # Draw the value text
#         painter.setPen(Qt.black)
#         painter.setFont(QFont('Arial', 24))
#         painter.drawText(50, 50, 200, 200, Qt.AlignCenter, f'{self.value}%' )


class CircularProgressBar(QWidget):
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
        self.value = (self.value + 10) % (self.max_value + 1)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Calculate the progress angle
        progress_angle = int(360 * self.value / self.max_value)

        # Draw the outer circle
        painter.setPen(QPen(QColor(200, 200, 200), 20))  # Set the border thickness
        painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(30, 30, 180, 180)

        # Draw the progress arc as a border
        painter.setPen(QPen(QColor(0, 0, 255), 20))  # Set the progress border color and thickness
        painter.drawArc(30, 30, 180, 180, 90 * 16, progress_angle * 16)

        # Draw the value text
        painter.setPen(Qt.black)
        painter.setFont(QFont('Arial', 12))
        painter.drawText(30, 30, 180, 180, Qt.AlignCenter, f'{self.value}%°C')
        painter.drawText(15, 15, 250, 240, Qt.AlignCenter, f'Temperature    ')

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowIcon(QtGui.QIcon('cansat_logo.png'))
        self.setWindowTitle("Ground Station")

        # Create a menu bar
        menubar = self.menuBar()

        # Create File menu and actions
        file_menu = menubar.addMenu('File')

        import_csv_action = QAction('Import CSV', self)
        import_csv_action.triggered.connect(self.import_csv)  # Connect to the import_csv function
        file_menu.addAction(import_csv_action)

        export_csv_action = QAction('Export CSV', self)
        file_menu.addAction(export_csv_action)

        gps_menu = menubar.addMenu('GPS')

        gps_action = QAction('Open GPS', self)
        gps_menu.addAction(gps_action)

        documents_menu = menubar.addMenu('Documents')

        documents_action = QAction('Open Documents', self)
        documents_menu.addAction(documents_action)

        # Style the menu bar with lilac color and black text
        menubar.setStyleSheet('''
            QMenuBar {
                background-color: #CF9FFF;
                border: 1px solid #000;
            }

            QMenuBar::item {
                background-color: #CF9FFF;
                padding: 5px 10px;
                border: 1px solid #000;
                color: black;  /* Text color is set to black */
            }

            QMenuBar::item:selected {
                background-color: #C090FF;
            }

            QMenu {
                background-color: #CF9FFF;
                border: 1px solid #000;
            }

            QMenu::item {
                background-color: #CF9FFF;
                padding: 5px 10px;
                border: 1px solid #000;
                color: black;  /* Text color is set to black */
            }

            QMenu::item:selected {
                background-color: #C090FF;
            }
        ''')

        layout = QVBoxLayout()
        titlebar = Color(QColor(81, 29, 102), 120, image_width_ratio=1, text_width_ratio=15, image2_width_ratio=5)
        layout.addWidget(titlebar, alignment=Qt.AlignTop)

        circular_progress = CircularProgressBar()
        layout.addWidget(circular_progress, alignment=Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def import_csv(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # Allow only read access to the selected file
        file_name, _ = QFileDialog.getOpenFileName(self, "Import CSV", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if file_name:
            try:
                with open(file_name, 'r', newline='') as file:
                    # Read and process the CSV file here
                    reader = csv.reader(file)
                    for row in reader:
                        print(row)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error reading CSV file:\n{str(e)}")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
