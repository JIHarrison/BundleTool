import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QValidator, QRegExpValidator, QActionEvent
from PyQt5.QtCore import pyqtSlot, QVariant, QStringListModel, pyqtBoundSignal
from PyQt5.QtWidgets import QInputDialog

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


        # baffle_cost lineEdit options/config
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
        self.textBrowser.setSource(QtCore.QUrl("file:///C:/Users/jharrison/Documents/GitHub/BundleTool/text_browser1.txt"))
        self.baffle_number_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.baffle_number_combobox.setGeometry(QtCore.QRect(30, 230, 81, 22))
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
        self.test_listview = QtWidgets.QListView(self.centralwidget)
        self.test_listview.setGeometry(QtCore.QRect(30, 270, 256, 51))
        self.test_listview.setStyleSheet("")
        self.test_listview.setObjectName("test_listview")
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
        self.total_tubing_label.setBuddy(self.total_tubing_lineEdit)
        self.tubesheet_material_label.setBuddy(self.tubesheet_combobox)
        self.tubesheet_diameter_label.setBuddy(self.tubesheet_diameter_combobox)
        self.label.setBuddy(self.configurator_listview_3)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tubesheet_combobox, self.tubesheet_diameter_combobox)
        MainWindow.setTabOrder(self.tubesheet_diameter_combobox, self.tube_material_combobox)
        MainWindow.setTabOrder(self.tube_material_combobox, self.tube_OD_combobox)
        MainWindow.setTabOrder(self.tube_OD_combobox, self.total_tubing_lineEdit)
        MainWindow.setTabOrder(self.total_tubing_lineEdit, self.baffle_number_combobox)
        MainWindow.setTabOrder(self.baffle_number_combobox, self.baffle_cost_lineEdit)
        MainWindow.setTabOrder(self.baffle_cost_lineEdit, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.textBrowser)
        MainWindow.setTabOrder(self.textBrowser, self.configurator_listview)
        MainWindow.setTabOrder(self.configurator_listview, self.configurator_listview_2)
        MainWindow.setTabOrder(self.configurator_listview_2, self.configurator_listview_3)


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
        self.baffle_cost_lineEdit.setPlaceholderText(_translate("MainWindow", "999max"))
        self.label.setText(_translate("MainWindow", "Configuration:"))
        self.pushButton.setText(_translate("MainWindow", "Add Baffles"))
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
        self.baffle_number_combobox.activated[str].connect(get_baffle_number)
        self.tubesheet_combobox.activated[str].connect(get_tubesheet_material)
        self.tubesheet_diameter_combobox.activated[str].connect(get_tubesheet_diameter)
        self.tube_material_combobox.activated[str].connect(get_tube_material)
        self.tube_OD_combobox.activated[str].connect(get_tube_OD)


        # connecting PushButton action "clicked" to their functions
        self.pushButton.clicked.connect(on_click)


        # connecting lineEdits to their functions
        # TODO connection works, need more functionality
        self.baffle_cost_lineEdit.textChanged[str].connect(get_baffle_cost)
        #self.baffle_cost_lineEdit.textEdited.connect(get_baffle_cost)
        #self.baffle_cost_lineEdit.editingFinished.connect(get_baffle_cost)


        # Sets an input mask to prevent any input over 999 for baffle_cost_lineEdit from user
        self.baffle_cost_lineEdit.setInputMask('')
        regexp = QtCore.QRegExp('^([1-9][0-9]{0,2}|1000)$')
        validator = QtGui.QRegExpValidator(regexp)
        self.baffle_cost_lineEdit.setValidator(validator)
        self.baffle_cost_lineEdit.setCursorPosition(0)


        # TODO load/save functionality
    #     self.actionLoad_Previous_Config.triggered.connect(self.file_open)
    #     openFile = QtGui.QAction("&Open File", self)
    #     openFile.setShortcut("Ctrl+O")
    #     openFile.setStatusTip('Open File')
    #     openFile.triggered.connect(self.file_open)
    #
    # def file_open(self):
    #     name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
    #     file = open(name, 'r')
    #
    #     self.editor()
    #
    #     with file:
    #         text = file.read()
    #         self.textEdit.setText(text)
    #
    # def editor(self):
    #     self.textEdit = QtGui.QTextEdit()
    #     self.setCentralWidget(self.textEdit)

# potential color scheme for correct input in a lineEdit, optional fluff
# @pyqtSlot()
# def check_state(self, *args, **kwargs):
#     sender = self.sender()
#     validator = sender.validator()
#     state = validator.validate(sender.text(), 0)[0]
#     if state == QtGui.QValidator.Acceptable:
#         color = '#c4df9b'  # green
#     elif state == QtGui.QValidator.Intermediate:
#         color = '#fff79a'  # yellow
#     else:
#         color = '#f6989d'  # red
#     sender.setStyleSheet('QLineEdit { background-color: %s }' % color)


def get_tubesheet_material(tubesheet_material):
    print("tubesheet material test")
    print(tubesheet_material)


def get_tubesheet_diameter(tubesheet_diameter):
    print("tubesheet diameter test")
    print(tubesheet_diameter)


def get_tube_material(tube_material):
    print("tube material test")
    print(tube_material)


def get_tube_OD(tube_OD):
    print("tube OD test")
    print(tube_OD)


# takes input from baffle_number_combobox
def get_baffle_number(number):
    print("baffle number test")
    print(number)

@pyqtSlot()
def on_click(self):
    print("on_click test")
    woo = open('./text_browser1.txt', 'a')
    woo.write("test ")
    QtGui.QGuiApplication.processEvents()
    woo.close()


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):

        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtGui.QGuiApplication.processEvents()

if __name__ == "__main__":
    def get_baffle_cost(cost):
        # just a test print; not for use
        print(cost)

    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()

    sys.exit(app.exec_())
