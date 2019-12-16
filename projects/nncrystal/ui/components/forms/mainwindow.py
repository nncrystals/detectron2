# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wuyuanyi/nnProject/detectron2/projects/nncrystal/ui/components/forms/mainwindow.ui',
# licensing of '/home/wuyuanyi/nnProject/detectron2/projects/nncrystal/ui/components/forms/mainwindow.ui' applies.
#
# Created: Mon Dec 16 00:46:12 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/app_icon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_overview = QtWidgets.QWidget()
        self.tab_overview.setObjectName("tab_overview")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_overview)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = OverviewWidget(self.tab_overview)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_overview, "")
        self.tab_dataset = QtWidgets.QWidget()
        self.tab_dataset.setObjectName("tab_dataset")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_dataset)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = DatasetWidget(self.tab_dataset)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2.addWidget(self.widget_2)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_dataset, "")
        self.tab_config = QtWidgets.QWidget()
        self.tab_config.setObjectName("tab_config")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_config)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_3 = ConfigWidget(self.tab_config)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3.addWidget(self.widget_3)
        self.tabWidget.addTab(self.tab_config, "")
        self.tab_train = QtWidgets.QWidget()
        self.tab_train.setObjectName("tab_train")
        self.tabWidget.addTab(self.tab_train, "")
        self.tab_evaluation = QtWidgets.QWidget()
        self.tab_evaluation.setObjectName("tab_evaluation")
        self.tabWidget.addTab(self.tab_evaluation, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuDebug = QtWidgets.QMenu(self.menubar)
        self.menuDebug.setObjectName("menuDebug")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.actionShow_states = QtWidgets.QAction(MainWindow)
        self.actionShow_states.setObjectName("actionShow_states")
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menuAbout.addAction(self.action_About)
        self.menuDebug.addAction(self.actionShow_states)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuDebug.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "NNCrystal Trainer", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_overview), QtWidgets.QApplication.translate("MainWindow", "&Overview", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dataset), QtWidgets.QApplication.translate("MainWindow", "&Dataset", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_config), QtWidgets.QApplication.translate("MainWindow", "&Configuration", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_train), QtWidgets.QApplication.translate("MainWindow", "&Train", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_evaluation), QtWidgets.QApplication.translate("MainWindow", "&Evaluation", None, -1))
        self.menu_File.setTitle(QtWidgets.QApplication.translate("MainWindow", "&File", None, -1))
        self.menuAbout.setTitle(QtWidgets.QApplication.translate("MainWindow", "&About", None, -1))
        self.menuDebug.setTitle(QtWidgets.QApplication.translate("MainWindow", "Debug", None, -1))
        self.action_Exit.setText(QtWidgets.QApplication.translate("MainWindow", "&Exit", None, -1))
        self.action_About.setText(QtWidgets.QApplication.translate("MainWindow", "&About", None, -1))
        self.actionShow_states.setText(QtWidgets.QApplication.translate("MainWindow", "Display States", None, -1))

from components.config import ConfigWidget
from components.dataset import DatasetWidget
from components.overview import OverviewWidget
import icons_rc
