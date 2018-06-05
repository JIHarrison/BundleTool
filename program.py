import sys
from bundle_tool_ui import Ui_MainWindow

from PyQt5 import QtWidgets


def get_estimate_number():
    pass


def get_tube_OD():
    pass


def get_tubesheet_material():
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