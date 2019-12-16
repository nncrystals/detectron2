from .forms import configs
from PySide2 import QtWidgets


class ConfigWidget(QtWidgets.QWidget, configs.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
