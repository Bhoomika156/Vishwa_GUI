import sys
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class SensorDisplay(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Sensor Values Display')
        self.title_label = QLabel('Sensor Values', self)

        self.roll_label = QLabel('Roll:', self)
        self.roll_value_label = QLabel('00.00 °', self)

        self.pitch_label = QLabel('Pitch:', self)
        self.pitch_value_label = QLabel('00.00 °', self)

        self.yaw_label = QLabel('Yaw:', self)
        self.yaw_value_label = QLabel('00.00 °', self)

        self.time_label = QLabel('Time:', self)
        self.time_value_label = QLabel('00:00:00', self)

        self.packet_count_label = QLabel('Packet Count:', self)
        self.packet_value_label = QLabel('0', self)

        self.mode_label = QLabel('Mode:', self)
        self.mode_value_label = QLabel('F', self)

        title_style = "font-size: 25px; margin-top: 5px;"
        label_style = "font-size: 30px; margin-top: 5px;"
        value_style = "font-size: 25px; margin-top: 2px; padding: 5px;"

        self.title_label.setStyleSheet(title_style)
        self.roll_label.setStyleSheet(label_style)
        self.roll_value_label.setStyleSheet(value_style)

        self.pitch_label.setStyleSheet(label_style)
        self.pitch_value_label.setStyleSheet(value_style)

        self.yaw_label.setStyleSheet(label_style)
        self.yaw_value_label.setStyleSheet(value_style)

        self.time_label.setStyleSheet(label_style)
        self.time_value_label.setStyleSheet(value_style)

        self.packet_count_label.setStyleSheet(label_style)
        self.packet_value_label.setStyleSheet(value_style)

        self.mode_label.setStyleSheet(label_style)
        self.mode_value_label.setStyleSheet(value_style)

        roll_layout = QVBoxLayout()
        roll_layout.addWidget(self.roll_label)
        roll_layout.addWidget(self.roll_value_label)

        pitch_layout = QVBoxLayout()
        pitch_layout.addWidget(self.pitch_label)
        pitch_layout.addWidget(self.pitch_value_label)

        yaw_layout = QVBoxLayout()
        yaw_layout.addWidget(self.yaw_label)
        yaw_layout.addWidget(self.yaw_value_label)

        time_layout = QVBoxLayout()
        time_layout.addWidget(self.time_label)
        time_layout.addWidget(self.time_value_label)

        packet_layout = QVBoxLayout()
        packet_layout.addWidget(self.packet_count_label)
        packet_layout.addWidget(self.packet_value_label)

        mode_layout = QVBoxLayout()
        mode_layout.addWidget(self.mode_label)
        mode_layout.addWidget(self.mode_value_label)

        hori_layout_1 = QHBoxLayout()
        hori_layout_1.addLayout(roll_layout)
        hori_layout_1.addLayout(pitch_layout)

        hori_layout_2 = QHBoxLayout()
        hori_layout_2.addLayout(yaw_layout)
        hori_layout_2.addLayout(time_layout)

        hori_layout_3 = QHBoxLayout()
        hori_layout_3.addLayout(packet_layout)
        hori_layout_3.addLayout(mode_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addLayout(hori_layout_1)
        main_layout.addLayout(hori_layout_2)
        main_layout.addLayout(hori_layout_3)

        self.setLayout(main_layout)

    def update_values(self, roll, pitch, yaw):
        self.roll_value_label.setText(f'{roll:.2f} degrees')
        self.pitch_value_label.setText(f'{pitch:.2f} degrees')
        self.yaw_value_label.setText(f'{yaw:.2f} degrees')