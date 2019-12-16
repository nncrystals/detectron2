# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wuyuanyi/nnProject/detectron2/projects/nncrystal/ui/components/forms/new_dataset_dialog.ui',
# licensing of '/home/wuyuanyi/nnProject/detectron2/projects/nncrystal/ui/components/forms/new_dataset_dialog.ui' applies.
#
# Created: Sun Dec 15 22:20:21 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 295)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/app_icon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.datasetNameLabel = QtWidgets.QLabel(Dialog)
        self.datasetNameLabel.setObjectName("datasetNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.datasetNameLabel)
        self.dataset_name_edit = QtWidgets.QLineEdit(Dialog)
        self.dataset_name_edit.setObjectName("dataset_name_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dataset_name_edit)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.categories_edit = QtWidgets.QLineEdit(Dialog)
        self.categories_edit.setObjectName("categories_edit")
        self.horizontalLayout_4.addWidget(self.categories_edit)
        self.copy_from_button_4 = QtWidgets.QPushButton(Dialog)
        self.copy_from_button_4.setObjectName("copy_from_button_4")
        self.horizontalLayout_4.addWidget(self.copy_from_button_4)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.image_list = QtWidgets.QListWidget(Dialog)
        self.image_list.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.image_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.image_list.setObjectName("image_list")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.image_list)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.action_add_images = QtWidgets.QAction(Dialog)
        self.action_add_images.setObjectName("action_add_images")
        self.action_remove_images = QtWidgets.QAction(Dialog)
        self.action_remove_images.setObjectName("action_remove_images")
        self.datasetNameLabel.setBuddy(self.dataset_name_edit)
        self.label.setBuddy(self.categories_edit)
        self.label_2.setBuddy(self.image_list)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "New dialog", None, -1))
        self.datasetNameLabel.setText(QtWidgets.QApplication.translate("Dialog", "&Dataset name", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "&Categories", None, -1))
        self.copy_from_button_4.setText(QtWidgets.QApplication.translate("Dialog", "Copy from", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "&Images", None, -1))
        self.action_add_images.setText(QtWidgets.QApplication.translate("Dialog", "&Add images", None, -1))
        self.action_remove_images.setText(QtWidgets.QApplication.translate("Dialog", "&Remove images", None, -1))

import icons_rc
