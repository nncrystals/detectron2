# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wuyuanyi/nnProject/detectron2/projects/nncrystal/ui/components/forms/overview.ui',
# licensing of '/home/wuyuanyi/nnProject/detectron2/projects/nncrystal/ui/components/forms/overview.ui' applies.
#
# Created: Thu Dec 12 22:21:40 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Overview(object):
    def setupUi(self, Overview):
        Overview.setObjectName("Overview")
        Overview.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Overview)
        self.gridLayout.setObjectName("gridLayout")
        self.summary = QtWidgets.QTextBrowser(Overview)
        self.summary.setObjectName("summary")
        self.gridLayout.addWidget(self.summary, 0, 0, 1, 1)

        self.retranslateUi(Overview)
        QtCore.QMetaObject.connectSlotsByName(Overview)

    def retranslateUi(self, Overview):
        Overview.setWindowTitle(QtWidgets.QApplication.translate("Overview", "Form", None, -1))
        self.summary.setHtml(QtWidgets.QApplication.translate("Overview", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Summary</span></p></body></html>", None, -1))

