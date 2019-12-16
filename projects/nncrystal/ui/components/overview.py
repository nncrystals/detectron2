from PySide2 import QtWidgets
from .forms import overview


class OverviewWidget(QtWidgets.QWidget, overview.Ui_Overview):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)