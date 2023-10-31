import sys
import csv
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer



class SensorDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_initial_values()  # Load initial values from the CSV
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_values)
        self.update_timer.start(1000)  # Update values every 5 seconds

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

        self.speed_label = QLabel('Speed:', self)
        self.speed_value_label = QLabel('0', self)

        self.HS_deployed_label = QLabel('HS Deployed:', self)
        self.HS_deployed_value_label = QLabel('N', self)

        self.PC_deployed_label = QLabel('PC Deployed:', self)
        self.PC_deployed_value_label = QLabel('N', self)

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

        self.speed_label.setStyleSheet(label_style)
        self.speed_value_label.setStyleSheet(value_style)

        self.HS_deployed_label.setStyleSheet(label_style)
        self.HS_deployed_value_label.setStyleSheet(value_style)

        self.PC_deployed_label.setStyleSheet(label_style)
        self.PC_deployed_value_label.setStyleSheet(value_style)

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

        speed_layout = QVBoxLayout()
        speed_layout.addWidget(self.speed_label)
        speed_layout.addWidget(self.speed_value_label)

        HS_deployed_layout = QVBoxLayout()
        HS_deployed_layout.addWidget(self.HS_deployed_label)
        HS_deployed_layout.addWidget(self.HS_deployed_value_label)

        PC_deployed_layout = QVBoxLayout()
        PC_deployed_layout.addWidget(self.PC_deployed_label)
        PC_deployed_layout.addWidget(self.PC_deployed_value_label)

        hori_layout_1 = QHBoxLayout()
        hori_layout_1.addLayout(roll_layout)
        hori_layout_1.addLayout(pitch_layout)

        hori_layout_2 = QHBoxLayout()
        hori_layout_2.addLayout(yaw_layout)
        hori_layout_2.addLayout(time_layout)

        hori_layout_3 = QHBoxLayout()
        hori_layout_3.addLayout(packet_layout)
        hori_layout_3.addLayout(mode_layout)

        hori_layout_4 = QHBoxLayout()
        hori_layout_4.addLayout(speed_layout)
        hori_layout_4.addLayout(HS_deployed_layout)

        hori_layout_5 = QHBoxLayout()
        hori_layout_5.addLayout(PC_deployed_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addLayout(hori_layout_1)
        main_layout.addLayout(hori_layout_2)
        main_layout.addLayout(hori_layout_3)
        main_layout.addLayout(hori_layout_4)
        main_layout.addLayout(hori_layout_5)

        self.setLayout(main_layout)

    def load_initial_values(self):
        try:
            with open('receivedPackets.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)

                for row in csv_reader:
                    pass  # Iterate through the file to get to the last row
                if len(row) >= 3:
                    self.roll = float(row[0])
                    self.pitch = float(row[1])
                    self.yaw = float(row[2])
                else:
                    self.roll = 0.0
                    self.pitch = 0.0
                    self.yaw = 0.0
        except FileNotFoundError:
            self.roll = 0.0
            self.pitch = 0.0
            self.yaw = 0.0

    def update_values(self):
        try:
            with open('receivedPackets.csv', 'r') as csv_file:
                # print("Opened")
                csv_reader = csv.reader(csv_file)
                last_row = None  # Initialize a variable to store the last row
                second_last_row = None  # Initialize a variable to store the last row

                for row in csv_reader:
                    second_last_row=last_row
                    last_row=row  # Store the current row

                # print(len(second_last_row))
                # print(second_last_row)
                if second_last_row and len(second_last_row) >= 3:
                    self.roll = float(second_last_row[0])
                    self.pitch = float(second_last_row[1])
                    self.yaw = float(second_last_row[2])

                    self.roll_value_label.setText(f'{self.roll:.2f} °')
                    self.pitch_value_label.setText(f'{self.pitch:.2f} °')
                    self.yaw_value_label.setText(f'{self.yaw:.2f} °')
                    # self.time_value_label.setText(count)
                else:
                    print("Incomplete data in the last row")
                    self.roll = 0.0
                    self.pitch = 0.0
                    self.yaw = 0.0
        except FileNotFoundError:
            self.roll = 0.0
            self.pitch = 0.0
            self.yaw = 0.0


       


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    sensor_display = SensorDisplay()
    window.setCentralWidget(sensor_display)
    window.setGeometry(100, 100, 400, 400)
    window.show()
    sys.exit(app.exec_())
