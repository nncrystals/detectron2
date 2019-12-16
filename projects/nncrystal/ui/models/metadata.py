from typing import Any

import PySide2
from PySide2 import QtWidgets, QtCore


class MetaData:
    def __init__(self, name, id):
        self.name = name


class MetaDataCollection:
    def __init__(self):
        self._meta = []
        self._last_id = 0

    def add_meta(self, name):
        self._meta.append(MetaData(name, self._last_id))
        self._last_id += 1

    def remove_meta(self, index):
        self._meta.pop(index)

    def get_meta(self, index):
        return self._meta[index]

    def __len__(self):
        return len(self._meta)

    def __getitem__(self, item):
        return self._meta[item]

    def get_model(self, parent=None):
        return MetaDataTableModel(self, parent)


class MetaDataTableModel(QtCore.QAbstractTableModel):
    def __init__(self, metadata_collection: MetaDataCollection, parent=None):
        super().__init__(parent)
        self.metadata_collection = metadata_collection

    def flags(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.Qt.ItemFlags:
        if index.column() == 0:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        elif index.column() == 1:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    def columnCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int:
        return 2

    def rowCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int:
        return len(self.metadata_collection)

    def setData(self, index: PySide2.QtCore.QModelIndex, value: Any, role: int = ...) -> bool:
        if index.column() == 1:
            self.metadata_collection[index.row()].name = value

        return True

    def headerData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int = ...) -> Any:
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            if section == 0:
                return "ID"
            else:
                return "Name"

    def data(self, index: PySide2.QtCore.QModelIndex, role: int = ...) -> Any:
        if role != QtCore.Qt.DisplayRole:
            return

        column = index.column()
        if column == 0:
            return index.row()

        elif column == 1:
            meta: MetaData = self.metadata_collection[index.row()]
            return meta.name
