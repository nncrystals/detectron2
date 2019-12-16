import json
import logging
import os
from typing import Any

import PySide2
import imantics
from PySide2 import QtCore, QtWidgets


class DatasetListModel(QtWidgets.QFileSystemModel):
    def __init__(self, dataset_path="./datasets", parent=None):
        super().__init__(parent)
        self.setRootPath(os.path.abspath(dataset_path))
        self.setNameFilters(["*.json"])
        self.dataset_path = dataset_path


class DatasetContentModel(QtCore.QAbstractTableModel):
    dataset: imantics.Dataset
    headers = ["ID", "Annotation", "Image"]

    def __init__(self, dataset_path: str, parent=None):
        super().__init__(parent)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.dataset_path = dataset_path
        self.dataset = None
        self.update()

    def columnCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int:
        return len(self.headers)

    def rowCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int:
        return len(self.dataset.images)

    def headerData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int = ...) -> Any:
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.headers[section]

    def data(self, index: PySide2.QtCore.QModelIndex, role: int = ...) -> Any:
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            data: imantics.Image = self.dataset.images[row]
            col = index.column()

            if col == 0:
                return row
            elif col == 1:
                return len(data.annotations)
            elif col == 2:
                return data.path
            else:
                raise ValueError("Dataset column out of range")

    def update(self):
        # TODO: upstream bug
        imantics.Dataset.annotations = {}
        imantics.Dataset.categories = {}
        imantics.Dataset.images = {}

        if self.dataset_path and os.path.exists(self.dataset_path):
            with open(self.dataset_path, "r") as f:
                coco_obj = json.load(f)
            self.dataset = imantics.Dataset.from_coco(coco_obj)
        else:
            self.dataset = imantics.Dataset("defaults")

    def get_image(self, idx: int):
        return self.dataset.images[idx]
