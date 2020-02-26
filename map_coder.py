import sys

from PyQt5.QtWidgets import QMainWindow

from static_map import get_map
from ui.mapcoderwindow import Ui_MapWindow


class MapCoder(QMainWindow, Ui_MapWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.search_button.clicked.connect(self.search)

    def search(self):
        coords = self.search_edit.text().split()
        map_params = {
            "l": "map",
            "size": '450,450',
            "pt": "~".join(coords)}
        try:
            result_map = get_map(map_params)
            print(result_map)
        except Exception:
            print('error')
