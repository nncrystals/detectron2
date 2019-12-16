from PySide2 import QtWidgets, QtGui, QtCore
from imantics import Image

from .forms import annotator
from .annotator_canvas import AnnotatorCanvas


class Annotator(QtWidgets.QDialog, annotator.Ui_Dialog):

    def __init__(self, image: Image, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.scrollBars = {
            QtCore.Qt.Vertical: self.scrollArea.verticalScrollBar(),
            QtCore.Qt.Horizontal: self.scrollArea.horizontalScrollBar(),
        }

        canvas: AnnotatorCanvas = self.canvas_widget
        canvas.scrollRequest.connect(self.scrollRequest)
        canvas.zoomRequest.connect(self.zoomRequest)

        canvas.setEditing(False)
        canvas.createMode = "polygon"

        self.image = image

        image = QtGui.QImage(image.path)
        pixmap = QtGui.QPixmap.fromImage(image)
        canvas.loadPixmap(pixmap)
        canvas.adjustSize()

    def scrollRequest(self, delta, orientation):
        units = - delta * 0.1  # natural scroll
        bar = self.scrollBars[orientation]
        bar.setValue(bar.value() + bar.singleStep() * units)

    def zoomRequest(self, delta, pos):
        canvas_width_old = self.canvas_widget.width()
        units = 1.1
        if delta < 0:
            units = 0.9
        self.paintCanvas(units)

        canvas_width_new = self.canvas_widget.width()
        if canvas_width_old != canvas_width_new:
            canvas_scale_factor = canvas_width_new / canvas_width_old

            x_shift = round(pos.x() * canvas_scale_factor) - pos.x()
            y_shift = round(pos.y() * canvas_scale_factor) - pos.y()

            self.scrollBars[QtCore.Qt.Horizontal].setValue(
                self.scrollBars[QtCore.Qt.Horizontal].value() + x_shift)
            self.scrollBars[QtCore.Qt.Vertical].setValue(
                self.scrollBars[QtCore.Qt.Vertical].value() + y_shift)

    def paintCanvas(self, scale):
        self.canvas_widget.scale = self.canvas_widget.scale * scale
        self.canvas_widget.adjustSize()
        self.canvas_widget.update()