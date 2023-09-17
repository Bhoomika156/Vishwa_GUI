from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QApplication, QMainWindow, QWidget, QLabel, QPushButton, QStackedWidget
from PyQt5.QtCore import Qt


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
            button.clicked.connect(
                lambda _, route=route: self.on_button_click(route))
            self.sidebar_buttons.append(button)
            sidebar_layout.addWidget(button)

            # Style the button
            button.setStyleSheet(
                "QPushButton {"
                "   background-color: #800080;"
                "   color: white;"
                "   border: none;"
                "   padding: 20px;"
                "   margin: 10px;"
                "   text-align: center;"
                "   font-weight: bold;"
                "}"
                "QPushButton:hover {"
                "   background-color:#4B0082;"
                "}"
            )

        # Create main content layout
        self.main_layout = QHBoxLayout()
        self.stacked_widget = QStackedWidget()

        # Add pages to the main content area
        for route in self.routes:
            page_widget = route["component"]()
            self.stacked_widget.addWidget(page_widget)

        self.main_layout.addWidget(self.stacked_widget)

        # Add sidebar and main content layouts to the main widget
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
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)


class SET_TIMEOUT(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("SET TIMEOUT")
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)


class CX_ON(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("CX ON")
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)


class CX_OFF(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("CX OFF")
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)


class SIM_ENABLE(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("SIM ENABLE")
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)


class SIM_ACTIVATE(QWidget):
    def __init__(self):
        super().___init___()
        self.label = QLabel("SIM ACTIVE")
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)


class SIM_DEACTIVATE(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("SIM DEACTIVATE")
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.sidebar = Sidebar([
            {"name": "CAL", "component": CAL},
            {"name": "Set timeout", "component": SET_TIMEOUT},
            {"name": "CX_ON", "component": CX_ON},
            {"name": "CX_OFF", "component": CX_OFF},
            {"name": "SIM ENABLE", "component": SIM_ENABLE},
            {"name": "SIM ACTIVATE", "component": SIM_ACTIVATE},
            {"name": "SIM DEACTIVATE", "component": SIM_DEACTIVATE},
        ])

        self.setCentralWidget(self.sidebar)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()