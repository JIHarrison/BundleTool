from __future__ import print_function
import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtGui import QIcon, QValidator, QRegExpValidator, QActionEvent
from PyQt5.QtCore import pyqtSlot, QVariant, QStringListModel, pyqtBoundSignal
from mailmerge import MailMerge
import itertools
import pandas as pd
import datetime

# tuples for later use, modularability(if this isn't a word I made it one, deal with it)
# this will possibly allow for someone to edit the script so they can dynamically add options for every field
master_tup = (
'TubeSheet Material', 'TubeSheet Diameter', 'Bolt Circle', 'Number of Bolt Holes', '# Tubeholes', 'Tube Material',
'Tube OD', 'Overall Length', 'Single or Double Wall', '# of Tubes', '# of Bends', '# of Baffles', 'Cost of Baffles')
# tubesheet_material_tup = ('Copper', 'Nickel Plated', 'Copper-Nickel', 'Naval Brass', 'Carbon Steel',)
# tubesheet_diameter_tup = ('5"', '6"', '8"', '10"', '12"', '14"', '16"', '18"', '20"', '22"', '24"')
# tube_material_tup = ('copper', 'Copper-Nickel')
# tube_OD_tup = ('1/2"', '3/4"', '1 - 1/4"')
# number_of_baffles_tup = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

final_list = ["", "", "", "", "", "", "", "", "", "", "", "", ""]

#misc_items = {'Tubesheet': [tubesheet_final], 'Tubes': [], 'Baffles': [], 'Gaskets1': [], 'Gaskets': [], 'Studs': [], 'Hex Nuts': [],'Redraw': [], 'Shop Hours': []}
#tubesheet_final = [tubesheet_qty, tubesheet_unit_cost, tubesheet_item_total]
#tubes_final = [tubes_qty, tubes_unit_cost, tubes_item_total]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 545)
        MainWindow.setMinimumSize(QtCore.QSize(400, 480))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.number_baffles_label = QtWidgets.QLabel(self.centralwidget)
        self.number_baffles_label.setGeometry(QtCore.QRect(15, 270, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.number_baffles_label.setFont(font)
        self.number_baffles_label.setObjectName("number_baffles_label")
        self.baffle_cost_label = QtWidgets.QLabel(self.centralwidget)
        self.baffle_cost_label.setGeometry(QtCore.QRect(150, 270, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.baffle_cost_label.setFont(font)
        self.baffle_cost_label.setObjectName("baffle_cost_label")
        self.tube_options_groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.tube_options_groupbox.setGeometry(QtCore.QRect(10, 140, 351, 181))
        self.tube_options_groupbox.setObjectName("tube_options_groupbox")
        self.tube_OD_label = QtWidgets.QLabel(self.tube_options_groupbox)
        self.tube_OD_label.setGeometry(QtCore.QRect(160, 10, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tube_OD_label.setFont(font)
        self.tube_OD_label.setObjectName("tube_OD_label")
        self.tube_material_label = QtWidgets.QLabel(self.tube_options_groupbox)
        self.tube_material_label.setGeometry(QtCore.QRect(20, 10, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tube_material_label.setFont(font)
        self.tube_material_label.setObjectName("tube_material_label")
        self.tube_OD_combobox = QtWidgets.QComboBox(self.tube_options_groupbox)
        self.tube_OD_combobox.setGeometry(QtCore.QRect(160, 30, 69, 22))
        self.tube_OD_combobox.setObjectName("tube_OD_combobox")
        self.tube_OD_combobox.addItem("")
        self.tube_OD_combobox.addItem("")
        self.tube_OD_combobox.addItem("")
        self.tube_material_combobox = QtWidgets.QComboBox(self.tube_options_groupbox)
        self.tube_material_combobox.setGeometry(QtCore.QRect(20, 30, 121, 22))
        self.tube_material_combobox.setEditable(False)
        self.tube_material_combobox.setObjectName("tube_material_combobox")
        self.tube_material_combobox.addItem("")
        self.tube_material_combobox.addItem("")

        self.single_double_label = QtWidgets.QLabel(self.tube_options_groupbox)
        self.single_double_label.setGeometry(QtCore.QRect(10, 60, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.single_double_label.setFont(font)
        self.single_double_label.setObjectName("single_double_label")
        self.overall_length_label = QtWidgets.QLabel(self.tube_options_groupbox)
        self.overall_length_label.setGeometry(QtCore.QRect(240, 10, 105, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.overall_length_label.setFont(font)
        self.overall_length_label.setObjectName("overall_length_label")
        self.overall_length_lineEdit = QtWidgets.QLineEdit(self.tube_options_groupbox)
        self.overall_length_lineEdit.setGeometry(QtCore.QRect(242, 30, 101, 20))
        self.overall_length_lineEdit.setObjectName("overall_length_lineEdit")
        self.single_double_combobox = QtWidgets.QComboBox(self.tube_options_groupbox)
        self.single_double_combobox.setGeometry(QtCore.QRect(20, 80, 69, 22))
        self.single_double_combobox.setObjectName("single_double_combobox")
        self.single_double_combobox.addItem("")
        self.single_double_combobox.addItem("")
        self.tube_amount_label = QtWidgets.QLabel(self.tube_options_groupbox)
        self.tube_amount_label.setGeometry(QtCore.QRect(150, 60, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tube_amount_label.setFont(font)
        self.tube_amount_label.setObjectName("tube_amount_label")
        self.tubes_amount_lineEdit = QtWidgets.QLineEdit(self.tube_options_groupbox)
        self.tubes_amount_lineEdit.setGeometry(QtCore.QRect(140, 80, 81, 20))
        self.tubes_amount_lineEdit.setObjectName("tubes_amount_lineEdit")
        self.bend_amount_label = QtWidgets.QLabel(self.tube_options_groupbox)
        self.bend_amount_label.setGeometry(QtCore.QRect(260, 60, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bend_amount_label.setFont(font)
        self.bend_amount_label.setObjectName("bend_amount_label")
        self.bends_amount_lineEdit = QtWidgets.QLineEdit(self.tube_options_groupbox)
        self.bends_amount_lineEdit.setGeometry(QtCore.QRect(240, 80, 101, 20))
        self.bends_amount_lineEdit.setObjectName("bends_amount_lineEdit")

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 361, 121))
        self.groupBox.setObjectName("groupBox")
        self.tubesheet_material_label = QtWidgets.QLabel(self.groupBox)
        self.tubesheet_material_label.setGeometry(QtCore.QRect(20, 20, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tubesheet_material_label.setFont(font)
        self.tubesheet_material_label.setObjectName("tubesheet_material_label")
        self.tubesheet_combobox = QtWidgets.QComboBox(self.groupBox)
        self.tubesheet_combobox.setGeometry(QtCore.QRect(20, 40, 121, 22))
        self.tubesheet_combobox.setObjectName("tubesheet_combobox")
        self.tubesheet_combobox.addItem("")
        self.tubesheet_combobox.addItem("")
        self.tubesheet_combobox.addItem("")
        self.tubesheet_combobox.addItem("")
        self.tubesheet_combobox.addItem("")
        self.tubesheet_diameter_label = QtWidgets.QLabel(self.groupBox)
        self.tubesheet_diameter_label.setGeometry(QtCore.QRect(20, 70, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tubesheet_diameter_label.setFont(font)
        self.tubesheet_diameter_label.setObjectName("tubesheet_diameter_label")
        self.tubesheet_diameter_combobox = QtWidgets.QComboBox(self.groupBox)
        self.tubesheet_diameter_combobox.setGeometry(QtCore.QRect(30, 90, 91, 22))
        self.tubesheet_diameter_combobox.setObjectName("tubesheet_diameter_combobox")
        self.tubesheet_diameter_combobox.addItem("")
        self.tubesheet_diameter_combobox.addItem("")
        self.tubesheet_diameter_combobox.addItem("")
        self.tubesheet_diameter_combobox.addItem("")
        self.tubesheet_diameter_combobox.addItem("")
        self.tubesheet_diameter_combobox.addItem("")
        self.tubesheet_diameter_combobox.addItem("")
        self.tubesheet_diameter_combobox.addItem("")
        self.tubesheet_diameter_combobox.addItem("")
        self.tubesheet_diameter_combobox.addItem("")
        self.tubesheet_diameter_combobox.addItem("")

        # new tubesheet options

        self.bolt_circle_label = QtWidgets.QLabel(self.groupBox)
        self.bolt_circle_label.setGeometry(QtCore.QRect(170, 20, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bolt_circle_label.setFont(font)
        self.bolt_circle_label.setObjectName("bolt_circle_label")
        self.bolt_holes_label = QtWidgets.QLabel(self.groupBox)
        self.bolt_holes_label.setGeometry(QtCore.QRect(150, 70, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bolt_holes_label.setFont(font)
        self.bolt_holes_label.setObjectName("bolt_holes_label")
        self.bolt_circle_combobox = QtWidgets.QComboBox(self.groupBox)
        self.bolt_circle_combobox.setGeometry(QtCore.QRect(160, 40, 91, 22))
        self.bolt_circle_combobox.setObjectName("bolt_circle_combobox")
        self.bolt_circle_combobox.addItem("")
        self.bolt_circle_combobox.addItem("")
        self.bolt_circle_combobox.addItem("")
        self.bolt_circle_combobox.addItem("")
        self.bolt_circle_combobox.addItem("")
        self.bolt_circle_combobox.addItem("")
        self.bolt_circle_combobox.addItem("")
        self.bolt_circle_combobox.addItem("")
        self.bolt_circle_combobox.addItem("")
        self.bolt_circle_combobox.addItem("")
        self.bolt_circle_combobox.addItem("")
        self.bolt_hole_number_combobox = QtWidgets.QComboBox(self.groupBox)
        self.bolt_hole_number_combobox.setGeometry(QtCore.QRect(170, 90, 69, 22))
        self.bolt_hole_number_combobox.setObjectName("bolt_hole_number_combobox")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.bolt_hole_number_combobox.addItem("")
        self.tubehole_combobox = QtWidgets.QComboBox(self.groupBox)
        self.tubehole_combobox.setGeometry(QtCore.QRect(280, 90, 69, 22))
        self.tubehole_combobox.setObjectName("tubehole_combobox")
        self.tubehole_combobox.addItem("")
        self.tubehole_combobox.addItem("")
        self.tubehole_combobox.addItem("")
        self.tubehole_combobox.addItem("")
        self.tubehole_combobox.addItem("")
        self.tubehole_combobox.addItem("")
        self.tubehole_combobox.addItem("")
        self.tubehole_combobox.addItem("")
        self.tubehole_combobox.addItem("")
        self.tubehole_combobox.addItem("")
        self.tubehole_combobox.addItem("")
        self.tubehole_combobox.addItem("")
        self.tubeholes_label = QtWidgets.QLabel(self.groupBox)
        self.tubeholes_label.setGeometry(QtCore.QRect(280, 70, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tubeholes_label.setFont(font)
        self.tubeholes_label.setObjectName("tubeholes_label")

        # baffle_cost lineEdit options/config
        self.baffle_cost_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.baffle_cost_lineEdit.setGeometry(QtCore.QRect(150, 290, 113, 20))
        self.baffle_cost_lineEdit.setObjectName("baffle_cost_lineEdit")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 500, 131, 20))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 290, 75, 23))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 330, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setSource(QtCore.QUrl("./text_browser1.txt"))
        self.baffle_number_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.baffle_number_combobox.setGeometry(QtCore.QRect(20, 290, 81, 22))
        self.baffle_number_combobox.setObjectName("baffle_number_combobox")
        self.baffle_number_combobox.addItem("")
        self.baffle_number_combobox.addItem("")
        self.baffle_number_combobox.addItem("")
        self.baffle_number_combobox.addItem("")
        self.baffle_number_combobox.addItem("")
        self.baffle_number_combobox.addItem("")
        self.baffle_number_combobox.addItem("")
        self.baffle_number_combobox.addItem("")
        self.baffle_number_combobox.addItem("")
        self.baffle_number_combobox.addItem("")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Save/Load Menu
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad_Previous_Config = QtWidgets.QAction(MainWindow)
        self.actionLoad_Previous_Config.setObjectName("actionLoad_Previous_Config")
        self.menuSettings.addAction(self.actionSave)
        self.menuSettings.addAction(self.actionLoad_Previous_Config)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.number_baffles_label.setBuddy(self.baffle_number_combobox)
        self.baffle_cost_label.setBuddy(self.baffle_cost_lineEdit)
        self.tube_OD_label.setBuddy(self.tube_OD_combobox)
        self.tube_material_label.setBuddy(self.tube_material_combobox)
        self.tubesheet_material_label.setBuddy(self.tubesheet_combobox)
        self.tubesheet_diameter_label.setBuddy(self.tubesheet_diameter_combobox)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tubesheet_combobox, self.tubesheet_diameter_combobox)
        MainWindow.setTabOrder(self.tubesheet_diameter_combobox, self.tube_material_combobox)
        MainWindow.setTabOrder(self.tube_material_combobox, self.tube_OD_combobox)
        MainWindow.setTabOrder(self.tube_OD_combobox, self.baffle_number_combobox)
        MainWindow.setTabOrder(self.baffle_number_combobox, self.baffle_cost_lineEdit)
        MainWindow.setTabOrder(self.baffle_cost_lineEdit, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.textBrowser)
        MainWindow.setTabOrder(self.textBrowser, self.tubesheet_combobox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Replacement Bundle Pricing"))
        self.number_baffles_label.setText(_translate("MainWindow", "# of Baffles"))
        self.baffle_cost_label.setText(_translate("MainWindow", "Cost Per Baffle"))
        self.tube_options_groupbox.setTitle(_translate("MainWindow", "Tube Options"))
        self.tube_OD_label.setText(_translate("MainWindow", "Tube OD"))
        self.tube_material_label.setText(_translate("MainWindow", "Tube Material"))
        self.tube_OD_combobox.setItemText(0, _translate("MainWindow", "1/2 \""))
        self.tube_OD_combobox.setItemText(1, _translate("MainWindow", "3/4 \""))
        self.tube_OD_combobox.setItemText(2, _translate("MainWindow", "1 - 1/4\""))
        self.tube_material_combobox.setItemText(0, _translate("MainWindow", "Copper"))
        self.tube_material_combobox.setItemText(1, _translate("MainWindow", "Copper-Nickel"))

        self.single_double_label.setText(_translate("MainWindow", "Single or Double Wall"))
        self.single_double_combobox.setItemText(0, _translate("MainWindow", "Single"))
        self.single_double_combobox.setItemText(1, _translate("MainWindow", "Double"))
        self.overall_length_label.setText(_translate("MainWindow", "Overall Length(ft.)"))
        self.tube_amount_label.setText(_translate("MainWindow", "# of Tubes"))
        self.bend_amount_label.setText(_translate("MainWindow", "# of Bends"))

        self.groupBox.setTitle(_translate("MainWindow", "TubeSheet Options"))
        self.tubesheet_material_label.setText(_translate("MainWindow", "TubeSheet Material"))
        self.tubesheet_combobox.setItemText(0, _translate("MainWindow", "Copper"))
        self.tubesheet_combobox.setItemText(1, _translate("MainWindow", "Nickel Plated"))
        self.tubesheet_combobox.setItemText(2, _translate("MainWindow", "Copper-Nickel"))
        self.tubesheet_combobox.setItemText(3, _translate("MainWindow", "Naval Brass"))
        self.tubesheet_combobox.setItemText(4, _translate("MainWindow", "Carbon Steel"))
        self.tubesheet_diameter_label.setText(_translate("MainWindow", "TubeSheet Diameter"))
        self.tubesheet_diameter_combobox.setItemText(0, _translate("MainWindow", "5\""))
        self.tubesheet_diameter_combobox.setItemText(1, _translate("MainWindow", "6\""))
        self.tubesheet_diameter_combobox.setItemText(2, _translate("MainWindow", "8\""))
        self.tubesheet_diameter_combobox.setItemText(3, _translate("MainWindow", "10\""))
        self.tubesheet_diameter_combobox.setItemText(4, _translate("MainWindow", "12\""))
        self.tubesheet_diameter_combobox.setItemText(5, _translate("MainWindow", "14\""))
        self.tubesheet_diameter_combobox.setItemText(6, _translate("MainWindow", "16\""))
        self.tubesheet_diameter_combobox.setItemText(7, _translate("MainWindow", "18\""))
        self.tubesheet_diameter_combobox.setItemText(8, _translate("MainWindow", "20\""))
        self.tubesheet_diameter_combobox.setItemText(9, _translate("MainWindow", "22\""))
        self.tubesheet_diameter_combobox.setItemText(10, _translate("MainWindow", "24\""))

        # new tubesheet options

        self.bolt_circle_label.setText(_translate("MainWindow", "Bolt Circle"))
        self.bolt_circle_combobox.setItemText(0, _translate("MainWindow", "13\""))
        self.bolt_holes_label.setText(_translate("MainWindow", "# Bolt Holes"))
        self.bolt_hole_number_combobox.setItemText(0, _translate("MainWindow", "5"))
        self.bolt_hole_number_combobox.setItemText(1, _translate("MainWindow", "6"))
        self.bolt_hole_number_combobox.setItemText(2, _translate("MainWindow", "7"))
        self.bolt_hole_number_combobox.setItemText(3, _translate("MainWindow", "8"))
        self.bolt_hole_number_combobox.setItemText(4, _translate("MainWindow", "9"))
        self.bolt_hole_number_combobox.setItemText(5, _translate("MainWindow", "10"))
        self.bolt_hole_number_combobox.setItemText(6, _translate("MainWindow", "11"))
        self.bolt_hole_number_combobox.setItemText(7, _translate("MainWindow", "12"))
        self.bolt_hole_number_combobox.setItemText(8, _translate("MainWindow", "13"))
        self.bolt_hole_number_combobox.setItemText(9, _translate("MainWindow", "14"))
        self.bolt_hole_number_combobox.setItemText(10, _translate("MainWindow", "15"))
        self.bolt_hole_number_combobox.setItemText(11, _translate("MainWindow", "16"))
        self.bolt_hole_number_combobox.setItemText(12, _translate("MainWindow", "17"))
        self.bolt_hole_number_combobox.setItemText(13, _translate("MainWindow", "18"))
        self.bolt_hole_number_combobox.setItemText(14, _translate("MainWindow", "19"))
        self.bolt_hole_number_combobox.setItemText(15, _translate("MainWindow", "20"))
        self.bolt_hole_number_combobox.setItemText(16, _translate("MainWindow", "21"))
        self.bolt_hole_number_combobox.setItemText(17, _translate("MainWindow", "22"))
        self.bolt_hole_number_combobox.setItemText(18, _translate("MainWindow", "23"))
        self.bolt_hole_number_combobox.setItemText(19, _translate("MainWindow", "24"))
        self.bolt_hole_number_combobox.setItemText(20, _translate("MainWindow", "25"))
        self.bolt_hole_number_combobox.setItemText(21, _translate("MainWindow", "26"))
        self.bolt_hole_number_combobox.setItemText(22, _translate("MainWindow", "27"))
        self.bolt_hole_number_combobox.setItemText(23, _translate("MainWindow", "28"))
        self.bolt_hole_number_combobox.setItemText(24, _translate("MainWindow", "29"))
        self.bolt_hole_number_combobox.setItemText(25, _translate("MainWindow", "30"))
        self.bolt_hole_number_combobox.setItemText(26, _translate("MainWindow", "31"))
        self.bolt_hole_number_combobox.setItemText(27, _translate("MainWindow", "32"))
        self.tubeholes_label.setText(_translate("MainWindow", "# Tubeholes"))
        self.tubehole_combobox.setItemText(0, _translate("MainWindow", "5"))

        self.pushButton.setText(_translate("MainWindow", "Complete"))
        self.baffle_number_combobox.setItemText(0, _translate("MainWindow", "1"))
        self.baffle_number_combobox.setItemText(1, _translate("MainWindow", "2"))
        self.baffle_number_combobox.setItemText(2, _translate("MainWindow", "3"))
        self.baffle_number_combobox.setItemText(3, _translate("MainWindow", "4"))
        self.baffle_number_combobox.setItemText(4, _translate("MainWindow", "5"))
        self.baffle_number_combobox.setItemText(5, _translate("MainWindow", "6"))
        self.baffle_number_combobox.setItemText(6, _translate("MainWindow", "7"))
        self.baffle_number_combobox.setItemText(7, _translate("MainWindow", "8"))
        self.baffle_number_combobox.setItemText(8, _translate("MainWindow", "9"))
        self.baffle_number_combobox.setItemText(9, _translate("MainWindow", "10"))
        self.menuSettings.setTitle(_translate("MainWindow", "Save/Load"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionLoad_Previous_Config.setText(_translate("MainWindow", "Load Previous Config"))

        ####################################################################################################

        # connecting comboboxes to their functions
        self.baffle_number_combobox.activated[str].connect(self.get_baffle_number)
        self.tubesheet_combobox.activated[str].connect(self.get_tubesheet_material)
        self.tubesheet_diameter_combobox.activated[str].connect(self.get_tubesheet_diameter)
        self.tube_material_combobox.activated[str].connect(self.get_tube_material)
        self.tube_OD_combobox.activated[str].connect(self.get_tube_OD)
        self.bolt_circle_combobox.activated[str].connect(self.get_bolt_circle)
        self.bolt_hole_number_combobox.activated[str].connect(self.get_bolt_hole_number)
        self.tubehole_combobox.activated[str].connect(self.get_tubehole_number)
        self.single_double_combobox.activated[str].connect(self.get_single_double)

        # connecting PushButtons to their functions
        self.pushButton.clicked.connect(self.on_click)

        # connecting lineEdits to their functions
        self.overall_length_lineEdit.editingFinished.connect(self.get_overall_length)
        self.tubes_amount_lineEdit.editingFinished.connect(self.get_tubes_amount)
        self.bends_amount_lineEdit.editingFinished.connect(self.get_bends_amount)
        self.baffle_cost_lineEdit.editingFinished.connect(self.get_baffle_cost)

        # Sets input masks and validators with regular expressions(regex)

        self.overall_length_lineEdit.setInputMask('')
        regexp = QtCore.QRegExp('^([1-9][0-9]{0,2}|1000)$')
        validator = QtGui.QRegExpValidator(regexp)
        self.overall_length_lineEdit.setValidator(validator)
        self.overall_length_lineEdit.setCursorPosition(0)

        self.tubes_amount_lineEdit.setInputMask('')
        regexp = QtCore.QRegExp('^([1-9][0-9]{0,2}|1000)$')
        validator = QtGui.QRegExpValidator(regexp)
        self.tubes_amount_lineEdit.setValidator(validator)
        self.tubes_amount_lineEdit.setCursorPosition(0)

        self.bends_amount_lineEdit.setInputMask('')
        regexp = QtCore.QRegExp('^([1-9][0-9]{0,2}|1000)$')
        validator = QtGui.QRegExpValidator(regexp)
        self.bends_amount_lineEdit.setValidator(validator)
        self.bends_amount_lineEdit.setCursorPosition(0)

        self.baffle_cost_lineEdit.setInputMask('')
        regexp = QtCore.QRegExp('^\$?[0-9]+\.?[0-9]?[0-9]?$')
        validator = QtGui.QRegExpValidator(regexp)
        self.baffle_cost_lineEdit.setValidator(validator)
        self.baffle_cost_lineEdit.setCursorPosition(0)

    def get_tubesheet_material(self):
        final_list[0] = self.tubesheet_combobox.currentText()
        write_options()
        self.textBrowser.reload()

    def get_tubesheet_diameter(self):
        final_list[1] = self.tubesheet_diameter_combobox.currentText()
        write_options()
        self.textBrowser.reload()

    def get_bolt_circle(self):
        final_list[2] = self.bolt_circle_combobox.currentText()
        write_options()
        self.textBrowser.reload()

    def get_bolt_hole_number(self):
        final_list[3] = self.bolt_hole_number_combobox.currentText()
        write_options()
        self.textBrowser.reload()

    def get_tubehole_number(self):
        final_list[4] = self.tubehole_combobox.currentText()
        write_options()
        self.textBrowser.reload()

    def get_tube_material(self):
        final_list[5] = self.tube_material_combobox.currentText()
        write_options()
        self.textBrowser.reload()

    def get_tube_OD(self):
        final_list[6] = self.tube_OD_combobox.currentText()
        write_options()
        self.textBrowser.reload()

    def get_overall_length(self):
        final_list[7] = self.overall_length_lineEdit.text()
        write_options()
        self.textBrowser.reload()

    def get_single_double(self):
        final_list[8] = self.single_double_combobox.currentText()
        write_options()
        self.textBrowser.reload()

    def get_tubes_amount(self):
        final_list[9] = self.tubes_amount_lineEdit.text()
        write_options()
        self.textBrowser.reload()

    def get_bends_amount(self):
        final_list[10] = self.bends_amount_lineEdit.text()
        write_options()
        self.textBrowser.reload()

    def get_baffle_number(self):
        final_list[11] = self.baffle_number_combobox.currentText()
        write_options()
        self.textBrowser.reload()

    def get_baffle_cost(self):
        final_list[12] = self.baffle_cost_lineEdit.text()
        write_options()
        self.textBrowser.reload()

    def get_final_list(self):
        final_list[0] = self.tubesheet_combobox.currentText()
        final_list[1] = self.tubesheet_diameter_combobox.currentText()
        final_list[2] = self.bolt_circle_combobox.currentText()
        final_list[3] = self.bolt_hole_number_combobox.currentText()
        final_list[4] = self.tubehole_combobox.currentText()
        final_list[5] = self.tube_material_combobox.currentText()
        final_list[6] = self.tube_OD_combobox.currentText()
        final_list[7] = self.overall_length_lineEdit.text()
        final_list[8] = self.single_double_combobox.currentText()
        final_list[9] = self.tubes_amount_lineEdit.text()
        final_list[10] = self.bends_amount_lineEdit.text()
        final_list[11] = self.baffle_number_combobox.currentText()
        final_list[12] = self.baffle_cost_lineEdit.text()
        self.textBrowser.clear()

    def on_click(self):
        self.get_final_list()
        write_options()
        # appending totals after calculations to the textfile to later print
        #write_final_options()
        self.textBrowser.reload()
        Ui_misc_Dialog.show_dialog(self)


def write_options():
    config = open('./text_browser1.txt', 'w')
    for items2, items1, in zip(final_list, master_tup):
        config.write(
            items1 + ('&nbsp;') + ('&nbsp;') + ('&nbsp;') + ('&nbsp;') + ('&nbsp;') + ('&nbsp;') + ('&nbsp;') + (
                "--- &nbsp; &nbsp; ") + items2 + ('<br>'))
    config.close()


# MailMerge dictionary construction for printing to Word Document and calculations preparing for such

word_document_items = [{
    'item': "Tubesheet",
    'qty': '2',
    'unit_cost': '350',
    'item_total': '700'
}, {
    'item': "Tubes ",
    'qty': '129',
    'unit_cost': '5.77',
    'item_total': '744.33'
}, {
    'item': "Baffles ",
    'qty': '1',
    'unit_cost': '126',
    'item_total': '126'
}]

word_document_misc = [{
    'miscellaneous': 'Misc. Items',
    'misc_qty': '2',
    'misc_cost': '100',
    'misc_totals': '200'
}]

def write_final_options():
    template = "./test-print.docx"
    document = MailMerge(template)
    # word_document_items = word_document_items_test
    # print(word_document_items)
    print(document.get_merge_fields())
    document.merge_rows('item', word_document_items)
    document.merge_rows('miscellaneous', word_document_misc)
    document.write('test-test-test.docx')


def save_options():
    pass


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class AppDiag(QtWidgets.QDialog):
    def __init__(self):
        super(AppDiag, self).__init__()
        self.dialog = Ui_misc_Dialog()
        self.dialog.setupUi(self)


# Popup dialog for miscellaneous inputs and parts numbers
# TODO: Tie into main window with appropriate function calls
class Ui_misc_Dialog(object):
    def setupUi(self, misc_Dialog):
        misc_Dialog.setObjectName("misc_Dialog")
        misc_Dialog.resize(444, 755)
        misc_Dialog.setMinimumSize(QtCore.QSize(426, 487))
        self.parts_number_label = QtWidgets.QLabel(misc_Dialog)
        self.parts_number_label.setGeometry(QtCore.QRect(130, 10, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.parts_number_label.setFont(font)
        self.parts_number_label.setObjectName("parts_number_label")
        self.shop_hours_cost_lineEdit = QtWidgets.QLineEdit(misc_Dialog)
        self.shop_hours_cost_lineEdit.setGeometry(QtCore.QRect(300, 440, 113, 20))
        self.shop_hours_cost_lineEdit.setObjectName("shop_hours_cost_lineEdit")
        self.spinBox = QtWidgets.QSpinBox(misc_Dialog)
        self.spinBox.setGeometry(QtCore.QRect(240, 40, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.tubesheet_unit_cost_lineEdit = QtWidgets.QLineEdit(misc_Dialog)
        self.tubesheet_unit_cost_lineEdit.setGeometry(QtCore.QRect(300, 40, 113, 20))
        self.tubesheet_unit_cost_lineEdit.setObjectName("tubesheet_unit_cost_lineEdit")
        self.materials_cost_label = QtWidgets.QLabel(misc_Dialog)
        self.materials_cost_label.setGeometry(QtCore.QRect(310, 340, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.materials_cost_label.setFont(font)
        self.materials_cost_label.setObjectName("materials_cost_label")
        self.spinBox_2 = QtWidgets.QSpinBox(misc_Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(240, 80, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_4 = QtWidgets.QSpinBox(misc_Dialog)
        self.spinBox_4.setGeometry(QtCore.QRect(240, 160, 42, 22))
        self.spinBox_4.setObjectName("spinBox_4")
        self.part_number_lineEdit_6 = QtWidgets.QLineEdit(misc_Dialog)
        self.part_number_lineEdit_6.setGeometry(QtCore.QRect(120, 240, 113, 20))
        self.part_number_lineEdit_6.setObjectName("part_number_lineEdit_6")
        self.hex_nuts_unit_cost_lineEdit = QtWidgets.QLineEdit(misc_Dialog)
        self.hex_nuts_unit_cost_lineEdit.setGeometry(QtCore.QRect(300, 280, 113, 20))
        self.hex_nuts_unit_cost_lineEdit.setObjectName("hex_nuts_unit_cost_lineEdit")
        self.calculated_materials_label = QtWidgets.QLabel(misc_Dialog)
        self.calculated_materials_label.setGeometry(QtCore.QRect(310, 360, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calculated_materials_label.setFont(font)
        self.calculated_materials_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calculated_materials_label.setObjectName("calculated_materials_label")
        self.studs_label = QtWidgets.QLabel(misc_Dialog)
        self.studs_label.setGeometry(QtCore.QRect(20, 240, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.studs_label.setFont(font)
        self.studs_label.setObjectName("studs_label")
        self.redraw_cost_lineEdit = QtWidgets.QLineEdit(misc_Dialog)
        self.redraw_cost_lineEdit.setGeometry(QtCore.QRect(300, 400, 113, 20))
        self.redraw_cost_lineEdit.setObjectName("redraw_cost_lineEdit")
        self.spinBox_5 = QtWidgets.QSpinBox(misc_Dialog)
        self.spinBox_5.setGeometry(QtCore.QRect(240, 200, 42, 22))
        self.spinBox_5.setObjectName("spinBox_5")
        self.gaskets2_label = QtWidgets.QLabel(misc_Dialog)
        self.gaskets2_label.setGeometry(QtCore.QRect(20, 200, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gaskets2_label.setFont(font)
        self.gaskets2_label.setObjectName("gaskets2_label")
        self.markup_SpinBox = QtWidgets.QDoubleSpinBox(misc_Dialog)
        self.markup_SpinBox.setGeometry(QtCore.QRect(240, 550, 61, 22))
        self.markup_SpinBox.setSingleStep(0.25)
        self.markup_SpinBox.setObjectName("markup_SpinBox")
        self.tubes_label = QtWidgets.QLabel(misc_Dialog)
        self.tubes_label.setGeometry(QtCore.QRect(20, 80, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tubes_label.setFont(font)
        self.tubes_label.setObjectName("tubes_label")
        self.shop_bundle_label = QtWidgets.QLabel(misc_Dialog)
        self.shop_bundle_label.setGeometry(QtCore.QRect(20, 440, 91, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.shop_bundle_label.setFont(font)
        self.shop_bundle_label.setObjectName("shop_bundle_label")
        self.redraw_label = QtWidgets.QLabel(misc_Dialog)
        self.redraw_label.setGeometry(QtCore.QRect(20, 400, 47, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.redraw_label.setFont(font)
        self.redraw_label.setObjectName("redraw_label")
        self.part_number_lineEdit = QtWidgets.QLineEdit(misc_Dialog)
        self.part_number_lineEdit.setGeometry(QtCore.QRect(120, 40, 113, 20))
        self.part_number_lineEdit.setObjectName("part_number_lineEdit")
        self.tubes_unit_cost_lineEdit = QtWidgets.QLineEdit(misc_Dialog)
        self.tubes_unit_cost_lineEdit.setGeometry(QtCore.QRect(300, 80, 113, 20))
        self.tubes_unit_cost_lineEdit.setObjectName("tubes_unit_cost_lineEdit")
        self.part_number_lineEdit_4 = QtWidgets.QLineEdit(misc_Dialog)
        self.part_number_lineEdit_4.setGeometry(QtCore.QRect(120, 160, 113, 20))
        self.part_number_lineEdit_4.setObjectName("part_number_lineEdit_4")
        self.gaskets_unit_cost_lineEdit_2 = QtWidgets.QLineEdit(misc_Dialog)
        self.gaskets_unit_cost_lineEdit_2.setGeometry(QtCore.QRect(300, 200, 113, 20))
        self.gaskets_unit_cost_lineEdit_2.setObjectName("gaskets_unit_cost_lineEdit_2")
        self.spinBox_3 = QtWidgets.QSpinBox(misc_Dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(240, 120, 42, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_6 = QtWidgets.QSpinBox(misc_Dialog)
        self.spinBox_6.setGeometry(QtCore.QRect(240, 240, 42, 22))
        self.spinBox_6.setObjectName("spinBox_6")
        self.markup_label = QtWidgets.QLabel(misc_Dialog)
        self.markup_label.setGeometry(QtCore.QRect(240, 530, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.markup_label.setFont(font)
        self.markup_label.setObjectName("markup_label")
        self.hex_label = QtWidgets.QLabel(misc_Dialog)
        self.hex_label.setGeometry(QtCore.QRect(20, 280, 51, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hex_label.setFont(font)
        self.hex_label.setObjectName("hex_label")
        self.tubesheet_label = QtWidgets.QLabel(misc_Dialog)
        self.tubesheet_label.setGeometry(QtCore.QRect(6, 40, 61, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tubesheet_label.setFont(font)
        self.tubesheet_label.setObjectName("tubesheet_label")
        self.studs_unit_cost_lineEdit = QtWidgets.QLineEdit(misc_Dialog)
        self.studs_unit_cost_lineEdit.setGeometry(QtCore.QRect(300, 240, 113, 20))
        self.studs_unit_cost_lineEdit.setObjectName("studs_unit_cost_lineEdit")
        self.part_number_lineEdit_7 = QtWidgets.QLineEdit(misc_Dialog)
        self.part_number_lineEdit_7.setGeometry(QtCore.QRect(120, 280, 113, 20))
        self.part_number_lineEdit_7.setObjectName("part_number_lineEdit_7")
        self.baffles_label = QtWidgets.QLabel(misc_Dialog)
        self.baffles_label.setGeometry(QtCore.QRect(20, 120, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.baffles_label.setFont(font)
        self.baffles_label.setObjectName("baffles_label")
        self.spinBox_9 = QtWidgets.QSpinBox(misc_Dialog)
        self.spinBox_9.setGeometry(QtCore.QRect(240, 400, 42, 22))
        self.spinBox_9.setObjectName("spinBox_9")
        self.spinBox_7 = QtWidgets.QSpinBox(misc_Dialog)
        self.spinBox_7.setGeometry(QtCore.QRect(240, 280, 42, 22))
        self.spinBox_7.setObjectName("spinBox_7")
        self.part_number_lineEdit_2 = QtWidgets.QLineEdit(misc_Dialog)
        self.part_number_lineEdit_2.setGeometry(QtCore.QRect(120, 80, 113, 20))
        self.part_number_lineEdit_2.setObjectName("part_number_lineEdit_2")
        self.baffles_unit_cost_lineEdit = QtWidgets.QLineEdit(misc_Dialog)
        self.baffles_unit_cost_lineEdit.setGeometry(QtCore.QRect(300, 120, 113, 20))
        self.baffles_unit_cost_lineEdit.setObjectName("baffles_unit_cost_lineEdit")
        self.per_item_label = QtWidgets.QLabel(misc_Dialog)
        self.per_item_label.setGeometry(QtCore.QRect(310, 10, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.per_item_label.setFont(font)
        self.per_item_label.setObjectName("per_item_label")
        self.spinBox_10 = QtWidgets.QSpinBox(misc_Dialog)
        self.spinBox_10.setGeometry(QtCore.QRect(240, 440, 42, 22))
        self.spinBox_10.setObjectName("spinBox_10")
        self.gaskets_label = QtWidgets.QLabel(misc_Dialog)
        self.gaskets_label.setGeometry(QtCore.QRect(20, 160, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gaskets_label.setFont(font)
        self.gaskets_label.setObjectName("gaskets_label")
        self.part_number_lineEdit_3 = QtWidgets.QLineEdit(misc_Dialog)
        self.part_number_lineEdit_3.setGeometry(QtCore.QRect(120, 120, 113, 20))
        self.part_number_lineEdit_3.setObjectName("part_number_lineEdit_3")
        self.part_number_lineEdit_5 = QtWidgets.QLineEdit(misc_Dialog)
        self.part_number_lineEdit_5.setGeometry(QtCore.QRect(120, 200, 113, 20))
        self.part_number_lineEdit_5.setObjectName("part_number_lineEdit_5")
        self.gaskets_unit_cost_lineEdit_1 = QtWidgets.QLineEdit(misc_Dialog)
        self.gaskets_unit_cost_lineEdit_1.setGeometry(QtCore.QRect(300, 160, 113, 20))
        self.gaskets_unit_cost_lineEdit_1.setObjectName("gaskets_unit_cost_lineEdit_1")
        self.calculate_pushButton = QtWidgets.QPushButton(misc_Dialog)
        self.calculate_pushButton.setGeometry(QtCore.QRect(340, 670, 91, 23))
        self.calculate_pushButton.setObjectName("calculate_pushButton")
        self.total_cost_label = QtWidgets.QLabel(misc_Dialog)
        self.total_cost_label.setGeometry(QtCore.QRect(310, 480, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.total_cost_label.setFont(font)
        self.total_cost_label.setObjectName("total_cost_label")
        self.calculated_total_label = QtWidgets.QLabel(misc_Dialog)
        self.calculated_total_label.setGeometry(QtCore.QRect(310, 500, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calculated_total_label.setFont(font)
        self.calculated_total_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calculated_total_label.setObjectName("calculated_total_label")
        self.rep_cost_label = QtWidgets.QLabel(misc_Dialog)
        self.rep_cost_label.setGeometry(QtCore.QRect(310, 580, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rep_cost_label.setFont(font)
        self.rep_cost_label.setObjectName("rep_cost_label")
        self.calculated_rep_cost_label = QtWidgets.QLabel(misc_Dialog)
        self.calculated_rep_cost_label.setGeometry(QtCore.QRect(310, 600, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calculated_rep_cost_label.setFont(font)
        self.calculated_rep_cost_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calculated_rep_cost_label.setObjectName("calculated_rep_cost_label")
        self.list_price_label = QtWidgets.QLabel(misc_Dialog)
        self.list_price_label.setGeometry(QtCore.QRect(310, 620, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.list_price_label.setFont(font)
        self.list_price_label.setObjectName("list_price_label")
        self.calculated_list_price_label = QtWidgets.QLabel(misc_Dialog)
        self.calculated_list_price_label.setGeometry(QtCore.QRect(310, 640, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calculated_list_price_label.setFont(font)
        self.calculated_list_price_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calculated_list_price_label.setObjectName("calculated_list_price_label")
        self.markup_SpinBox_2 = QtWidgets.QDoubleSpinBox(misc_Dialog)
        self.markup_SpinBox_2.setGeometry(QtCore.QRect(240, 630, 61, 22))
        self.markup_SpinBox_2.setSingleStep(0.05)
        self.markup_SpinBox_2.setObjectName("markup_SpinBox_2")
        self.markup_label_2 = QtWidgets.QLabel(misc_Dialog)
        self.markup_label_2.setGeometry(QtCore.QRect(240, 610, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.markup_label_2.setFont(font)
        self.markup_label_2.setObjectName("markup_label_2")
        self.misc_label = QtWidgets.QLabel(misc_Dialog)
        self.misc_label.setGeometry(QtCore.QRect(150, 310, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.misc_label.setFont(font)
        self.misc_label.setObjectName("misc_label")
        self.spinBox_8 = QtWidgets.QSpinBox(misc_Dialog)
        self.spinBox_8.setGeometry(QtCore.QRect(240, 310, 42, 22))
        self.spinBox_8.setObjectName("spinBox_8")
        self.misc_unit_cost_lineEdit = QtWidgets.QLineEdit(misc_Dialog)
        self.misc_unit_cost_lineEdit.setGeometry(QtCore.QRect(300, 310, 113, 20))
        self.misc_unit_cost_lineEdit.setObjectName("misc_unit_cost_lineEdit")
        misc_Dialog.setCentralWidget(misc_Dialog)
        self.menubar = QtWidgets.QMenuBar(misc_Dialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 444, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        misc_Dialog.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(misc_Dialog)
        self.statusbar.setObjectName("statusbar")
        misc_Dialog.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(misc_Dialog)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.actionExport_to_Excel = QtWidgets.QAction(misc_Dialog)
        self.actionExport_to_Excel.setObjectName("actionExport_to_Excel")
        self.menuFile.addAction(self.actionExport_to_Excel)

        self.retranslateUi(misc_Dialog)
        QtCore.QMetaObject.connectSlotsByName(misc_Dialog)
        misc_Dialog.setTabOrder(self.part_number_lineEdit, self.spinBox)
        misc_Dialog.setTabOrder(self.spinBox, self.tubesheet_unit_cost_lineEdit)
        misc_Dialog.setTabOrder(self.tubesheet_unit_cost_lineEdit, self.part_number_lineEdit_2)
        misc_Dialog.setTabOrder(self.part_number_lineEdit_2, self.spinBox_2)
        misc_Dialog.setTabOrder(self.spinBox_2, self.tubes_unit_cost_lineEdit)
        misc_Dialog.setTabOrder(self.tubes_unit_cost_lineEdit, self.part_number_lineEdit_3)
        misc_Dialog.setTabOrder(self.part_number_lineEdit_3, self.spinBox_3)
        misc_Dialog.setTabOrder(self.spinBox_3, self.baffles_unit_cost_lineEdit)
        misc_Dialog.setTabOrder(self.baffles_unit_cost_lineEdit, self.part_number_lineEdit_4)
        misc_Dialog.setTabOrder(self.part_number_lineEdit_4, self.spinBox_4)
        misc_Dialog.setTabOrder(self.spinBox_4, self.gaskets_unit_cost_lineEdit_1)
        misc_Dialog.setTabOrder(self.gaskets_unit_cost_lineEdit_1, self.part_number_lineEdit_5)
        misc_Dialog.setTabOrder(self.part_number_lineEdit_5, self.spinBox_5)
        misc_Dialog.setTabOrder(self.spinBox_5, self.gaskets_unit_cost_lineEdit_2)
        misc_Dialog.setTabOrder(self.gaskets_unit_cost_lineEdit_2, self.part_number_lineEdit_6)
        misc_Dialog.setTabOrder(self.part_number_lineEdit_6, self.spinBox_6)
        misc_Dialog.setTabOrder(self.spinBox_6, self.studs_unit_cost_lineEdit)
        misc_Dialog.setTabOrder(self.studs_unit_cost_lineEdit, self.part_number_lineEdit_7)
        misc_Dialog.setTabOrder(self.part_number_lineEdit_7, self.spinBox_7)
        misc_Dialog.setTabOrder(self.spinBox_7, self.hex_nuts_unit_cost_lineEdit)
        misc_Dialog.setTabOrder(self.hex_nuts_unit_cost_lineEdit, self.spinBox_8)
        misc_Dialog.setTabOrder(self.spinBox_8, self.misc_unit_cost_lineEdit)
        misc_Dialog.setTabOrder(self.misc_unit_cost_lineEdit, self.spinBox_9)
        misc_Dialog.setTabOrder(self.spinBox_9, self.redraw_cost_lineEdit)
        misc_Dialog.setTabOrder(self.redraw_cost_lineEdit, self.spinBox_10)
        misc_Dialog.setTabOrder(self.spinBox_10, self.shop_hours_cost_lineEdit)
        misc_Dialog.setTabOrder(self.shop_hours_cost_lineEdit, self.markup_SpinBox)
        misc_Dialog.setTabOrder(self.markup_SpinBox, self.markup_SpinBox_2)
        misc_Dialog.setTabOrder(self.markup_SpinBox_2, self.calculate_pushButton)

    def retranslateUi(self, misc_Dialog):
        _translate = QtCore.QCoreApplication.translate
        misc_Dialog.setWindowTitle(_translate("misc_Dialog", "Dialog"))
        self.parts_number_label.setText(_translate("misc_Dialog", "Parts Numbers"))
        self.shop_hours_cost_lineEdit.setText(_translate("misc_Dialog", "0.0"))
        self.tubesheet_unit_cost_lineEdit.setText(_translate("misc_Dialog", "0.0"))
        self.materials_cost_label.setText(_translate("misc_Dialog", "Materials Cost:"))
        self.hex_nuts_unit_cost_lineEdit.setText(_translate("misc_Dialog", "0.0"))
        self.calculated_materials_label.setText(_translate("misc_Dialog", "0.0"))
        self.studs_label.setText(_translate("misc_Dialog", "Studs"))
        self.redraw_cost_lineEdit.setText(_translate("misc_Dialog", "0.0"))
        self.gaskets2_label.setText(_translate("misc_Dialog", "Gaskets"))
        self.tubes_label.setText(_translate("misc_Dialog", "Tubes"))
        self.shop_bundle_label.setText(_translate("misc_Dialog", "Shop Hours"))
        self.redraw_label.setText(_translate("misc_Dialog", "Redraw"))
        self.tubes_unit_cost_lineEdit.setText(_translate("misc_Dialog", "0.0"))
        self.gaskets_unit_cost_lineEdit_2.setText(_translate("misc_Dialog", "0.0"))
        self.markup_label.setText(_translate("misc_Dialog", "Mark Up"))
        self.hex_label.setText(_translate("misc_Dialog", "Hex Nuts"))
        self.tubesheet_label.setText(_translate("misc_Dialog", "Tubesheet"))
        self.studs_unit_cost_lineEdit.setText(_translate("misc_Dialog", "0.0"))
        self.baffles_label.setText(_translate("misc_Dialog", "Baffles"))
        self.baffles_unit_cost_lineEdit.setText(_translate("misc_Dialog", "0.0"))
        self.per_item_label.setText(_translate("misc_Dialog", "Cost Per Item"))
        self.gaskets_label.setText(_translate("misc_Dialog", "Gaskets"))
        self.gaskets_unit_cost_lineEdit_1.setText(_translate("misc_Dialog", "0.0"))
        self.calculate_pushButton.setText(_translate("misc_Dialog", "Calculate"))
        self.total_cost_label.setText(_translate("misc_Dialog", "Total Cost:"))
        self.calculated_total_label.setText(_translate("misc_Dialog", "0.0"))
        self.rep_cost_label.setText(_translate("misc_Dialog", "Rep Cost:"))
        self.calculated_rep_cost_label.setText(_translate("misc_Dialog", "0.0"))
        self.list_price_label.setText(_translate("misc_Dialog", "List Price:"))
        self.calculated_list_price_label.setText(_translate("misc_Dialog", "0.0"))
        self.markup_label_2.setText(_translate("misc_Dialog", "Mark Up"))
        self.misc_label.setText(_translate("misc_Dialog", "Miscellaneous"))
        self.misc_unit_cost_lineEdit.setText(_translate("misc_Dialog", "0.0"))
        self.menuFile.setTitle(_translate("misc_Dialog", "File"))
        self.actionSave.setText(_translate("misc_Dialog", "Save"))
        self.actionSave.setShortcut(_translate("misc_Dialog", "Ctrl+S"))
        self.actionExport_to_Excel.setText(_translate("misc_Dialog", "Export to Excel"))




        ########################################################################
        # copy below before replacing designer generated code for entire class: Ui_misc_Dialog
        ########################################################################


        # connections to functions
        self.tubesheet_unit_cost_lineEdit.editingFinished.connect(self.set_tubesheet_unit_cost)
        self.tubes_unit_cost_lineEdit.editingFinished.connect(self.set_tubes_unit_cost)
        self.baffles_unit_cost_lineEdit.editingFinished.connect(self.set_baffles_unit_cost)
        self.gaskets_unit_cost_lineEdit_1.editingFinished.connect(self.set_gaskets_unit_cost)
        self.gaskets_unit_cost_lineEdit_2.editingFinished.connect(self.set_gaskets2_unit_cost)
        self.studs_unit_cost_lineEdit.editingFinished.connect(self.set_studs_unit_cost)
        self.hex_nuts_unit_cost_lineEdit.editingFinished.connect(self.set_hex_unit_cost)
        self.misc_unit_cost_lineEdit.editingFinished.connect(self.set_misc_unit_cost)
        self.redraw_cost_lineEdit.editingFinished.connect(self.set_redraw_unit_cost)
        self.shop_hours_cost_lineEdit.editingFinished.connect(self.set_shop_hrs_unit_cost)
        self.part_number_lineEdit.editingFinished.connect(self.set_tubesheet_parts)
        self.part_number_lineEdit_2.editingFinished.connect(self.set_tubes_parts)
        self.part_number_lineEdit_3.editingFinished.connect(self.set_baffles_parts)
        self.part_number_lineEdit_4.editingFinished.connect(self.set_gaskets1_parts)
        self.part_number_lineEdit_5.editingFinished.connect(self.set_gaskets2_parts)
        self.part_number_lineEdit_6.editingFinished.connect(self.set_studs_parts)
        self.part_number_lineEdit_7.editingFinished.connect(self.set_hex_parts)

        self.spinBox.editingFinished.connect(self.set_tubesheet_qty)
        self.spinBox_2.editingFinished.connect(self.set_tubes_qty)
        self.spinBox_3.editingFinished.connect(self.set_baffles_qty)
        self.spinBox_4.editingFinished.connect(self.set_gaskets_qty)
        self.spinBox_5.editingFinished.connect(self.set_gaskets2_qty)
        self.spinBox_6.editingFinished.connect(self.set_studs_qty)
        self.spinBox_7.editingFinished.connect(self.set_hex_qty)
        self.spinBox_8.editingFinished.connect(self.set_misc_qty)
        self.spinBox_9.editingFinished.connect(self.set_redraw_qty)
        self.spinBox_10.editingFinished.connect(self.set_shop_hrs_qty)
        self.markup_SpinBox.editingFinished.connect(self.set_markup1)
        self.markup_SpinBox_2.editingFinished.connect(self.set_markup2)

        self.calculate_pushButton.clicked.connect(self.calculate_total_costs)


        self.actionSave.triggered.connect(self.file_save)
        self.actionExport_to_Excel.connect(self.excel_export)

        # lineEdit validators restricting input to integers and 2 decimal places
        self.baffles_unit_cost_lineEdit.setInputMask('')
        self.misc_unit_cost_lineEdit.setInputMask('')
        self.tubesheet_unit_cost_lineEdit.setInputMask('')
        self.tubes_unit_cost_lineEdit.setInputMask('')
        self.gaskets_unit_cost_lineEdit_1.setInputMask('')
        self.gaskets_unit_cost_lineEdit_2.setInputMask('')
        self.studs_unit_cost_lineEdit.setInputMask('')
        self.hex_nuts_unit_cost_lineEdit.setInputMask('')
        self.redraw_cost_lineEdit.setInputMask('')
        self.shop_hours_cost_lineEdit.setInputMask('')

        regexp = QtCore.QRegExp('^|[0-9]*(\.[0-9][0-9]?)?')
        validator = QtGui.QRegExpValidator(regexp)

        self.baffles_unit_cost_lineEdit.setValidator(validator)
        self.misc_unit_cost_lineEdit.setValidator(validator)
        self.tubesheet_unit_cost_lineEdit.setValidator(validator)
        self.tubes_unit_cost_lineEdit.setValidator(validator)
        self.gaskets_unit_cost_lineEdit_1.setValidator(validator)
        self.gaskets_unit_cost_lineEdit_2.setValidator(validator)
        self.studs_unit_cost_lineEdit.setValidator(validator)
        self.hex_nuts_unit_cost_lineEdit.setValidator(validator)
        self.redraw_cost_lineEdit.setValidator(validator)
        self.shop_hours_cost_lineEdit.setValidator(validator)
        self.baffles_unit_cost_lineEdit.setValidator(validator)

        self.baffles_unit_cost_lineEdit.setCursorPosition(0)

    def create_dicts(self, qty, cost, totals):
        docx_dict.clear()
        docx_dict.extend([{'item': i, 'parts_number': p, 'qty': q, 'unit_cost': c, 'total_cost': str(t)} for i, p, q, c, t in
         itertools.zip_longest(item, parts, qty, cost, totals, fillvalue='N/A')])

    def create_merge2(self, rep, list_price, markup, material_cost, redraw_eng_cost, markup_multiplier2):
        merge2.clear()
        date_time = datetime.date.today()
        merge2.update({'rep_cost': str(rep), 'list_price': str(list_price), 'markup': str(markup), 'materials_cost': str(material_cost), 'complete_cost':str(redraw_eng_cost), 'markup2':str(markup_multiplier2), 'date_time':str(date_time)})

    def write_final_options(self, name):
        template = "test-print.docx"
        document = MailMerge(template)
        document.merge_rows('item', docx_dict)
        document.merge(**merge2)
        if name.endswith('.docx'):
            document.write(name)
        else:
            document.write(name + '.docx')
        document.close()

    def file_save(self):
        name = QtWidgets.QFileDialog.getSaveFileName()
        self.write_final_options(str(name[0]))

    def excel_export(self):
        pass

    def set_tubesheet_qty(self):
        item_qtys[0] = self.spinBox.text()

    def set_tubes_qty(self):
        item_qtys[1] = self.spinBox_2.text()

    def set_baffles_qty(self):
        item_qtys[2] = self.spinBox_3.text()

    def set_gaskets_qty(self):
        item_qtys[3] = self.spinBox_4.text()

    def set_gaskets2_qty(self):
        item_qtys[4] = self.spinBox_5.text()

    def set_studs_qty(self):
        item_qtys[5] = self.spinBox_6.text()

    def set_hex_qty(self):
        item_qtys[6] = self.spinBox_7.text()

    def set_misc_qty(self):
        item_qtys[7] = self.spinBox_8.text()

    def set_redraw_qty(self):
        item_qtys[8] = self.spinBox_9.text()

    def set_shop_hrs_qty(self):
        item_qtys[9] = self.spinBox_10.text()

    def set_tubesheet_unit_cost(self):
        unit_costs[0] = self.tubesheet_unit_cost_lineEdit.text()

    def set_tubes_unit_cost(self):
        unit_costs[1] = self.tubes_unit_cost_lineEdit.text()

    def set_baffles_unit_cost(self):
        unit_costs[2] = self.baffles_unit_cost_lineEdit.text()

    def set_gaskets_unit_cost(self):
        unit_costs[3] = self.gaskets_unit_cost_lineEdit_1.text()

    def set_gaskets2_unit_cost(self):
        unit_costs[4] = self.gaskets_unit_cost_lineEdit_2.text()

    def set_studs_unit_cost(self):
        unit_costs[5] = self.studs_unit_cost_lineEdit.text()

    def set_hex_unit_cost(self):
        unit_costs[6] = self.hex_nuts_unit_cost_lineEdit.text()

    def set_misc_unit_cost(self):
        unit_costs[7] = self.misc_unit_cost_lineEdit.text()

    def set_redraw_unit_cost(self):
        unit_costs[8] = self.redraw_cost_lineEdit.text()

    def set_shop_hrs_unit_cost(self):
        unit_costs[9] = self.shop_hours_cost_lineEdit.text()

    def set_markup1(self):
        markup_multiplier = self.markup_SpinBox.text()

    def set_markup2(self):
        markup_multiplier2 = self.markup_SpinBox_2.text()

    def set_tubesheet_parts(self):
        parts_numbers[0] = self.part_number_lineEdit.text()

    def set_tubes_parts(self):
        parts_numbers[1] = self.part_number_lineEdit_2.text()

    def set_baffles_parts(self):
        parts_numbers[2] = self.part_number_lineEdit_3.text()

    def set_gaskets1_parts(self):
        parts_numbers[3] = self.part_number_lineEdit_4.text()

    def set_gaskets2_parts(self):
        parts_numbers[4] = self.part_number_lineEdit_5.text()

    def set_studs_parts(self):
        parts_numbers[5] = self.part_number_lineEdit_6.text()

    def set_hex_parts(self):
        parts_numbers[6] = self.part_number_lineEdit_7.text()

    def costs_qtys(self):
        for x in unit_costs:
            if x == "":
                x = 0
                unit_costs_float.append(float(x))
            else:
                unit_costs_float.append(float(x))
        for y in item_qtys:
            item_qtys_float.append(float(y))
        total_costs = [x * y for x, y in zip(unit_costs_float, item_qtys_float)]
        item_total = total_costs
        materials_cost = sum(total_costs[:-2])
        material_cost = materials_cost
        redraw_eng_cost = sum(total_costs)
        markup_multiplier = self.markup_SpinBox.text()
        markup_multiplier2 = self.markup_SpinBox_2.text()
        rep_cost = (redraw_eng_cost * float(markup_multiplier))
        list_price = rep_cost + (rep_cost * float(markup_multiplier2))
        self.calculated_total_label.setText(str(redraw_eng_cost))
        self.calculated_materials_label.setText(str(materials_cost))
        self.calculated_rep_cost_label.setText(str(rep_cost))
        self.calculated_list_price_label.setText(str(list_price))
        self.create_dicts(item_qtys, unit_costs, total_costs)
        self.create_merge2(rep_cost, list_price, markup_multiplier, material_cost, redraw_eng_cost, markup_multiplier2)
        del total_costs[:]
        del unit_costs_float[:]
        del item_qtys_float[:]

    def calculate_total_costs(self):
        self.costs_qtys()

    def create_dataframe(self):
        df = pd.DataFrame(data, columns=['Estimate Number', 'Estimate Date', 'Tubesheet Material', 'Tube Material', 'Qty', 'Unit Cost', 'Total Cost'])
        print(df)

    def show_dialog(self):
        self.appdiag = AppDiag()
        self.appdiag.exec_()

parts_numbers = ["", "", "", "", "", "", ""]
materials_cost = 0.0
unit_costs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
unit_costs_float = []
item_qtys = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
item_qtys_float = []
markup_multiplier2 = 0.0
markup_multiplier = 0.0

item = ['Tubesheet', 'Tubes', 'Baffles', 'Gaskets', 'Gaskets', 'Studs', 'Hex Nuts', 'Miscellaneous', 'Redraw', 'Shop Hours']
qty = item_qtys
unit_cost = unit_costs
item_total = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
keys = ['item', 'part_number', 'qty', 'unit_cost', 'item_total']
parts = parts_numbers
docx_dict = []
merge2 = {}

if __name__ == "__main__":
    open('./text_browser1.txt', 'w').close()
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())
