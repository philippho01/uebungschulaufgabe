import random

from PyQt6.QtCore import QTimer, pyqtSlot, pyqtSignal
from PyQt6.QtWidgets import QWidget, QSlider, QHBoxLayout, QGridLayout, QLabel

from UbungChart import UbungChart
from DatumChart import DatumChart

class CentralWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ubungchart = UbungChart(parent)
        self.datumchart = DatumChart(parent)

        layout = QGridLayout()

        layout.addWidget(self.ubungchart)
        layout.addWidget(self.datumchart)

        self.setLayout(layout)