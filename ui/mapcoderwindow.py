# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapcoderwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MapWindow(object):
    def setupUi(self, MapWindow):
        MapWindow.setObjectName("MapWindow")
        MapWindow.resize(1280, 720)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        MapWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MapWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stacked_view = QtWidgets.QStackedWidget(self.centralwidget)
        self.stacked_view.setGeometry(QtCore.QRect(0, 0, 1281, 701))
        self.stacked_view.setObjectName("stacked_view")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.image_view_label = QtWidgets.QLabel(self.page)
        self.image_view_label.setGeometry(QtCore.QRect(0, 0, 1280, 690))
        self.image_view_label.setText("")
        self.image_view_label.setObjectName("image_view_label")
        self.slider_size = QtWidgets.QSlider(self.page)
        self.slider_size.setGeometry(QtCore.QRect(20, 130, 22, 431))
        self.slider_size.setMinimum(0)
        self.slider_size.setMaximum(100)
        self.slider_size.setProperty("value", 50)
        self.slider_size.setOrientation(QtCore.Qt.Vertical)
        self.slider_size.setObjectName("slider_size")
        self.search_edit = QtWidgets.QLineEdit(self.page)
        self.search_edit.setGeometry(QtCore.QRect(40, 20, 361, 31))
        self.search_edit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.search_edit.setInputMask("")
        self.search_edit.setText("")
        self.search_edit.setObjectName("search_edit")
        self.search_button = QtWidgets.QPushButton(self.page)
        self.search_button.setGeometry(QtCore.QRect(410, 20, 75, 31))
        self.search_button.setObjectName("search_button")
        self.view_mode = QtWidgets.QPushButton(self.page)
        self.view_mode.setGeometry(QtCore.QRect(20, 630, 61, 51))
        self.view_mode.setObjectName("view_mode")
        self.result_view = QtWidgets.QStackedWidget(self.page)
        self.result_view.setGeometry(QtCore.QRect(1000, 0, 271, 691))
        self.result_view.setObjectName("result_view")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.result_text = QtWidgets.QLabel(self.page_3)
        self.result_text.setGeometry(QtCore.QRect(20, 70, 251, 51))
        self.result_text.setWordWrap(True)
        self.result_text.setObjectName("result_text")
        self.result_view.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.result_view.addWidget(self.page_4)
        self.reset_result = QtWidgets.QPushButton(self.page)
        self.reset_result.setEnabled(False)
        self.reset_result.setGeometry(QtCore.QRect(20, 572, 61, 51))
        self.reset_result.setCheckable(False)
        self.reset_result.setObjectName("reset_result")
        self.stacked_view.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stacked_view.addWidget(self.page_2)
        MapWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MapWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 25))
        self.menubar.setObjectName("menubar")
        MapWindow.setMenuBar(self.menubar)

        self.retranslateUi(MapWindow)
        self.stacked_view.setCurrentIndex(0)
        self.result_view.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MapWindow)

    def retranslateUi(self, MapWindow):
        _translate = QtCore.QCoreApplication.translate
        MapWindow.setWindowTitle(_translate("MapWindow", "MapCoder v0.1 by borsctchsh team"))
        self.search_edit.setPlaceholderText(_translate("MapWindow", "Что ищем?.."))
        self.search_button.setText(_translate("MapWindow", "Найти!"))
        self.view_mode.setText(_translate("MapWindow", "Вид"))
        self.result_text.setText(_translate("MapWindow", "Result"))
        self.reset_result.setText(_translate("MapWindow", "Сброс"))
