import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 605)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.configurator_listview = QtWidgets.QListView(self.centralwidget)
        self.configurator_listview.setGeometry(QtCore.QRect(370, 20, 256, 231))
        self.configurator_listview.setObjectName("configurator_listview")
        self.number_baffles_label = QtWidgets.QLabel(self.centralwidget)
        self.number_baffles_label.setGeometry(QtCore.QRect(20, 210, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.number_baffles_label.setFont(font)
        self.number_baffles_label.setObjectName("number_baffles_label")
        self.configurator_listview_2 = QtWidgets.QListView(self.centralwidget)
        self.configurator_listview_2.setGeometry(QtCore.QRect(370, 270, 256, 231))
        self.configurator_listview_2.setObjectName("configurator_listview_2")
        self.baffle_cost_label = QtWidgets.QLabel(self.centralwidget)
        self.baffle_cost_label.setGeometry(QtCore.QRect(170, 210, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.baffle_cost_label.setFont(font)
        self.baffle_cost_label.setObjectName("baffle_cost_label")
        self.configurator_listview_3 = QtWidgets.QListView(self.centralwidget)
        self.configurator_listview_3.setGeometry(QtCore.QRect(370, 520, 256, 31))
        self.configurator_listview_3.setObjectName("configurator_listview_3")
        self.tube_options_groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.tube_options_groupbox.setGeometry(QtCore.QRect(10, 140, 351, 61))
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
        self.total_tubing_label = QtWidgets.QLabel(self.tube_options_groupbox)
        self.total_tubing_label.setGeometry(QtCore.QRect(240, 10, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.total_tubing_label.setFont(font)
        self.total_tubing_label.setObjectName("total_tubing_label")
        self.total_tubing_lineEdit = QtWidgets.QLineEdit(self.tube_options_groupbox)
        self.total_tubing_lineEdit.setGeometry(QtCore.QRect(240, 30, 101, 20))
        self.total_tubing_lineEdit.setObjectName("total_tubing_lineEdit")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 181, 121))
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
        self.tubesheet_diameter_lineEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.tubesheet_diameter_lineEdit.setGeometry(QtCore.QRect(20, 90, 121, 21))
        self.tubesheet_diameter_lineEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tubesheet_diameter_lineEdit.setObjectName("tubesheet_diameter_lineEdit")

        # TODO Get text from QlineEdits to save to textfile for TextBrowser to display
        self.baffle_number_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.baffle_number_lineEdit.setGeometry(QtCore.QRect(20, 230, 113, 20))
        self.baffle_number_lineEdit.setInputMask("")
        self.baffle_number_lineEdit.setObjectName("baffle_number_lineEdit")
        baffle_number = self.baffle_number_lineEdit.text()


        self.baffle_cost_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.baffle_cost_lineEdit.setGeometry(QtCore.QRect(170, 230, 113, 20))
        self.baffle_cost_lineEdit.setObjectName("baffle_cost_lineEdit")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 500, 131, 20))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 230, 75, 23))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 330, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
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
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad_Previous_Config = QtWidgets.QAction(MainWindow)
        self.actionLoad_Previous_Config.setObjectName("actionLoad_Previous_Config")
        self.menuSettings.addAction(self.actionSave)
        self.menuSettings.addAction(self.actionLoad_Previous_Config)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tubesheet_combobox, self.tube_material_combobox)
        MainWindow.setTabOrder(self.tube_material_combobox, self.tube_OD_combobox)
        MainWindow.setTabOrder(self.tube_OD_combobox, self.baffle_number_lineEdit)
        MainWindow.setTabOrder(self.baffle_number_lineEdit, self.configurator_listview)
        MainWindow.setTabOrder(self.configurator_listview, self.configurator_listview_2)
        MainWindow.setTabOrder(self.configurator_listview_2, self.configurator_listview_3)

#Setting names and default text of fields

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Replacement Bundle Pricing"))
        self.number_baffles_label.setText(_translate("MainWindow", "Number of Baffles"))
        self.baffle_cost_label.setText(_translate("MainWindow", "Cost of Baffles"))
        self.tube_options_groupbox.setTitle(_translate("MainWindow", "Tube Options"))
        self.tube_OD_label.setText(_translate("MainWindow", "Tube OD"))
        self.tube_material_label.setText(_translate("MainWindow", "Tube Material"))
        self.tube_OD_combobox.setItemText(0, _translate("MainWindow", "1/2 \""))
        self.tube_OD_combobox.setItemText(1, _translate("MainWindow", "3/4 \""))
        self.tube_OD_combobox.setItemText(2, _translate("MainWindow", "1 - 1/4\""))
        self.tube_material_combobox.setItemText(0, _translate("MainWindow", "Copper"))
        self.tube_material_combobox.setItemText(1, _translate("MainWindow", "Copper-Nickel"))
        self.total_tubing_label.setText(_translate("MainWindow", "Total Tubing (ft)"))
        self.total_tubing_lineEdit.setPlaceholderText(_translate("MainWindow", "####"))
        self.groupBox.setTitle(_translate("MainWindow", "TubeSheet Options"))
        self.tubesheet_material_label.setText(_translate("MainWindow", "TubeSheet Material"))
        self.tubesheet_combobox.setItemText(0, _translate("MainWindow", "Copper"))
        self.tubesheet_combobox.setItemText(1, _translate("MainWindow", "Nickel Plated"))
        self.tubesheet_combobox.setItemText(2, _translate("MainWindow", "Copper-Nickel"))
        self.tubesheet_combobox.setItemText(3, _translate("MainWindow", "Naval Brass"))
        self.tubesheet_combobox.setItemText(4, _translate("MainWindow", "Carbon Steel"))
        self.tubesheet_diameter_label.setText(_translate("MainWindow", "TubeSheet Diameter"))
        self.tubesheet_diameter_lineEdit.setPlaceholderText(_translate("MainWindow", "#####"))
        self.baffle_number_lineEdit.setPlaceholderText(_translate("MainWindow", "####"))
        self.baffle_cost_lineEdit.setPlaceholderText(_translate("MainWindow", "$ ####.##"))
        self.label.setText(_translate("MainWindow", "Configuration:"))
        self.pushButton.setText(_translate("MainWindow", "Add Baffles"))
        self.menuSettings.setTitle(_translate("MainWindow", "Save/Load"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionLoad_Previous_Config.setText(_translate("MainWindow", "Load Previous Config"))

        # connecting PushBotton action "clicked" to PushButton_add
        self.pushButton.clicked.connect(on_click)

#TODO: connecting lineEdits to Return/EnterPress signals
        #self.baffle_number_lineEdit.returnPressed.connect(get_number_baffles())
        #self.baffle_cost_lineEdit.connect(enterPress)

    def calculate_baffle_cost(self):
        pass

    def get_baffles_cost():
        pass

@pyqtSlot()
def on_click(self):
    woo = open(".\\text_browser1.txt", 'a')
    woo.write("test")
    woo.close()


def pushButton_add():
    pass


def get_tube_OD():
    pass


def get_tubesheet_material():
    pass


def add_tubesheet():
    pass


def choose_tube_material():
    pass


def get_number_baffles():
    pass


def get_number_gaskets():
    pass


def get_gasket_cost():
    pass


def get_tube_bundle_length():
    pass


def calc_net_price():
    pass


def calc_list_price():
    pass


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def main():

    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()