import json
import logging
import os

import imantics
from PySide2 import QtWidgets, QtCore
from send2trash import send2trash
from ui.models.dataset import DatasetListModel, DatasetContentModel
from .annotator import Annotator
from .forms import dataset
from .new_dataset_dialog import NewDatasetDialog
from utils.dataset_utils import replace_image_base_dir


class DatasetWidget(QtWidgets.QWidget, dataset.Ui_Dataset):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.configure_dataset_list_context_menu()
        self.configure_content_table_context_menu()
        self.configure_actions()

        self.dataset_model = DatasetListModel(parent=self)
        self.content_model = DatasetContentModel(None)  # default

        self.configure_dataset_list_view()
        self.configure_dataset_detail_table_view()

        self.logger = logging.getLogger(self.__class__.__name__)

    # View configurations
    def configure_dataset_list_view(self):
        self.dataset_list.setModel(self.dataset_model)
        self.dataset_list.setRootIndex(self.dataset_model.index(self.dataset_model.dataset_path))
        [self.dataset_list.hideColumn(x) for x in range(1, self.dataset_model.columnCount())]

        self.dataset_list.doubleClicked.connect(self._dataset_selected)

    def configure_dataset_detail_table_view(self):
        self.content_table.setModel(self.content_model)

    # Context menu configurations

    def configure_dataset_list_context_menu(self):
        self.dataset_list.addAction(self.action_add_dataset)
        self.dataset_list.addAction(self.action_remove_dataset)

    def configure_content_table_context_menu(self):
        self.content_table.addAction(self.action_enter_annotation)
        self.content_table.addAction(self.action_replace_image_directory)

    def configure_actions(self):
        self.action_add_dataset.triggered.connect(self._add_dataset)
        self.action_remove_dataset.triggered.connect(self._remove_dataset)
        self.action_replace_image_directory.triggered.connect(self._replace_image_directory)
        self.action_enter_annotation.triggered.connect(self.show_annotation_dialog)
        self.content_table.doubleClicked.connect(self.show_annotation_dialog)

    def _add_dataset(self):
        path = self.dataset_model.filePath(self.dataset_list.currentIndex())
        if not os.path.isdir(path):
            path = os.path.dirname(path)

        d = NewDatasetDialog(path, self)
        d.exec_()

    def _remove_dataset(self):
        sel = self.dataset_list.selectedIndexes()
        if len(sel) == 0:
            return

        sel = sel[0]
        ds = self.dataset_model.filePath(self.dataset_list.currentIndex())

        if os.path.isfile(ds) and ds.endswith(".json"):

            yes = QtWidgets.QMessageBox.question(self, "Delete dataset", f"delete {ds}?")

            if yes == QtWidgets.QMessageBox.Yes:
                send2trash(ds)

    def _add_metadata(self):
        self.metadata.add_meta("Name")
        self.metadata_model.endResetModel()

    def _remove_metadata(self):
        try:
            idx = self.meta_table.selectedIndexes()
            if not idx:
                return
            self.metadata.remove_meta(idx[0].row())
            self.metadata_model.endResetModel()
        except Exception as e:
            self.logger.exception("Failed to remove metadata", exc_info=e)

    def _dataset_selected(self, index: QtCore.QModelIndex):
        current = self.dataset_model.filePath(self.dataset_list.currentIndex())
        self.load_dataset(current)

    def load_dataset(self, dataset_path):
        if os.path.isfile(dataset_path) and dataset_path.endswith(".json"):
            self.content_model = DatasetContentModel(dataset_path)
            self.groupBox_2.setTitle(dataset_path)
            self.content_table.setModel(self.content_model)

    def _replace_image_directory(self):
        dataset_path = self.content_model.dataset_path

        d = QtWidgets.QFileDialog(self)
        d.setFileMode(d.DirectoryOnly)
        d.exec_()

        selected_dir = d.selectedFiles()[0]

        with open(dataset_path, "r") as f:
            coco_obj = json.load(f)
        coco_obj = replace_image_base_dir(coco_obj, selected_dir)
        with open(dataset_path, "w") as f:
            json.dump(coco_obj, f)
        self.load_dataset(dataset_path)

    def show_annotation_dialog(self, index=None):
        index = index or self.content_table.selectedIndexes()
        index: QtCore.QModelIndex
        image = index.model().get_image(index.row())
        if not os.path.exists(image.path):
            QtWidgets.QMessageBox.warning(self, "Failed to load the image",
                                          f"Failed to load {image.path}. "
                                          "Please use 'replace image directory' in the image list"
                                          )
            return

        d = Annotator(image, self)
        d.exec_()
