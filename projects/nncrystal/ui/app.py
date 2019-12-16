import sys
import os
import logging
logging.root.setLevel(logging.INFO)

def configure_import_path():
    sys.path.append(os.path.join(os.path.dirname(__file__), "resources"))
    sys.path.append(os.path.join(os.path.dirname(__file__)))


configure_import_path()

from PySide2.QtWidgets import QApplication
from ui.components.main_window import MainWindow
from ui.state import S

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()
