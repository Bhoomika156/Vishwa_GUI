import sys
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Sidebar(QWidget):
    def __init__(self, routes):
        super().__init__()

        self.routes = routes
        self.sidebar_buttons = []

        # Create sidebar layout
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Add sidebar buttons for each route
        for route in self.routes:
            button = QPushButton(route["name"])
            button.clicked.connect(lambda _, route=route: self.on_button_click(route))
            sidebar_layout.addWidget(button)
        
            button.setStyleSheet(
                "QPushButton {"
                "   background-color: #800080;"
                "   color: white;"
                "   border: none;"
                "   padding: 5px;"
                "   margin: 10px;"
                "font-size: 20px;"
                "   text-align: center;"
                "   font-weight: bold;"
                "width:250px;"
                "Height:40px;"
                "border-radius:10px;"
                "border: 4px solid #4B0082;"
                
                "}"
                "QPushButton:hover {"
                "   background-color:#4B0082;"
                "border: 4px solid  #800080;"
                "}"
            )
        
        # Create main content layout
        self.main_layout = QVBoxLayout()
        self.stacked_widget = QStackedWidget()

        # Add pages to the main content area
        for route in self.routes:
            page_widget = route["component"]()
            self.stacked_widget.addWidget(page_widget)

        self.main_layout.addWidget(self.stacked_widget)

        # Add sidebar and main content layouts to main widget
        main_layout = QHBoxLayout(self)
        main_layout.addLayout(sidebar_layout)
        main_layout.addLayout(self.main_layout)

        # Set the initial page to display
        self.stacked_widget.setCurrentIndex(0)

    def on_button_click(self, route):
        index = self.routes.index(route)
        self.stacked_widget.setCurrentIndex(index)
    
class CAL(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("CAL")
        self.setFont(QFont('Arial',20))
        


class SET_TIMEOUT(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("SET TIMEOUT")
        


class CX_ON(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("CX ON")
        


class CX_OFF(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("CX OFF")
        


class SIM_ENABLE(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("SIM ENABLE")
        


class SIM_ACTIVATE(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("SIM ACTIVE")
        


class SIM_DEACTIVATE(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("SIM DEACTIVATE")

class SIMP(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("SIMP")