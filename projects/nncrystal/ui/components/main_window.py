import os
import sys

from PySide2 import QtWidgets
from .forms.mainwindow import Ui_MainWindow
from .about import AboutDialog
from ui.state import S


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(800, 600)
        self._configure_debug_menu()
        self._configure_actions()

    def _configure_debug_menu(self):
        if not os.environ.get("DEBUG"):
            self.menuDebug.hide()

    def _configure_actions(self):
        self.action_About.triggered.connect(self._show_about)
        self.action_Exit.triggered.connect(sys.exit)

        # debug actions
        self.actionShow_states.triggered.connect(self._display_states)

    def _show_about(self):
        m = AboutDialog(self)
        m.show()

    def _display_states(self):
        import json
        msgbox = QtWidgets.QMessageBox()
        msgbox.setText(json.dumps(S.get_state_dict(), indent=4))
        msgbox.exec_()

    def _new_project(self):
        d = QtWidgets.QFileDialog(self, "Select location to create new project", os.getcwd())
        d.setFileMode(d.AnyFile)
        d.exec_()
        print(d.selectedFiles())