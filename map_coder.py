import sys

from PyQt5.QtWidgets import QMainWindow

from ui.mapcoderwindow import MapCoderUi


class MapCoder(QMainWindow, MapCoderUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
