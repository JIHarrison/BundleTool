import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QValidator, QRegExpValidator, QActionEvent
from PyQt5.QtCore import pyqtSlot, QVariant, QStringListModel, pyqtBoundSignal


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
        self.number_baffles_label.setText(_translate("MainWindow", "Number of Baffles"))
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
        self.bolt_holes_label.setText(_translate("MainWindow", "Number of Bolt Holes"))
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

        self.label.setText(_translate("MainWindow", "Configuration:"))
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
        regexp = QtCore.QRegExp('^([1-9][0-9]{0,2}|1000)$')
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

    def on_click(self):
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
        final_list[10] = self.overall_length_lineEdit.text()
        final_list[11] = self.baffle_number_combobox.currentText()
        final_list[12] = self.baffle_cost_lineEdit.text()
        self.textBrowser.clear()
        write_options()
        self.textBrowser.reload()

# tuples for later use, modularability(if this isn't a word I made it one, deal with it)
# this will possibly allow for someone to edit the script so they can dynamically add options for every field
master_tup = ('TubeSheet Material', 'TubeSheet Diameter', 'Bolt Circle', 'Number of Bolt Holes', '# Tubeholes', 'Tube Material', 'Tube OD', 'Overall Length', 'Single or Double Wall', '# of Tubes', '# of Bends', '# of Baffles', 'Cost of Baffles')
tubesheet_material_tup = ('Copper', 'Nickel Plated', 'Copper-Nickel', 'Naval Brass', 'Carbon Steel',)
tubesheet_diameter_tup = ('5"', '6"', '8"', '10"', '12"', '14"', '16"', '18"', '20"', '22"', '24"')
tube_material_tup = ('copper', 'Copper-Nickel')
tube_OD_tup = ('1/2"', '3/4"', '1 - 1/4"')
number_of_baffles_tup = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

final_list = ["", "", "", "", "", "", "", "", "", "", "", "", ""]


def write_options():
    config = open('./text_browser1.txt', 'w')
    for items2, items1, in zip(final_list, master_tup):
        config.write(items1 + ('&nbsp;') + ('&nbsp;') + ('&nbsp;') + ('&nbsp;') + ('&nbsp;') + ('&nbsp;') + ('&nbsp;') + ("--- &nbsp; &nbsp; ") + items2 + ('<br>'))
    config.close()

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    open('./text_browser1.txt', 'w').close()
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())