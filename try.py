from PyQt5 import QtWidgets, QtCore, QtGui
import sys

class Style(QtWidgets.QProxyStyle):
    def __init__(self, style = None):
        super().__init__(style)
        self._colors = dict()

    def setColor(self, text, color):
        self._colors[text] = color

    def drawControl(self, element, option, painter, widget):
        if element == QtWidgets.QStyle.CE_MenuItem:
            text = option.text
            option_ = QtWidgets.QStyleOptionMenuItem(option)
            if text in self._colors:
                color = self._colors[text]
            else:
                color = QtGui.QColor("#A9BBAE")
            option_.palette.setColor(QtGui.QPalette.Text, color)
            return self.baseStyle().drawControl(element, option_, painter, widget)
        return self.baseStyle().drawControl(element, option, painter, widget)

class MenuStyler():
    def __init__(self, menu):
        style = Style()
        style.setBaseStyle(menu.style())
        menu.setStyle(style)
        self._style = style
        self._menu = menu

    def setColor(self, key, color):
        if isinstance(key, str):
            self._style.setColor(key, color)
        elif isinstance(key, int):
            text = self._menu.actions()[key].text()
            self._style.setColor(text, color)
        else:
            raise ValueError("Key must be either int or string")

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)

    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))

    palette = app.palette()
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor("#18191C"))
    palette.setColor(QtGui.QPalette.Text, QtGui.QColor("#A9BBAE"))
    palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor("#A9BBAE"))
    palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor("#A9BBAE"))
    app.setPalette(palette)

    menu = QtWidgets.QMenu()
    menu.addAction("Mark As Read")
    menu.addSeparator()
    menu.addAction("Invite People")
    submenuMute = menu.addMenu("MuteServer")

    submenuMute.addAction("submenu")

    hideMuted = QtWidgets.QAction("Hide Muted Channels")
    hideMuted.setCheckable(True)
    menu.addAction(hideMuted)
    menu.addSeparator()
    menu.addAction("Leave Server")

    styler = MenuStyler(menu)
    styler.setColor("Invite People", QtGui.QColor("#3D6BC4"))
    styler.setColor("Leave Server", QtGui.QColor("#F04544"))
    
    menu.exec(QtCore.QPoint(100,100))

    app.exec()