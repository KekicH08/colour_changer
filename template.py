from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Final_interface(object):
    def setupUi(self, Final_interface):
        if not Final_interface.objectName():
            Final_interface.setObjectName(u"Final_interface")
        Final_interface.resize(463, 479)
        Final_interface.setMaximumSize(684, 519)
        self.gridLayout = QGridLayout(Final_interface)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(16, 16, 16, 16)
        self.find = QPushButton(Final_interface)
        self.find.setObjectName(u"find")

        self.gridLayout.addWidget(self.find, 1, 1, 1, 1)

        self.Green = QSlider(Final_interface)
        self.Green.setObjectName(u"Green")
        self.Green.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.Green, 15, 0, 1, 1)

        self.label_4 = QLabel(Final_interface)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 1)

        self.find_name = QLineEdit(Final_interface)
        self.find_name.setObjectName(u"find_name")

        self.gridLayout.addWidget(self.find_name, 0, 1, 1, 1)

        self.label_3 = QLabel(Final_interface)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)

        self.setups = QPushButton(Final_interface)
        self.setups.setObjectName(u"setups")

        self.gridLayout.addWidget(self.setups, 3, 0, 1, 1)

        self.label_5 = QLabel(Final_interface)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 12, 0, 1, 1)

        self.Brightness = QSlider(Final_interface)
        self.Brightness.setObjectName(u"Brightness")
        self.Brightness.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.Brightness, 5, 0, 1, 1)

        self.label_2 = QLabel(Final_interface)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)

        self.accept = QPushButton(Final_interface)
        self.accept.setObjectName(u"accept")

        self.gridLayout.addWidget(self.accept, 1, 0, 1, 1)

        self.Red = QSlider(Final_interface)
        self.Red.setObjectName(u"Red")
        self.Red.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.Red, 13, 0, 1, 1)

        self.Blue = QSlider(Final_interface)
        self.Blue.setObjectName(u"Blue")
        self.Blue.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.Blue, 17, 0, 1, 1)

        self.Saturation = QSlider(Final_interface)
        self.Saturation.setObjectName(u"Saturation")
        self.Saturation.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.Saturation, 9, 0, 1, 1)

        self.create_setup = QPushButton(Final_interface)
        self.create_setup.setObjectName(u"create_setup")

        self.gridLayout.addWidget(self.create_setup, 1, 2, 1, 1)

        self.new_name = QLineEdit(Final_interface)
        self.new_name.setObjectName(u"new_name")

        self.gridLayout.addWidget(self.new_name, 0, 2, 1, 1)

        self.Warmth = QSlider(Final_interface)
        self.Warmth.setObjectName(u"Warmth")
        self.Warmth.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.Warmth, 11, 0, 1, 1)

        self.label = QLabel(Final_interface)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.save = QPushButton(Final_interface)
        self.save.setObjectName(u"save")

        self.gridLayout.addWidget(self.save, 2, 0, 1, 1)

        self.Contrast = QSlider(Final_interface)
        self.Contrast.setObjectName(u"Contrast")
        self.Contrast.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.Contrast, 7, 0, 1, 1)

        self.label_6 = QLabel(Final_interface)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 14, 0, 1, 1)

        self.choose_pic_button = QPushButton(Final_interface)
        self.choose_pic_button.setObjectName(u"choose_pic_button")

        self.gridLayout.addWidget(self.choose_pic_button, 0, 0, 1, 1)

        self.label_7 = QLabel(Final_interface)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 16, 0, 1, 1)

        self.use = QPushButton(Final_interface)
        self.use.setObjectName(u"use")

        self.gridLayout.addWidget(self.use, 17, 1, 1, 2)

        self.name_use = QLineEdit(Final_interface)
        self.name_use.setObjectName(u"name_use")

        self.gridLayout.addWidget(self.name_use, 16, 1, 1, 2)

        self.table = QTableWidget(Final_interface)
        self.table.setObjectName(u"table")

        self.gridLayout.addWidget(self.table, 2, 1, 14, 2)


        self.retranslateUi(Final_interface)

        QMetaObject.connectSlotsByName(Final_interface)
    # setupUi

    def retranslateUi(self, Final_interface):
        Final_interface.setWindowTitle(QCoreApplication.translate("Final_interface", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0446\u0432\u0435\u0442\u0430", None))
        self.find.setText(QCoreApplication.translate("Final_interface", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.label_4.setText(QCoreApplication.translate("Final_interface", u"<html><head/><body><p align=\"center\">\u0422\u0435\u043f\u043b\u043e\u0442\u0430</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Final_interface", u"<html><head/><body><p align=\"center\">\u041d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u043e\u0441\u0442\u044c</p></body></html>", None))
        self.setups.setText(QCoreApplication.translate("Final_interface", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u043d\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_5.setText(QCoreApplication.translate("Final_interface", u"<html><head/><body><p align=\"center\">\u041a\u0440\u0430\u0441\u043d\u044b\u0439</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Final_interface", u"<html><head/><body><p align=\"center\">\u041a\u043e\u043d\u0442\u0440\u0430\u0441\u0442</p></body></html>", None))
        self.accept.setText(QCoreApplication.translate("Final_interface", u"\u041f\u0440\u043d\u0438\u044f\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.create_setup.setText(QCoreApplication.translate("Final_interface", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0443", None))
        self.label.setText(QCoreApplication.translate("Final_interface", u"<html><head/><body><p align=\"center\">\u042f\u0440\u043a\u043e\u0441\u0442\u044c</p></body></html>", None))
        self.save.setText(QCoreApplication.translate("Final_interface", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a", None))
        self.label_6.setText(QCoreApplication.translate("Final_interface", u"<html><head/><body><p align=\"center\">\u0417\u0435\u043b\u0435\u043d\u044b\u0439</p></body></html>", None))
        self.choose_pic_button.setText(QCoreApplication.translate("Final_interface", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443", None))
        self.label_7.setText(QCoreApplication.translate("Final_interface", u"<html><head/><body><p align=\"center\">\u0421\u0438\u043d\u0438\u0439</p></body></html>", None))
        self.use.setText(QCoreApplication.translate("Final_interface", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0443", None))
    # retranslateUi
