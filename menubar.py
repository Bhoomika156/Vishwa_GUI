from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QAction, QToolBar
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        self.setWindowIcon(QtGui.QIcon('logo.png'))
         # set the title
        self.setGeometry(0, 0, 11920, 60)
        self.setWindowTitle("Team Aether")

        # size of window
        width = 1000
        self.setFixedWidth(width)

        height = 800
        self.setFixedHeight(height)

        # creating title bar
        titlebar = QMenuBar()
        titlebar.setStyleSheet("QMenuBar { background-color: #511D66; color: white; height: 40px; width: 200px; }")
        layout.addWidget(titlebar, 5, 0)

        # create menu
        menubar = QMenuBar()
        menubar.setStyleSheet("QMenuBar { background-color: 	#301934; color: white; ;  }"
                              "QMenuBar.widget::hover"
                            "{"
                            "background-color : white;"
                            "}")
        layout.addWidget(menubar, 0, 0)
        actionFile = menubar.addMenu("Import CSV")
        actionFile.addAction("New")
        actionFile.addAction("Open")
        actionFile.addAction("Save")
        actionFile.addAction("Save as")
        actionFile.addSeparator()
        actionFile.addAction("Quit")
        menubar.addMenu("Export CSV")
        menubar.addMenu("Graph")
        menubar.addMenu("GPS")

        # add textbox
        tbox = QPlainTextEdit()
        layout.addWidget(tbox, 1, 0)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())