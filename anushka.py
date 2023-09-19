import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QAction, QToolBar

class MyWindow(QMainWindow):
    def _init_(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        # Create the main menu bar
        menubar = self.menuBar()

        # Set the background color, font color, height, and width of the main menu bar
        menubar.setStyleSheet("QMenuBar { background-color: #511D66; color: white; height: 40px; width: 200px; }")
        # menubar.setStyleSheet("QMenuBar { background-color: 451952; color: white; height: 40px; width: 200px; }") 
        layout.addWidget(menubar, 0, 0)
        
        actionFile = menubar.addMenu("Import")
        actionFile.addAction("New")
        actionFile.addAction("Open")
        actionFile.addAction("Save")
        actionFile.addAction("Save as")
        actionFile.addSeparator()
        actionFile.addAction("Quit")
        menubar.addMenu("Export CSV")
        menubar.addMenu("Graph")
        menubar.addMenu("GPS")

        # Create a toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # Add actions to the main toolbar
        toolbar.addAction("Import CSV")
        toolbar.addAction("Export CSV")
        toolbar.addAction("Graph")
        toolbar.addAction("GPS")
        # toolbar.addAction("Action 2")
        # toolbar.addAction("Action 2")

        # Add menus and actions to the main menu bar
        file_menu = menubar.addMenu("File")
        edit_menu = menubar.addMenu("Edit")

        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        undo_action = QAction("Undo", self)
        redo_action = QAction("Redo", self)

        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)

        # Create a secondary menu bar
        secondary_menubar = self.menuBar().addMenu("Secondary")
        secondary_menubar.setStyleSheet("background-color: #FFA500; color: black;")

        secondary_open_action = QAction("Secondary Open", self)
        secondary_save_action = QAction("Secondary Save", self)

        secondary_menubar.addAction(secondary_open_action)
        secondary_menubar.addAction(secondary_save_action)

        self.setWindowTitle("Main Menu Bar and Secondary Menu Bar Example")
        self.setGeometry(100, 100, 800, 600)

if _name_ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())