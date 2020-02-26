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
        self.x_c = 55.777751
        self.y_c = 58.087718
        self.coords = str(self.x_c) + ',' + str(self.y_c)
        self.update_map(self.get_spn())

    def get_spn(self):
        spn = str(self.spn_x) + ',' + str(self.spn_y)
        return spn

    def search(self):
        self.coords = self.search_edit.text()
        self.x_c, self.y_c = self.coords.split(',')
        spn = self.get_spn()
        self.update_map(spn)
        # 37.677751,55.757718

    def update_map(self, spn, *pts):
        print(spn, self.coords)
        self.map_params = {
            "l": "map",
            "size": '450,450',
            "ll": self.coords,
            "spn": spn}
        # "pt": coords}
        self.draw_map()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.change_spn('+')
        if event.key() == Qt.Key_PageDown:
            self.change_spn('-')
        if event.key() == Qt.Key_Down:
            self.change_coord('v')
        if event.key() == Qt.Key_Up:
            self.change_coord('^')
        if event.key() == Qt.Key_Left:
            self.change_coord('<')
        if event.key() == Qt.Key_Right:
            self.change_coord('>')

    def change_spn(self, type_of_changing):
        change_x, change_y = 2, 2
        if type_of_changing == '+':
            self.spn_x *= change_x
            self.spn_y *= change_y
        if type_of_changing == '-':
            self.spn_x /= change_x
            self.spn_y /= change_y
        self.spn_x = round(self.spn_x, 4)
        self.spn_y = round(self.spn_y, 4)
        if self.spn_x == 0:
            self.spn_x = 0.0001
        elif self.spn_x > 100:
            self.spn_x = 99.0000
        if self.spn_y == 0:
            self.spn_y = 0.0001
        elif self.spn_y > 100:
            self.spn_y = 99.0000
        self.update_map(self.get_spn())

    def change_coord(self, type_of_changing):
        change_x, change_y = 0.01, 0.01
        if type_of_changing == '>':
            self.x_c += change_x
        if type_of_changing == '<':
            self.x_c -= change_x
        if type_of_changing == '^':
            self.y_c += change_y
        if type_of_changing == 'v':
            self.y_c -= change_y
        self.x_c = round(self.x_c, 6)
        self.y_c = round(self.y_c, 6)
        self.coords = str(self.x_c) + ',' + str(self.y_c)
        self.update_map(self.get_spn())

    def draw_map(self):
        try:
            result_map = get_map(self.map_params)
            pm = QPixmap()
            pm.loadFromData(result_map)
            pm = pm.scaledToWidth(1280)
            self.image_view_label.setPixmap(pm)
        except Exception:
            print('error')
