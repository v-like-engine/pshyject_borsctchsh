import sys

from PyQt5.QtWidgets import QMainWindow


class MapCoder(QMainWindow, Ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
