import PySide2
from PySide2 import QtWidgets
from .menu_bar import MainWindowMenuBar
from .forms.about_dialog import Ui_about_dialog


class AboutDialog(QtWidgets.QDialog, Ui_about_dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.exitButton.clicked.connect(self.close)

