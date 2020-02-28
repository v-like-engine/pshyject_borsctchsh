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
        self.z = 10
        self.x_c = 55.777751
        self.y_c = 58.087718
        self.coords = str(self.x_c) + ',' + str(self.y_c)
        self.update_map()

    def search(self):
        self.coords = self.search_edit.text()
        self.x_c, self.y_c = self.coords.split(',')
        self.update_map()
        # 37.677751,55.757718

    def update_map(self, *pts):
        self.map_params = {
            "l": "map",
            "size": '450,450',
            "ll": self.coords,
            'z': str(self.z)}
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
        change = 1
        if type_of_changing == '+':
            self.z += 1
        if type_of_changing == '-':
            self.z -= 1
        if self.z > 17:
            self.z = 17
        elif self.z < 1:
            self.z = 1
        self.update_map()

    def change_coord(self, type_of_changing):
        change_x, change_y = self.z * self.x_c, self.z * self.y_c
        if type_of_changing == '>':
            self.x_c += change_x
        if type_of_changing == '<':
            self.x_c -= change_x
        if type_of_changing == '^':
            self.y_c += change_y
        if type_of_changing == 'v':
            self.y_c -= change_y
        self.coords = str(self.x_c) + ',' + str(self.y_c)
        self.update_map()

    def draw_map(self):
        try:
            result_map = get_map(self.map_params)
            pm = QPixmap()
            pm.loadFromData(result_map)
            pm = pm.scaledToWidth(1280)
            self.image_view_label.setPixmap(pm)
        except Exception:
            print('error')
