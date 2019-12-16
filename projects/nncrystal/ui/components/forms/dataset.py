# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wuyuanyi/nnProject/detectron2/projects/nncrystal/ui/components/forms/dataset.ui',
# licensing of '/home/wuyuanyi/nnProject/detectron2/projects/nncrystal/ui/components/forms/dataset.ui' applies.
#
# Created: Mon Dec 16 00:12:43 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dataset(object):
    def setupUi(self, Dataset):
        Dataset.setObjectName("Dataset")
        Dataset.resize(763, 533)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dataset)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dataset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dataset_list = QtWidgets.QTreeView(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataset_list.sizePolicy().hasHeightForWidth())
        self.dataset_list.setSizePolicy(sizePolicy)
        self.dataset_list.setMinimumSize(QtCore.QSize(0, 0))
        self.dataset_list.setBaseSize(QtCore.QSize(0, 0))
        self.dataset_list.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.dataset_list.setObjectName("dataset_list")
        self.verticalLayout_3.addWidget(self.dataset_list)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.groupBox_2 = QtWidgets.QGroupBox(Dataset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.content_table = QtWidgets.QTableView(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content_table.sizePolicy().hasHeightForWidth())
        self.content_table.setSizePolicy(sizePolicy)
        self.content_table.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.content_table.setObjectName("content_table")
        self.content_table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.content_table)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.action_add_dataset = QtWidgets.QAction(Dataset)
        self.action_add_dataset.setObjectName("action_add_dataset")
        self.action_remove_dataset = QtWidgets.QAction(Dataset)
        self.action_remove_dataset.setObjectName("action_remove_dataset")
        self.action_enter_annotation = QtWidgets.QAction(Dataset)
        self.action_enter_annotation.setObjectName("action_enter_annotation")
        self.action_replace_image_directory = QtWidgets.QAction(Dataset)
        self.action_replace_image_directory.setObjectName("action_replace_image_directory")

        self.retranslateUi(Dataset)
        QtCore.QMetaObject.connectSlotsByName(Dataset)

    def retranslateUi(self, Dataset):
        Dataset.setWindowTitle(QtWidgets.QApplication.translate("Dataset", "Form", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Dataset", "Datasets", None, -1))
        self.dataset_list.setWhatsThis(QtWidgets.QApplication.translate("Dataset", "<html><head/><body><p>Dataset List</p></body></html>", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("Dataset", "Data", None, -1))
        self.action_add_dataset.setText(QtWidgets.QApplication.translate("Dataset", "&Add Dataset", None, -1))
        self.action_remove_dataset.setText(QtWidgets.QApplication.translate("Dataset", "&Remove Dataset", None, -1))
        self.action_enter_annotation.setText(QtWidgets.QApplication.translate("Dataset", "&Enter annotation mode", None, -1))
        self.action_replace_image_directory.setText(QtWidgets.QApplication.translate("Dataset", "&Replace image directory", None, -1))

