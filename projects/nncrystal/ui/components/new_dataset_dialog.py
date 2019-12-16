import json
import os
from typing import List

import imantics
from PySide2 import QtWidgets
from .forms import new_dataset_dialog
from imantics import Dataset, Category, Image


class NewDatasetDialog(QtWidgets.QDialog, new_dataset_dialog.Ui_Dialog):

    def __init__(self, dir_path, parent=None):
        super().__init__(parent)
        self.dir_path = dir_path
        self.setupUi(self)
        self.configure_image_list()
        self.configure_actions()

    def configure_actions(self):
        self.action_add_images.triggered.connect(self.add_images)
        self.action_remove_images.triggered.connect(self.remove_images)
        self.copy_from_button_4.clicked.connect(self.copy_from)
        self.buttonBox.accepted.connect(self.confirm)
        self.buttonBox.rejected.connect(self.close)

    def configure_image_list(self):
        self.image_list.addAction(self.action_add_images)
        self.image_list.addAction(self.action_remove_images)

    def add_images(self):
        d = QtWidgets.QFileDialog(self)
        d.setFileMode(d.ExistingFiles)
        d.setWindowTitle("Select images")
        d.setNameFilter("Image files (*.jpg *.png)")
        d.exec_()
        self.image_list.clear()
        self.image_list.addItems(d.selectedFiles())

    def remove_images(self):
        items = self.image_list.selectedItems()
        count = len(items)
        ret = QtWidgets.QMessageBox.question(self, "Delete images", f"Confirm removing {count} image(s)?")
        if ret == QtWidgets.QMessageBox.Yes:
            for item in items:
                self.image_list.takeItem(self.image_list.row(item))

    def copy_from(self):
        d = QtWidgets.QFileDialog(self)
        d.setFileMode(d.ExistingFile)
        d.setWindowTitle("Select other dataset")
        d.setNameFilter("COCO dataset files (*.json *.txt)")
        d.exec_()

        with open(d.selectedFiles()[0], "r") as f:
            coco_obj = json.load(f)
        ds = Dataset.from_coco(coco_obj)
        cats: List[Category] = list(ds.categories.values())

        cat_str = ",".join([x.name for x in cats])
        self.categories_edit.setText(cat_str)

    def validate(self):
        name = self.dataset_name_edit.text()
        path = os.path.join(self.dir_path, f"{name}.json")
        if os.path.exists(path):
            QtWidgets.QMessageBox.warning(self, "Dataset exists", f'Path "{path}" exists!')
            return False

        categories = self.categories_edit.text()
        if categories.endswith(",") or len(categories) == 0:
            QtWidgets.QMessageBox.warning(self, "Category error", "Category definition is invalid")
            return False

        if self.image_list.count() == 0:
            QtWidgets.QMessageBox.warning(self, "Image set", "No image selected")
            return False

        return True

    def confirm(self):
        if not self.validate():
            return
        else:
            self.create_dataset()
            self.close()

    def create_dataset(self):
        dataset_name = self.dataset_name_edit.text()
        image_list = []
        for i in range(self.image_list.count()):
            image_list.append(self.image_list.item(i).text())

        ds = imantics.Dataset(dataset_name)
        _id = 0
        for image_path in image_list:
            image = Image.from_path(image_path)
            image.id = _id
            ds.add(image)
            _id += 1
        with open(os.path.join(self.dir_path, f"{dataset_name}.json"), "w") as f:
            json.dump(ds.coco(), f)
