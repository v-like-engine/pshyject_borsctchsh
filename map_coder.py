import io
import sys
import urllib.request

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow

from static_map import get_map
from ui.mapcoderwindow import Ui_MapWindow


class MapCoder(QMainWindow, Ui_MapWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.search_button.clicked.connect(self.search)
        self.spn_x = 0.001
        self.spn_y = 0.001

    def search(self):
        coords = self.search_edit.text().split()
        spn = str(self.spn_x) + ',' + str(self.spn_y)
        print(spn)
        self.map_params = {
            "l": "map",
            "size": '450,450',
            "ll": coords,
            "spn": spn,
            "pt": coords}
        self.draw_map()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.change_spn('+')
        if event.key() == Qt.Key_PageDown:
            self.change_spn('-')

    def change_spn(self, type_of_changing):
        change_x, change_y = 10, 10
        if type_of_changing == '+':
            self.spn_x *= change_x
            self.spn_y *= change_y
        if type_of_changing == '-':
            self.spn_x //= change_x
            self.spn_y //= change_y
        self.spn_x = round(self.spn_x, 3)
        self.spn_y = round(self.spn_y, 3)
        self.search()

    def draw_map(self):
        try:
            result_map = get_map(self.map_params)
            pm = QPixmap()
            pm.loadFromData(result_map)
            pm = pm.scaledToWidth(1280)
            self.image_view_label.setPixmap(pm)
        except Exception:
            print('error')
