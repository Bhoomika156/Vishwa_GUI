import sys
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class TextInputPage(QWidget):
    def __init__(self):
        super().__init__()
        self.input_label = QLabel('ENTRY COMMAND')
        self.input_label.setFont(QFont('Arial',20))
        self.input_label.setStyleSheet("font-size:25px; font-style:bold;")
        self.text_input = QLineEdit()
        self.text_input.setFixedWidth(300)  # Set the fixed width of the text input to 300 pixels
        self.text_input.setStyleSheet("font-size:25px")
        self.result_label = QLabel('Result: ')
        self.result_label.setFixedWidth(300)
        self.result_label.setStyleSheet("font-size:25px")
        submit_button = QPushButton('Submit')
        submit_button.setFixedWidth(100)  # Reduced width of the submit button
        # submit_button.clicked.connect(self.on_submit)

        # Create a layout for the input elements and align them to the bottom-left corner
        input_layout = QVBoxLayout()
        input_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.text_input)
        input_layout.addWidget(submit_button)
        
        # Create a main layout for the page
        layout = QVBoxLayout(self)
        layout.addLayout(input_layout)
        # layout.addWidget(self.result_label)
        # self.result_label.setFixedHeight(35)
        # submit_button.setStyleSheet("font-size:25px")

    # def on_submit(self):
    #     input_text = self.text_input.text()
    #     self.result_label.setText(f'Result: {input_text}')
       

