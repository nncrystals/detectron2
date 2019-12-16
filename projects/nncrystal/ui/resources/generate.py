import sys
import os
import subprocess as sp
import logging
import glob
from ui.utils.depgen import PySide2ResourceGenerator

logging.root.setLevel(logging.DEBUG)


if __name__ == '__main__':
    form_dir = os.path.dirname(__file__)
    qrc_files = glob.glob(os.path.join(form_dir, "*.qrc"))

    for qrc_file in qrc_files:
        PySide2ResourceGenerator(qrc_file).make()
