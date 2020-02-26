import sys

from PyQt5.QtWidgets import QApplication

from map_coder import MapCoder


app = QApplication(sys.argv)
mainwindow = MapCoder()
mainwindow.show()
sys.exit(app.exec_())