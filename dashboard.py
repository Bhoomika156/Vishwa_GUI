import sys
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QStackedWidget,QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtCore import Qt
from OnlyInput import TextInputPage
from CircProgBar import CircularProgressBar

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
        colors = [Qt.green, Qt.green, Qt.blue, Qt.yellow, Qt.cyan, Qt.magenta]
        return colors[stage % len(colors)]
    
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
                "   padding: 10px;"
                "   margin: 10px;"
                "   text-align: center;"
                "   font-weight: bold;"
                "width:150px;"
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
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout_bar=QGridLayout()
        self.layout_bar.sidebar = Sidebar([
            {"name": "CAL", "component": CAL},
            {"name": "Set timeout", "component": SET_TIMEOUT},
            {"name": "CX_ON", "component": CX_ON},
            {"name": "CX_OFF", "component": CX_OFF},
            {"name": "SIM ENABLE", "component": SIM_ENABLE},
            {"name": "SIM ACTIVATE", "component": SIM_ACTIVATE},
            {"name": "SIM DEACTIVATE", "component": SIM_DEACTIVATE},
        ])
        self.layout_bar.addWidget(self.layout_bar.sidebar,0,0,6,2)

        self.CirBar_page = CircularProgressBar()
        self.layout_bar.addWidget(self.CirBar_page, 0, 2,3,1)

        self.CirBar_page = CircularProgressBar()
        self.layout_bar.addWidget(self.CirBar_page, 0, 3,3,1)

        self.CirBar_page = CircularProgressBar()
        self.layout_bar.addWidget(self.CirBar_page, 0, 4,3,1)

        self.CirBar_page = CircularProgressBar()
        self.layout_bar.addWidget(self.CirBar_page, 3, 2,3,1)

        self.CirBar_page = CircularProgressBar()
        self.layout_bar.addWidget(self.CirBar_page, 3, 3,3,1)

        self.CirBar_page = CircularProgressBar()
        self.layout_bar.addWidget(self.CirBar_page, 3, 4,3,1)

        # Create the CircleWidget and add it to the layout
        self.circle_widget = CircleWidget()
        self.layout_bar.addWidget(self.circle_widget, 6, 2,3,4)

        # Create the text input page
        self.text_input_page = TextInputPage()
        self.text_input_page.setStyleSheet("border: 3px solid black;")

        # Add the text input page to the layout
        self.layout_bar.addWidget(self.text_input_page, 6, 0, 2, 3)  # Span 1 row and 2 columns

        # Create a central widget to contain the layout
        central_widget = QWidget()
        central_widget.setLayout(self.layout_bar)

        # Set the central widget of the main window
        self.setCentralWidget(central_widget)
       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100,100,300,600)
    window.show()
    sys.exit(app.exec_())

