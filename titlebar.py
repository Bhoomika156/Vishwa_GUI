import sys
from PyQt5 import QtGui
#from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QAction, QToolBar, QVBoxLayout, QWidget, QLabel, QApplication, QHBoxLayout
#from PyQt5.QtGui import QPalette, QColor, QPixmap, QFont
#from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# NEEDED FOR RUNNING TITLEBAR.PY AS A STANDALONE APPLICATION
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()

#         self.setWindowTitle("Your Main Application")
#         self.setGeometry(100, 100, 800, 600)

#         # Create and add the custom title bar
#         titlebar = Color(QColor(81, 29, 102), 120, image_width_ratio=1, text_width_ratio=15, image2_width_ratio=5)
#         self.setMenuWidget(titlebar)

class Color(QWidget):

    def __init__(self, color, height, image_width_ratio=1, text_width_ratio=1, image2_width_ratio=1):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        # palette.setColor(QPalette.Window, QColor(color))
        palette.setColor(self.backgroundRole(), color)
        self.setPalette(palette)
        self.setFixedHeight(height)
        #self.setGeometry(0, 0, 120, 120) # to start it from co-ordinates (0, 0)

        # Create a QHBoxLayout to arrange the image and text side by side
        h_layout = QHBoxLayout()

        # Add a QLabel with an image
        pixmap = QPixmap("logo.png") 

        # Set the size of the image using the scaled method
        desired_image_size = QSize(100, 100) 
        pixmap = pixmap.scaled(desired_image_size, Qt.KeepAspectRatio)

        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)
        # h_layout.addWidget(self.image_label)

        # Set the size policy to allow expansion horizontally
        self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Add stretch to control the width of the image
        h_layout.addWidget(self.image_label, image_width_ratio)

        # Add a QLabel for text
        self.text_label = QLabel("TEAM AETHER", self)

        # Change the font size and color
        font = QFont()
        font.setPointSize(30)  
        self.text_label.setFont(font)
        # font.setFamily("Times New Roman")
        self.text_label.setStyleSheet("color: white;")  

        # Adjust the QLabel's height based on font size
        text_height = self.text_label.fontMetrics().height()
        self.text_label.setFixedHeight(text_height + 20)  # Add some extra height so that text doesn't get cut if font size ever exceeds

        # Set the size policy to allow expansion horizontally
        self.text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        h_layout.addWidget(self.text_label)

        # Add stretch to control the width of the text
        h_layout.addWidget(self.text_label, text_width_ratio)


        # Add a QVBoxLayout to stack the new image and text vertically
        v_layout = QVBoxLayout()
            
        # Add a QLabel for the second image
        pixmap2 = QPixmap("flag.png")  
        desired_image_size2 = QSize(150, 300)  
        pixmap2 = pixmap2.scaled(desired_image_size2, Qt.KeepAspectRatio)
            
        self.second_image_label = QLabel(self)
        self.second_image_label.setPixmap(pixmap2)
            
        # Set the size policy to allow expansion horizontally
        self.second_image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            
        v_layout.addWidget(self.second_image_label)
            
        # Add a QLabel for the second text
        self.second_text_label = QLabel("                    INDIA", self)
            
        # Change the font size, color, and style for the second text
        font2 = QFont()
        font2.setPointSize(8)  
        font2.setFamily("Times New Roman")  
        self.second_text_label.setFont(font2)
        self.second_text_label.setStyleSheet("color: white;")  
            
        # Set the size policy to allow expansion horizontally
        self.second_text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            
        v_layout.addWidget(self.second_text_label)
            
        # Add the vertical layout to the horizontal layout with a stretch
        h_layout.addStretch()
        h_layout.addLayout(v_layout)
        

        # Set the horizontal layout as the main layout for the Color widget
        self.setLayout(h_layout)

# NEEDED FOR RUNNING TITLEBAR.PY AS A STANDALONE APPLICATION
# class MainWindow(QMainWindow):

#     def __init__(self):
#         super(MainWindow, self).__init__()

#         self.setWindowIcon(QtGui.QIcon('cansat_logo.png'))
#         self.setWindowTitle("Ground Station")

#         # setting a vertical box layout with this titlebar at the top
#         layout = QVBoxLayout()
#         titlebar = Color(QColor(81, 29, 102), 120, image_width_ratio=1, text_width_ratio=15, image2_width_ratio=5)
#         layout.addWidget(titlebar, alignment=Qt.AlignTop) # taking it to the top

#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec()
