import sys
import os
import subprocess as sp
import logging
import glob
from ui.utils.depgen import PySide2FormGenerator
logging.root.setLevel(logging.DEBUG)

if __name__ == '__main__':
    form_dir = os.path.dirname(__file__)
    ui_files = glob.glob(os.path.join(form_dir, "*.ui"))
    for ui_file in ui_files:
        PySide2FormGenerator(ui_file).make()


